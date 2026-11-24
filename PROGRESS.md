# Agent Commerce MCP (Universal Open Web MCP Runner)
Jembatan otomatisasi pesanan berbasis protokol MCP (Model Context Protocol) untuk UMKM & Bisnis Lokal di Indonesia.

## 📌 Status Terakhir (Zero-Amnesia Protocol & Checkpoint Handoff)
Status per: Senin, 23 November 2026. Project disimpan sementara sesuai instruksi Tuan Yudi ("simpan nanti project ini").

### [x] Selesai & Terverifikasi:
1. **Core Arsitektur 3-Layer (`BLUEPRINT_ARSITEKTUR.md`):**
   - Layer 1: Client Open Web Runner (Universal HTML/JS, zero server cost).
   - Layer 2: Intelligence & Hub Proxy (`runner-api/src/server.py` FastAPI port 3891).
   - Layer 3: Merchant MCP Endpoint (`kedai-kopi-mcp` port 3890) & LuxWA Gateway (:3085).
   - Diagram interaktif live: `https://social.luxcyber.my.id/dl/arsitektur-agentic-commerce.html`.
2. **Open Web Runner Interface (`runner-web/public/index.html`):**
   - URL Live: `https://social.luxcyber.my.id/agent-runner/`.
   - Standar Anti-Slop: Palet slate-navy `#090c15`, font Plus Jakarta Sans & JetBrains Mono, zero ungu/biru generik.
   - Aksesibilitas WCAG AA, responsive touch-target jempol mobile (min 44px).
   - Fitur Voice Ordering (Web Speech API `id-ID`) via tombol mic interaktif.
   - Modal Onboarding Toko Mandiri `[+ Daftar Toko]` (`POST /api/merchants/register`).
3. **Backend Hub Engine & AI Intent (`runner-api/`):**
   - Rate limiting IP sliding window (20 req/menit), WAF input sanitizer.
   - Integrasi 9Router `ag/gemini-3.8-flash-medium` via SQLite dynamic token extraction.
   - Handler multi-item & cross-merchant parsing (kombinasi kopi + roti sekaligus).
4. **WhatsApp Bridge (LuxWA):**
   - Target nomor kasir resmi dikonfigurasi ke: `089675313633` (`6289675313633`).
   - Format pesan multi-item + opsi balas cepat kasir (1 / 2 / 0).
   - Riset perbandingan tombol interaktif: One-Click Action Links vs Native Flow Buttons Baileys.

### [/] Status Service Aktif di Background:
- `agent-runner-hub` (PM2 ID 31, Port 3891, CPU 0%, RAM ~9MB) -> STATUS: ONLINE
- `kedai-kopi-mcp` (PM2 ID 30, Port 3890, CPU 0%, RAM ~5MB) -> STATUS: ONLINE
- Nginx reverse-proxy: `/agent-runner/` -> 3891, `/kedai-kopi/` -> 3890.

### [ ] Next (Saat Tuan Ingin Melanjutkan):
1. **Pilihan Tombol Interaktif Kasir WA:**
   - Pasang Solusi A (Tautan 1-Klik `wa.me/...`) atau Solusi B (Native Flow Button Baileys) untuk nomor `089675313633`.
2. **Fitur Radius & Logistik:**
   - Geofencing batas antar (maksimal 3-5 km) atau mode Dine-In meja QR.
3. **QRIS Dinamis:**
   - Integrasi pop-up QRIS pembayaran sebelum pesanan dieksekusi kasir.

### 📦 Repository & Commit Checkpoint:
- Repo: `https://github.com/yudi1999/agent-commerce-mcp.git`
- Branch: `master`
- Terakhir commit: `c62fb03` (chore: update target wa kasir to 089675313633 and document interactive button technical feasibility).
