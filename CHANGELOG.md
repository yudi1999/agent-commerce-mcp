# Changelog

Semua perubahan dan evolusi project didokumentasikan di sini.

## [1.1.0-PROD] - 2026-11-23

### Ditambahkan
- **Engine UI Motion & Video Renderer (`scripts/render_video.py`):**
  - Mengimplementasikan standar skill `programmatic-ui-motion-video` dan `antislop-ui`.
  - Format 9:16 vertical (1080x1920 @ 30 FPS, 24 detik durasi).
  - Screen Studio camera (virtual zoom & pan halus).
  - Alur 4 scene: Order AI -> Protokol MCP -> Pembayaran QRIS -> Notifikasi WhatsApp Toko & Value Proposition UMKM.
- **Synthesizer Efek Suara Haptik (`scripts/generate_sfx.py`):**
  - Efek audio tactile tap, WhatsApp notification chime, dan chord QRIS success murni matematika gelombang tanpa asset bajakan.
- **Offload Rendering via GitHub Actions (`.github/workflows/render-video.yml`):**
  - Seluruh beban rendering video grafis dialihkan ke server GitHub Actions (bebas beban VPS).
  - Otomatis upload artefak video MP4 siap unduh.

## [1.0.0-PROD] - 2026-11-23

### Ditambahkan
- **Core MCP Server (`src/server.py`):**
  - Implementasi 3 tool utama untuk AI Agent: `cari_menu_produk`, `buat_pesanan`, dan `cek_status_pesanan`.
  - Format data katalog berbasis JSON sederhana (`src/catalog.json`) agar mudah di-sync dengan Excel/Google Sheets.
- **WhatsApp Notification Bridge (`src/notifier.py`):**
  - Simulasi pengiriman notifikasi pesanan ramah kasir ke WhatsApp/HP pemilik toko saat AI Agent melakukan checkout.
  - Logging riwayat pesanan otomatis ke file lokal (`src/orders_log.json`).
- **Panduan Edukasi & Pitching Lapangan (`docs/PITCHING_UMKM.md`):**
  - Skrip percakapan penawaran jasa instalasi terima beres untuk UMKM tanpa jargon teknis rumit.
  - Paket penawaran harga dan skema monetisasi riil (Setup Fee + Retainer).
- **Protokol Ketahanan Project (`PROGRESS.md`):**
  - Catatan status dan roadmap pengembangan lanjutan.

### Status Operasional
- **Status:** Siap dijadikan demonstrasi prototype & materi kampanye lapangan.
