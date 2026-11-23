# Changelog

Semua perubahan dan evolusi project didokumentasikan di sini.

## [1.2.0-PROD] - 2026-11-23

### Ditambahkan
- **Engine Video Animasi Edukasi MCP (`scripts/render_edukasi_video.py`):**
  - Durasi 30 detik format vertikal 9:16 (1080x1920 @ 30 FPS).
  - Mengimplementasikan standar kurikulum `iart-ai/motion-skills` & `motion-graphics-craft`.
  - Pacing 4 tahap:
    1. Detik 0-7: Perubahan perilaku konsumen (tidak browsing manual lagi, beralih ke agen AI).
    2. Detik 7-14: Masalah web tradisional (AI 'buta' melihat banner & button, butuh data mesin).
    3. Detik 14-22: Analogi awam MCP sebagai "colokan USB langsung dari toko ke otak AI", notifikasi masuk WhatsApp kasir toko tanpa potongan 20%.
    4. Detik 22-30: Penawaran jasa instalasi terima beres untuk UMKM lokal.
  - Fitur karaoke subtitles scroll-stopping dengan safe area band (terhindar dari UI TikTok/Reels).
  - Offloaded ke cloud runner GitHub Actions (0% beban VPS).

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
