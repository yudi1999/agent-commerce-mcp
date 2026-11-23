"""
Notifier Module: Menjembatani pesanan dari AI Agent ke WhatsApp/HP Kasir Toko.
Pemilik UMKM tidak perlu paham MCP/AI; mereka cukup terima notifikasi di WA seperti biasa.
"""
import os
import json
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

def kirim_notifikasi_kasir(order_data: dict) -> bool:
    """
    Format notifikasi ramah kasir dan kirim via webhook / WhatsApp gateway.
    """
    pesan = (
        f"🔔 *PESANAN BARU MASUK DARI ASISTEN AI!*\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"📋 *No. Pesanan:* {order_data.get('order_id')}\n"
        f"👤 *Nama Pemesan:* {order_data.get('customer_name')}\n"
        f"📱 *Kontak Pemesan:* {order_data.get('customer_contact')}\n"
        f"📍 *Alamat Kirim:* {order_data.get('delivery_address')}\n"
        f"🛒 *Detail Produk:* {order_data.get('item_name')} ({order_data.get('qty')} porsi)\n"
        f"💰 *Total Tagihan:* Rp {order_data.get('total'):,}\n"
        f"💳 *Metode:* {order_data.get('payment_method')} ({order_data.get('status')})\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"👉 *Tindakan Kasir:* Siapkan pesanan dan konfirmasi saat kurir/pemesan tiba."
    )
    
    # Cetak ke log atau integrasikan ke gateway WA (seperti Baileys / Waha / WA Gateway lokal)
    logging.info("Mengirim notifikasi pesanan ke WhatsApp Toko:")
    print(pesan)
    
    # Simpan log pesanan harian untuk rekap kasir
    log_file = os.path.join(os.path.dirname(__file__), "orders_log.json")
    orders = []
    if os.path.exists(log_file):
        try:
            with open(log_file, "r", encoding="utf-8") as f:
                orders = json.load(f)
        except Exception:
            orders = []
            
    orders.append(order_data)
    with open(log_file, "w", encoding="utf-8") as f:
        json.dump(orders, f, indent=2, ensure_ascii=False)
        
    return True

if __name__ == "__main__":
    # Test simulasi
    test_order = {
        "order_id": "ORD-TEST-01",
        "customer_name": "Tuan Yudi (via JARVIS)",
        "customer_contact": "089623829690",
        "delivery_address": "Jl. Kemenangan No. 99, Karawang",
        "item_name": "Kopi Susu Gula Aren",
        "qty": 2,
        "total": 36000,
        "payment_method": "QRIS",
        "status": "SUDAH_DIBAYAR"
    }
    kirim_notifikasi_kasir(test_order)
