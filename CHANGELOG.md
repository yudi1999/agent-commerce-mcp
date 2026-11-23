# Changelog

Semua perubahan dan evolusi project didokumentasikan di sini.

## [2.3.0-PROD] - 2026-11-23

### Ditambahkan (Super Dynamic Motion Graphics Suite)
- **Engine Motion Grafis v5 (`scripts/generate_html_scene_v5.py` & `templates/base.html`):**
  - **Animated Talking SVG Character:** Mata berkedip tiap 3.2 detik, mulut bergerak dinamis, kepala mengangguk (*head bobbing*), dan cincin gelombang kejut energi (*shockwave energy rings*) memancar dari smartphone ke AI.
  - **Floating App Chaos (Scene 1):** Ikon-ikon aplikasi toko jadul melayang dengan efek floating sinusoidal dan tag memori penuh (450MB, 380MB, 290MB).
  - **Dynamic Multi-Color Audio Visualizer (Scene 2):** Bar equalizer audio 18 baris dengan lonjakan ritmis biru-hijau dan particle glow.
  - **Cyber Glitch Alert & Error Crash (Scene 3):** Mockup browser bergetar glitching saat AI terhalang popup promo dan captcha robot.
  - **Pulsing Energy Pipe & Neon Glow (Scene 4):** Jalur data MCP berdenyut listrik oranye dengan gradient glow.
  - **Slam-In Stamp Effect (Scene 5):** Stempel merah `POTONGAN KOMISI: 0%` membanting layar dengan transisi scale cubic-bounce.
  - **Pulsing Glow CTA (Scene 6):** Kartu ajakan DM/PC berdenyut oranye terang (*pulsing neon button*).
- **Audio Tetap:** Gemini Puck 40.12 detik utuh tanpa terpotong.
- **Zero VPS Load:** Offload rendering Chromium ke GitHub Actions runner.
 
 ## [2.2.0-PROD] - 2026-11-23

### Diperbaiki Total (Root Cause Suara Kepotong & Desync Selesai 100%)
- **Akar Masalah Terbongkar:**
  - Sebelumnya suara narasi Gemini Puck terpotong di detik 30 karena limitasi endpoint `/api/v1/tts` memotong teks di 30 detik (`max_duration_sec: 30`), sehingga kata terakhir terpotong paksa dan visual bergerak terlalu cepat membalap audio.
- **Solusi Permanen 6 Segmen Utuh (`assets/audio/vo_storytelling_full.mp3`):**
  - Teks narasi dipecah menjadi 6 segmen kalimat murni tanpa batas pemotongan:
    1. Seg 1 (6.35s): *"Pernah sadar gak? Sekarang orang makin malas buka banyak aplikasi untuk belanja."*
    2. Seg 2 (7.55s): *"Mereka tinggal bilang ke asisten AI di HP: Pesanin kopi susu dua cup langsung kirim ke rumah."*
    3. Seg 3 (8.09s): *"Tapi masalahnya: AI itu buta! AI gak bisa klik banner promo atau web yang ribet."*
    4. Seg 4 (5.94s): *"Di sinilah protokol MCP bekerja. Menghubungkan toko Anda langsung ke otak AI."*
    5. Seg 5 (6.35s): *"Orderan langsung loncat ke WhatsApp kasir lengkap dengan QRIS, tanpa potongan komisi dua puluh persen!"*
    6. Seg 6 (5.84s): *"Mau toko Anda dipasangin terima beres? Cukup DM atau private chat sekarang juga!"*
  - Total durasi riil: **40.12 detik utuh** tanpa ada kata yang terpotong satu huruf pun.
- **Karakter Orang Animasi Aktif (`scripts/generate_html_scene_v4.py`):**
  - Karakter vektor Plus Jakarta aktif berbicara, mengangguk lembut, dan memegang HP memancarkan sinyal gelombang ke AI di Scene 1, 2, dan 6.
  - Timeline video dikunci mati mengikuti 40.12 detik audio (1203 frame @ 30 FPS).
- **Zero VPS Load:** Offload rendering ke GitHub Actions runner.
 
 ## [2.1.0-PROD] - 2026-11-23

### Diperbaiki (Animasi Karakter SVG Hidup & Sinkronisasi Audio Presisi)
- **Animasi Karakter Orang Bergerak (`scripts/generate_html_scene_v3.py`):**
  - Karakter vektor modern (Plus Jakarta style) dengan animasi kepala mengangguk (*head bobbing*), mulut berbicara sinkron narasi Puck, lengan memegang smartphone dengan denyut radiasi audio ke AI.
  - Menghilangkan kesan monoton/statis.
- **Sinkronisasi Presisi 6 Babak Audio (`assets/audio/vo_storytelling.mp3`):**
  - **0.0 - 5.5s:** "Pernah sadar gak? Orang makin malas buka banyak aplikasi..." (Karakter orang bercerita + Headline fenomena baru).
  - **5.5 - 10.5s:** "Tinggal bilang ke asisten AI: Pesanin kopi susu ke rumah..." (Karakter berbicara ke HP + Equalizer suara AI merespons).
  - **10.5 - 14.0s:** "Tapi masalahnya: AI itu buta! Gak bisa klik banner atau web ribet..." (Browser error crash, popup banner memblokir AI).
  - **14.0 - 21.0s:** "Di sinilah protokol MCP bekerja, menghubungkan toko Anda langsung ke otak AI..." (Diagram Toko <-> MCP <-> Otak AI + 3 poin alur).
  - **21.0 - 25.5s:** "Orderan langsung loncat ke WhatsApp kasir, tanpa potongan komisi 20%..." (Card WA Kasir + Stempel merah POTONGAN KOMISI: 0%).
  - **25.5 - 30.0s:** "Mau toko Anda dipasangin terima beres? Cukup DM / PC sekarang juga!" (Karakter tersenyum + Tombol oranye DM/PC Sekarang).
- **Zero VPS Load:** Offload ke runner GitHub Actions dengan browser Chromium asli.
 
 ## [2.0.0-PROD] - 2026-11-23

### Dirombak Total (HTML/CSS Browser-Engine Renderer)
- **Migrasi Penuh ke Headless Chromium (Playwright):**
  - Menghentikan 100% cara menggambar manual via PIL/sketsa garis primitif.
  - Menggunakan engine layout web modern (`templates/base.html` & `scripts/generate_html_scene.py`):
    - Font profesional: **Plus Jakarta Sans** (tebal, bersih, internasional) & **JetBrains Mono**.
    - Grid background gelap bertekstur modern (`#0c0d12` dengan grid halus 60px).
    - Komponen UI Card presisi tinggi dengan border halus dan bayangan alami.
    - Headline dinamis 64px dengan teks highlight kontras tinggi.
    - Status audio waveform dinamis, mockup browser error SVG, diagram alur MCP terstandarisasi, dan bubble WhatsApp Kasir resmi.
    - 3 Pill navigasi bawah bernomor (`01 KEBIASAAN`, `02 MASALAH AI`, `03 PROTOKOL MCP`) yang menyala oranye persis `@benergak_v1`.
  - Suara tetap menggunakan Gemini Puck 30.0 detik pas.
  - Kompilasi otomatis di cloud runner GitHub Actions (0% beban VPS).
 
## [1.6.0-PROD] - 2026-11-23

### Ditambahkan
- **Engine Motion Explainer 100% Persis Arsitektur `@benergak_v1` (`scripts/render_benergak_authentic.py`):**
  - Menerapkan tata letak 3-Tier identik:
    1. **Top Tier:** Headline tebal berwibawa di kiri atas + badge kategori topik oranye (`● POLA KONSUMEN`, `● KEBUNTUAN SISTEM`, `● SOLUSI PROTOKOL`, `● HASIL OPERASIONAL`).
    2. **Middle Tier (Objek & Subjek Riil):**
       - Ilustrasi line-art karakter minimalis memegang ponsel dengan gelombang sinyal audio terpancar.
       - Mockup browser toko konvensional gagal: popup iklan berkedip, form alamat ruwet, captcha yang memblokir AI.
       - Garis sirkuit titik-titik bergerak (*dotted tracking flow*) menghubungkan Toko UMKM langsung ke Otak AI melalui jembatan pipa oranye `⚡ PROTOKOL MCP ⚡`.
       - Notifikasi WhatsApp kasir masuk nota lunas QRIS + stempel kotak merah raksasa `POTONGAN KOMISI: 0%`.
    3. **Bottom Tier:** 3 Pill navigasi bernomor (`01 KEBIASAAN`, `02 MASALAH AI`, `03 PROTOKOL MCP`) yang menyala oranye bergantian mengikuti babak narasi.
  - Call-to-Action bersih di akhir video: **`📩 CUKUP DM / PC SEKARANG`** (Jasa Pasang Terima Beres • Konsultasi Gratis).
  - Voiceover studio Gemini Puck 30.0 detik pas.
  - Kompilasi offloaded ke cloud runner GitHub Actions (0% beban VPS).
 
## [1.5.0-PROD] - 2026-11-23

### Ditambahkan
- **Engine Motion Explainer Sinematik ala `@benergak_v1` (`scripts/render_story_explainer.py`):**
  - Menerapkan kurikulum lengkap `video-shotcraft` (124 shot recipes):
    1. **Hook Audio Waveform (Detik 0–6.5s):** Ilustrasi smartphone dengan equalizer audio bergerak saat user memesan ke asisten AI.
    2. **Visual Problem "AI Buta" (Detik 6.5–12.5s):** Browser mockup error merah yang menunjukkan AI tidak bisa klik banner promo atau form ruwet.
    3. **Jembatan Kabel Berpendar MCP (Detik 12.5–18.5s):** Analogi visual kabel data glowing yang menghubungkan Toko UMKM langsung ke Otak AI.
    4. **WhatsApp Kasir & Stempel Komisi 0% (Detik 18.5–24.5s):** UI bubble WhatsApp pesanan masuk + stempel merah potongan ojol 0%.
    5. **Lockup Penutup (Detik 24.5–30.0s):** Ajakan jelas dan bersih: `📩 Cukup DM / PC Sekarang`.
  - Menggunakan suara natural studio Gemini Puck dengan pacing storytelling 30 detik pas.
  - Offloaded ke cloud runner GitHub Actions (0% beban VPS).
 
## [1.4.0-PROD] - 2026-11-23

### Ditambahkan
- **Engine Masterpiece Motion Design v2 (`scripts/render_voice_masterpiece.py`):**
  - Mengintegrasikan suara studio natural non-robot (Gemini Speech Broadcast Voice `Puck` dengan post-processing compand & atempo tebal).
  - Call-to-Action disesuaikan: Menghapus nomor kontak WhatsApp, digantikan ajakan organik **`📩 Cukup DM / PC Sekarang`**.
  - Durasi presisi 22.0 detik sinkron dengan audio narasi studio.
  - Kompilasi dan perenderan di-offload ke cloud runner GitHub Actions (0% beban VPS).
 
## [1.3.0-PROD] - 2026-11-23

### Ditambahkan
- **Engine Masterpiece Motion Design (`scripts/render_masterpiece.py`):**
  - Mengadopsi prinsip motion design senior dari suite `iart-ai/motion-skills` (`animation-principles`, `motion-art-direction`, `shot-composition`).
  - Menghilangkan penyakit *acak-acakan* dan *visual overcrowding*:
    - **One Focal Point per Shot:** 1 layar hanya memiliki 1 hero ide besar, bukan menumpuk 10 kotak sekaligus.
    - **Asymmetric Snappy Easing:** Transisi masuk menggunakan `ease-out cubic` (`1 - (1-t)^3`) untuk entri cepat dan perlambatan halus berbobot.
    - **Stagger 60-120ms:** Elemen pendukung muncul secara teratur setelah headline utama mendarat.
    - **3-Layer Depth:** Ambient subtle grid, secondary surface card, primary giant typography.
    - **Palette Minimalis:** Obsidian Slate Dark (`#0b0d11`) + Stripe/Apple clean typography.
  - Offloaded ke cloud GitHub Actions (0% beban VPS).

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
