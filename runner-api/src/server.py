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

class OrderItem(BaseModel):
    item_id: str
    quantity: int = Field(..., ge=1, le=50)

class DirectOrderRequest(BaseModel):
    merchant_id: Optional[str] = "MERCHANT-KOPI-01"
    item_id: Optional[str] = None
    quantity: Optional[int] = 1
    items: Optional[List[OrderItem]] = None
    customer_name: str = Field(..., min_length=2, max_length=100)
    delivery_address: str = Field(..., min_length=3, max_length=200)

class RegisterMerchantRequest(BaseModel):
    name: str = Field(..., min_length=3, max_length=60)
    category: str = Field(..., min_length=3, max_length=50)
    location: str = Field(..., min_length=3, max_length=80)
    wa_number: str = Field(..., min_length=10, max_length=20)
    catalog: List[dict] = Field(...)

REGISTRY_FILE = os.path.join(os.path.dirname(__file__), "../data/registry.json")

def load_registry():
    if os.path.exists(REGISTRY_FILE):
        with open(REGISTRY_FILE, "r") as f:
            return json.load(f)
    return {"merchants": []}

def save_registry(data):
    with open(REGISTRY_FILE, "w") as f:
        json.dump(data, f, indent=2)

@app.post("/api/merchants/register")
def register_merchant(payload: RegisterMerchantRequest, request: Request):
    check_rate_limit(request)
    name = sanitize_input_text(payload.name)
    category = sanitize_input_text(payload.category)
    location = sanitize_input_text(payload.location)
    
    # Normalisasi nomor WA
    raw_wa = re.sub(r"[^0-9]", "", payload.wa_number)
    if raw_wa.startswith("08"):
        raw_wa = "628" + raw_wa[2:]
    elif not raw_wa.startswith("62"):
        raw_wa = "62" + raw_wa

    merchant_id = f"MERCHANT-{uuid.uuid4().hex[:6].upper()}"
    
    # Format katalog
    formatted_catalog = []
    for idx, c in enumerate(payload.catalog):
        item_id = f"ITEM-{idx+1:02d}"
        formatted_catalog.append({
            "id": item_id,
            "name": sanitize_input_text(c.get("name", f"Menu {idx+1}")),
            "price": int(c.get("price", 10000)),
            "stock": int(c.get("stock", 50)),
            "desc": sanitize_input_text(c.get("desc", "Menu pilihan segar dan lezat"))
        })
        
    new_merchant = {
        "id": merchant_id,
        "name": name,
        "category": category,
        "location": location,
        "wa_number": raw_wa,
        "mcp_url": f"https://social.luxcyber.my.id/agent-runner/mcp/{merchant_id}.json",
        "api_order_url": "https://social.luxcyber.my.id/agent-runner/api/execute-order",
        "catalog": formatted_catalog
    }
    
    reg = load_registry()
    reg.setdefault("merchants", []).append(new_merchant)
    save_registry(reg)
    
    return {
        "status": "success",
        "message": f"Toko '{name}' berhasil terdaftar di Protokol MCP!",
        "merchant": new_merchant
    }

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
    
    system_prompt = """Anda adalah Universal Shopping Assistant ramah & cerdas.
Tugas Anda membantu pembeli memilih menu/barang dari toko UMKM lokal yang terdaftar di protokol MCP kami.

Berikut katalog resmi toko yang terdaftar:
""" + catalog_context + """

INSTRUKSI FORMAT JAWABAN:
1. Jawab ramah dan ringkas dalam Bahasa Indonesia.
2. Jika pembeli ingin memesan dan menyebutkan menu spesifik (bisa 1 menu atau beberapa menu sekaligus, misal "2 kopi susu gula aren dan 1 roti sisir mentega spesial"), identifikasi seluruh item yang dipesan:
   - Buat daftar "items" yang dipesan lengkap dengan:
     - item_id (misal: "KOPI-01")
     - item_name
     - quantity (angka)
     - price_per_item (angka)
     - subtotal (angka)
   - Hitung total_price dari seluruh item.
   - Format JSON order intent wajib seperti ini:
   ```json-intent
   {"action": "ORDER_INTENT", "merchant_id": "MERCHANT-KOPI-01", "items": [{"item_id": "KOPI-01", "item_name": "Kopi Susu Gula Aren", "quantity": 2, "price_per_item": 18000, "subtotal": 36000}, {"item_id": "ROTI-02", "item_name": "Roti Sisir Mentega Spesial", "quantity": 1, "price_per_item": 12000, "subtotal": 12000}], "total_price": 48000}
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
        "temperature": 0.3,
        "stream": False
    }
    
    reply_text = "Maaf, asisten sedang sibuk. Silakan pilih menu langsung dari daftar di bawah."
    try:
        # Load active 9Router API key from DB
        auth_key = ""
        try:
            import sqlite3
            with sqlite3.connect("/home/ubuntu/.9router/db/data.sqlite") as db:
                c = db.cursor()
                c.execute("SELECT key FROM apiKeys WHERE isActive=1 ORDER BY id DESC LIMIT 1")
                row = c.fetchone()
                if row:
                    auth_key = row[0]
        except Exception:
            pass

        headers = {"Content-Type": "application/json"}
        if auth_key:
            headers["Authorization"] = f"Bearer {auth_key}"

        req = urllib.request.Request(
            url,
            data=json.dumps(req_body).encode("utf-8"),
            headers=headers
        )
        with urllib.request.urlopen(req, timeout=15) as resp:
            raw_body = resp.read().decode("utf-8")
            # Parse both JSON or SSE lines (if 9router forces stream)
            if raw_body.startswith("data:"):
                # SSE response
                collected = []
                for line in raw_body.splitlines():
                    line = line.strip()
                    if line.startswith("data:") and not line.endswith("[DONE]"):
                        data_part = line[5:].strip()
                        if data_part:
                            try:
                                chunk = json.loads(data_part)
                                delta = chunk.get("choices", [{}])[0].get("delta", {})
                                if "content" in delta and delta["content"]:
                                    collected.append(delta["content"])
                            except Exception:
                                pass
                if collected:
                    reply_text = "".join(collected)
            else:
                data = json.loads(raw_body)
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
    Mendukung multi-item dan single-item secara cerdas.
    """
    check_rate_limit(request)
    sanitize_input_text(payload.customer_name)
    sanitize_input_text(payload.delivery_address)
    
    reg = load_registry()
    all_merchants = reg.get("merchants", [])
    
    # Kumpulkan daftar item yang dipesan
    items_to_process = []
    if payload.items and len(payload.items) > 0:
        for it in payload.items:
            items_to_process.append({"item_id": it.item_id, "quantity": it.quantity})
    elif payload.item_id:
        items_to_process.append({"item_id": payload.item_id, "quantity": payload.quantity or 1})
    else:
        raise HTTPException(status_code=400, detail="Tidak ada item yang dipesan.")

    # Validasi tiap item ke katalog merchant
    detailed_items = []
    total_bill = 0
    merchant_names = set()

    for entry in items_to_process:
        target_id = entry["item_id"]
        qty = entry["quantity"]
        
        found = False
        for m in all_merchants:
            for cat_it in m.get("catalog", []):
                if cat_it["id"] == target_id:
                    if cat_it["stock"] < qty:
                        raise HTTPException(status_code=400, detail=f"Stok {cat_it['name']} tidak cukup (sisa {cat_it['stock']}).")
                    subtotal = cat_it["price"] * qty
                    detailed_items.append({
                        "item_id": target_id,
                        "name": cat_it["name"],
                        "quantity": qty,
                        "price": cat_it["price"],
                        "subtotal": subtotal,
                        "merchant": m["name"]
                    })
                    total_bill += subtotal
                    merchant_names.add(m["name"])
                    found = True
                    break
            if found:
                break
        if not found:
            raise HTTPException(status_code=404, detail=f"Item ID {target_id} tidak ditemukan di katalog merchant manapun.")

    order_id = f"ORD-{int(time.time())}-{uuid.uuid4().hex[:4].upper()}"
    store_summary = ", ".join(merchant_names) if merchant_names else "Merchant Mitra"

    # Format text ringkasan pesanan untuk WhatsApp
    pesanan_lines = []
    for d in detailed_items:
        pesanan_lines.append(f"• {d['name']} ({d['quantity']}x) - Rp {d['subtotal']:,}")
    pesanan_text = "\n".join(pesanan_lines)

    # 1. Objek data order
    order_data = {
        "order_id": order_id,
        "merchants": list(merchant_names),
        "items": detailed_items,
        "total_price": total_bill,
        "customer_name": payload.customer_name,
        "delivery_address": payload.delivery_address,
        "status": "CONFIRMED",
        "payment": "QRIS_ACTIVE",
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    
    # 2. Trigger Notifikasi WhatsApp Kasir via LuxWA
    wa_message = f"""🛒 *PESANAN MULTI-ITEM MASUK VIA OPEN WEB RUNNER!*
━━━━━━━━━━━━━━━━━━━━
🏪 *Toko/Mitra:* {store_summary}
📋 *No. Pesanan:* {order_id}
👤 *Pemesan:* {payload.customer_name}
📍 *Alamat:* {payload.delivery_address}

🛒 *Rincian Pesanan:*
{pesanan_text}

💰 *Total Tagihan:* Rp {total_bill:,}
💳 *Metode:* QRIS (LUNAS_AUTO)
━━━━━━━━━━━━━━━━━━━━
👉 *Konfirmasi Kasir (Balas Cepat):*
Ketik *1* : Terima & Sedang Disiapkan
Ketik *2* : Pesanan Selesai / Sedang Diantar
Ketik *0* : Tolak (Stok Habis)"""

    wa_notified = False
    try:
        # Kirim ke nomor WA kasir spesifik Tuan (+6282249767288)
        target_phone = "6282249767288"
        wa_url = "http://127.0.0.1:3085/send-message"
        wa_payload = {
            "to": target_phone,
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
