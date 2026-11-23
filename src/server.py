"""
MCP Commerce Server untuk Toko / Resto Lokal UMKM.
Mengekspos kemampuan pencarian produk, order intent, dan cek status ke AI Agent pembeli.
"""
import os
import json
from mcp.server.fastmcp import FastMCP
from notifier import kirim_notifikasi_kasir

# Inisialisasi MCP Server
mcp = FastMCP("TokoUMKM-Commerce-Bridge")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CATALOG_PATH = os.path.join(BASE_DIR, "catalog.json")
ORDERS_PATH = os.path.join(BASE_DIR, "orders.json")

def load_catalog():
    if not os.path.exists(CATALOG_PATH):
        return []
    with open(CATALOG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def load_orders():
    if not os.path.exists(ORDERS_PATH):
        return {}
    with open(ORDERS_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def save_orders(orders):
    with open(ORDERS_PATH, "w", encoding="utf-8") as f:
        json.dump(orders, f, indent=2, ensure_ascii=False)

@mcp.tool()
def cari_menu_produk(kata_kunci: str = "") -> list:
    """
    Cari daftar menu makanan/minuman atau produk toko yang sedang tersedia beserta harga & stok.
    """
    catalog = load_catalog()
    if not kata_kunci.strip():
        return catalog
    
    query = kata_kunci.lower().strip()
    return [
        item for item in catalog
        if query in item["nama"].lower() or query in item.get("deskripsi", "").lower() or query in item.get("kategori", "").lower()
    ]

@mcp.tool()
def buat_pesanan(
    produk_id: str,
    jumlah: int,
    nama_pemesan: str,
    kontak_pemesan: str,
    alamat_pengiriman: str
) -> dict:
    """
    Membuat pesanan baru oleh AI Agen atas nama pembeli.
    Mengunci stok dan menghasilkan instruksi tagihan pembayaran QRIS toko.
    """
    catalog = load_catalog()
    target_item = next((item for item in catalog if item["id"] == produk_id), None)
    
    if not target_item:
        return {"sukses": False, "pesan": f"Produk dengan ID '{produk_id}' tidak ditemukan di katalog toko."}
    
    if target_item.get("stok", 0) < jumlah:
        return {
            "sukses": False,
            "pesan": f"Stok tidak mencukupi. Sisa stok {target_item['nama']}: {target_item.get('stok', 0)} unit."
        }
    
    orders = load_orders()
    order_id = f"ORD-{len(orders) + 1001}"
    total_bayar = target_item["harga"] * jumlah
    
    order_entry = {
        "order_id": order_id,
        "customer_name": nama_pemesan,
        "customer_contact": kontak_pemesan,
        "delivery_address": alamat_pengiriman,
        "item_id": produk_id,
        "item_name": target_item["nama"],
        "qty": jumlah,
        "total": total_bayar,
        "payment_method": "QRIS Dinamis",
        "status": "MENUNGGU_PEMBAYARAN"
    }
    
    orders[order_id] = order_entry
    save_orders(orders)
    
    # Kirim notifikasi seketika ke WhatsApp Kasir UMKM
    kirim_notifikasi_kasir(order_entry)
    
    return {
        "sukses": True,
        "order_id": order_id,
        "nama_produk": target_item["nama"],
        "jumlah": jumlah,
        "total_harga": total_bayar,
        "status": "MENUNGGU_PEMBAYARAN",
        "instruksi_pembayaran": {
            "metode": "QRIS",
            "qris_string": f"00020101021126570014ID.TOKOUMKM.WWW011893600911000{order_id}5802ID5303360540{total_bayar}5802ID",
            "catatan": "Tampilkan QRIS ini ke pemesan atau bayar lewat delegated agent wallet."
        }
    }

@mcp.tool()
def cek_status_pesanan(order_id: str) -> dict:
    """
    Cek status proses pesanan (Menunggu Pembayaran, Sedang Disiapkan, Sedang Diantar, Selesai).
    """
    orders = load_orders()
    if order_id not in orders:
        return {"sukses": False, "pesan": f"Pesanan dengan nomor {order_id} tidak terdaftar."}
    
    order = orders[order_id]
    return {
        "sukses": True,
        "order_id": order_id,
        "status": order["status"],
        "produk": order["item_name"],
        "jumlah": order["qty"],
        "total": order["total"],
        "alamat": order["delivery_address"]
    }

if __name__ == "__main__":
    mcp.run()
