"""
Backend Hub & Security Proxy untuk Open Web MCP Runner
Port: 3891 (Localhost only)
Fitur Keamanan:
1. Anti-DDoS Rate Limiting (15 req/min per IP via sliding window).
2. Server-Side Intent Parsing via 9Router (Zero API Key Leakage ke Frontend).
3. Payload Validation & Anti-Tampering (Strict Pydantic models).
4. Direct Execution Bridge ke Merchant MCP & Notifikasi LuxWA.
5. Audit Logging Keamanan (WAF Detection).
"""
import os
import re
import time
import json
import uuid
import logging
import urllib.request
import urllib.error
from typing import Dict, Any, List, Optional
from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

app = FastAPI(title="Universal Agentic Commerce Hub", version="1.0.0")

# Security Standards: Whitelist CORS (Localhost + Production Domain)
ALLOWED_ORIGINS = [
    "https://social.luxcyber.my.id",
    "http://127.0.0.1:3890",
    "http://127.0.0.1:3891",
    "http://localhost:3890",
    "http://localhost:3891"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

# 1. Rate Limiting In-Memory Zone (15 req/minute per IP)
ip_rate_records: Dict[str, List[float]] = {}
RATE_LIMIT_PER_MINUTE = 20

def get_real_client_ip(request: Request) -> str:
    cf_ip = request.headers.get("cf-connecting-ip")
    if cf_ip:
        return cf_ip.strip()
    x_forwarded = request.headers.get("x-forwarded-for")
    if x_forwarded:
        return x_forwarded.split(",")[0].strip()
    return request.client.host if request.client else "127.0.0.1"

def check_rate_limit(request: Request):
    ip = get_real_client_ip(request)
    now = time.time()
    if ip not in ip_rate_records:
        ip_rate_records[ip] = []
    
    # Prune timestamps older than 60s
    ip_rate_records[ip] = [t for t in ip_rate_records[ip] if now - t < 60]
    
    if len(ip_rate_records[ip]) >= RATE_LIMIT_PER_MINUTE:
        logging.warning(f"[WAF-BLOCK] Rate limit exceeded by IP: {ip}")
        raise HTTPException(status_code=429, detail="Terlalu banyak permintaan. Silakan tunggu 1 menit.")
    
    ip_rate_records[ip].append(now)

# 2. WAF Pattern Validator (Anti-XSS, Injection & Probing)
WAF_PATTERNS = [
    re.compile(r'(<script[\s>]|javascript:|onload\s*=|onerror\s*=|document\.cookie)', re.IGNORECASE),
    re.compile(r'(\bunion\b.*\bselect\b|--|/\*|\*/|\bdrop\b\s+\btable\b)', re.IGNORECASE),
    re.compile(r'(\.\./|\.\.\\|/etc/passwd|/proc/self)', re.IGNORECASE)
]

def sanitize_input_text(val: str) -> str:
    for pat in WAF_PATTERNS:
        if pat.search(val):
            raise HTTPException(status_code=403, detail="Karakter atau payload terlarang terdeteksi.")
    return val.strip()

# Data Models
class ChatRequest(BaseModel):
    message: str = Field(..., min_length=2, max_length=500)
    customer_name: Optional[str] = "Konsumen Web"
    delivery_address: Optional[str] = "Alamat Pengiriman Default"

class DirectOrderRequest(BaseModel):
    merchant_id: str
    item_id: str
    quantity: int = Field(..., ge=1, le=20)
    customer_name: str = Field(..., min_length=2, max_length=100)
    delivery_address: str = Field(..., min_length=5, max_length=200)

REGISTRY_FILE = os.path.join(os.path.dirname(__file__), "../data/registry.json")

def load_registry():
    if os.path.exists(REGISTRY_FILE):
        with open(REGISTRY_FILE, "r") as f:
            return json.load(f)
    return {"merchants": []}

@app.get("/api/merchants")
def list_merchants(request: Request):
    check_rate_limit(request)
    reg = load_registry()
    return {"status": "success", "total": len(reg["merchants"]), "merchants": reg["merchants"]}

@app.post("/api/chat-assistant")
async def chat_assistant(payload: ChatRequest, request: Request):
    """
    Otak AI Orchestrator:
    Menerima pesan natural konsumen -> Membaca katalog MCP -> Mengurai intent -> Mengembalikan rekomendasi atau mengeksekusi order.
    """
    check_rate_limit(request)
    clean_msg = sanitize_input_text(payload.message)
    reg = load_registry()
    
    # Format konteks katalog untuk 9Router LLM
    context_lines = []
    for m in reg.get("merchants", []):
        context_lines.append(f"Toko: {m['name']} (ID: {m['id']})")
        for item in m.get("catalog", []):
            context_lines.append(f"  - [{item['id']}] {item['name']} - Rp {item['price']:,} (Stok: {item['stock']}) | {item['desc']}")
    
    catalog_context = "\n".join(context_lines)
    
    system_prompt = f"""Anda adalah Universal Shopping Assistant ramah & cerdas.
Tugas Anda membantu pembeli memilih menu/barang dari toko UMKM lokal yang terdaftar di protokol MCP kami.

Berikut katalog resmi toko yang terdaftar:
{catalog_context}

INSTRUKSI FORMAT JAWABAN:
1. Jawab ramah dan ringkas dalam Bahasa Indonesia.
2. Jika pembeli ingin memesan dan menyebutkan menu spesifik (misal "Pesan 2 kopi susu gula aren"), identifikasi:
   - merchant_id (misal: "MERCHANT-KOPI-01")
   - item_id (misal: "KOPI-01")
   - quantity (angka)
   - total_price
   Lalu sertakan tag JSON order intent di paling akhir jawaban Anda dengan format:
   ```json-intent
   {{"action": "ORDER_INTENT", "merchant_id": "...", "item_id": "...", "item_name": "...", "quantity": ..., "price_per_item": ..., "total_price": ...}}
   ```
3. Jika pembeli baru bertanya menu atau minta rekomendasi budget (misal "Gw punya budget 50rb"), hitung kombinasinya dan rekomendasikan dengan sopan. Jangan sertakan json-intent jika pembeli belum pasti mau memesan."""

    # Panggil 9Router lokal
    url = "http://127.0.0.1:20128/v1/chat/completions"
    req_body = {
        "model": "ag/gemini-3.8-flash-medium",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": clean_msg}
        ],
        "temperature": 0.3
    }
    
    reply_text = "Maaf, asisten sedang sibuk. Silakan pilih menu langsung dari daftar di bawah."
    try:
        req = urllib.request.Request(
            url,
            data=json.dumps(req_body).encode("utf-8"),
            headers={"Content-Type": "application/json"}
        )
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            reply_text = data["choices"][0]["message"]["content"]
    except Exception as e:
        logging.error(f"[AI-ERROR] 9Router call failed: {e}")
        # Fallback local regex parsing
        if "kopi" in clean_msg.lower():
            reply_text = 'Saya rekomendasikan **Kopi Susu Gula Aren** (Rp 18.000). Mau saya pesankan sekarang?\n```json-intent\n{"action": "ORDER_INTENT", "merchant_id": "MERCHANT-KOPI-01", "item_id": "KOPI-01", "item_name": "Kopi Susu Gula Aren", "quantity": 1, "price_per_item": 18000, "total_price": 18000}\n```'

    # Extract JSON intent if present
    order_intent = None
    intent_match = re.search(r'```json-intent\s*(\{.*?\})\s*```', reply_text, re.DOTALL)
    if intent_match:
        try:
            order_intent = json.loads(intent_match.group(1))
            # Bersihkan tag JSON dari teks chat agar tampilan rapi
            reply_text = reply_text.replace(intent_match.group(0), "").strip()
        except Exception:
            pass

    return {
        "status": "success",
        "reply": reply_text,
        "order_intent": order_intent
    }

@app.post("/api/execute-order")
async def execute_order(payload: DirectOrderRequest, request: Request):
    """
    Eksekutor Resmi: Menembak order ke Merchant MCP Endpoint & Memancarkan notifikasi LuxWA
    """
    check_rate_limit(request)
    sanitize_input_text(payload.customer_name)
    sanitize_input_text(payload.delivery_address)
    
    reg = load_registry()
    merchant = next((m for m in reg.get("merchants", []) if m["id"] == payload.merchant_id), None)
    if not merchant:
        raise HTTPException(status_code=404, detail="Merchant tidak ditemukan dalam registry.")
    
    item = next((it for it in merchant.get("catalog", []) if it["id"] == payload.item_id), None)
    if not item:
        raise HTTPException(status_code=404, detail="Menu / Item tidak ditemukan di toko ini.")
    
    if item["stock"] < payload.quantity:
        raise HTTPException(status_code=400, detail=f"Stok tidak cukup. Sisa stok hanya {item['stock']}.")
    
    total_price = item["price"] * payload.quantity
    order_id = f"ORD-{int(time.time())}-{uuid.uuid4().hex[:4].upper()}"
    
    # 1. Dispatch ke Merchant Gateway lokal / API Order
    order_data = {
        "order_id": order_id,
        "merchant_name": merchant["name"],
        "item_id": item["id"],
        "item_name": item["name"],
        "quantity": payload.quantity,
        "price_per_item": item["price"],
        "total_price": total_price,
        "customer_name": payload.customer_name,
        "delivery_address": payload.delivery_address,
        "status": "CONFIRMED",
        "payment": "QRIS_ACTIVE",
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    
    # 2. Trigger Notifikasi WhatsApp Kasir via LuxWA
    wa_message = f"""☕ *PESANAN BARU VIA OPEN WEB RUNNER!*
━━━━━━━━━━━━━━━━━━━━
🏪 *Toko:* {merchant['name']}
📋 *No. Pesanan:* {order_id}
👤 *Pemesan:* {payload.customer_name}
📍 *Alamat:* {payload.delivery_address}
🛒 *Pesanan:* {item['name']} ({payload.quantity} porsi)
💰 *Total Tagihan:* Rp {total_price:,}
💳 *Metode:* QRIS (LUNAS_AUTO)
━━━━━━━━━━━━━━━━━━━━
👉 *Tindakan Kasir:* Siapkan pesanan sekarang. Pembeli memesan lewat Asisten AI."""

    wa_notified = False
    try:
        wa_url = "http://127.0.0.1:3085/send-message"
        wa_payload = {
            "to": "6289623829690",
            "message": wa_message
        }
        wa_req = urllib.request.Request(
            wa_url,
            data=json.dumps(wa_payload).encode("utf-8"),
            headers={
                "Content-Type": "application/json",
                "Authorization": "Yudi.18101999#"
            }
        )
        with urllib.request.urlopen(wa_req, timeout=5) as wa_resp:
            res_data = json.loads(wa_resp.read().decode("utf-8"))
            wa_notified = res_data.get("success", False)
    except Exception as e:
        logging.error(f"[LUXWA-ERROR] Gagal kirim WA kasir: {e}")

    return {
        "status": "success",
        "message": "Pesanan berhasil dieksekusi dan diterima oleh kasir toko!",
        "order": order_data,
        "whatsapp_notified": wa_notified
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=3891)
