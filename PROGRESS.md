# Agent Commerce MCP (TokoAgent Bridge)
Jembatan otomatisasi pesanan berbasis protokol MCP (Model Context Protocol) untuk UMKM & Bisnis Lokal di Indonesia.

## 📌 Status Pengerjaan (Zero-Amnesia Protocol)
- [x] Inisialisasi struktur repo & konsep bisnis hybrid (Teknologi Modern + Pendekatan Awam UMKM).
- [x] Engine MCP Server (`src/server.py`) dengan dukungan JSON-RPC Tool:
  - `cari_menu_produk`: Pencarian produk/menu toko real-time.
  - `buat_pesanan`: Reservasi pesanan, hitung total, dan generate instruksi bayar QRIS.
  - `cek_status_pesanan`: Tracking pesanan oleh AI Agen pembeli.
- [x] WhatsApp/Webhook Bridge mockup (`src/notifier.py`) agar kasir UMKM menerima pesanan di HP mereka.
- [x] Panduan Edukasi & Skrip Penawaran Lapangan (`docs/PITCHING_UMKM.md`) dengan bahasa non-teknis.
- [x] Changelog perdana (`CHANGELOG.md`).

## 🚀 Komponen
1. `src/server.py` - FastMCP Server untuk AI Agents (Claude, JARVIS, ChatGPT, dll).
2. `src/catalog.json` - Database produk sederhana, mudah diedit pemilik toko.
3. `src/notifier.py` - Pengirim notifikasi otomatis ke WA/Telegram Kasir saat AI checkout.
4. `docs/PITCHING_UMKM.md` - Dokumen penawaran jasa instalasi & edukasi UMKM.
