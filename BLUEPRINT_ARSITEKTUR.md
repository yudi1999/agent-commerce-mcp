# Blueprint & Arsitektur Universal Agentic Commerce (Open Web MCP Runner)
Dokumen spesifikasi arsitektur teknis dan eksekusi platform.

## 📌 Status Pengerjaan (Zero-Amnesia Protocol)
- [x] Selesai:
  - Validasi ekosistem AI Browser & MCP limits (OpenAI & Gemini Sandbox Boundaries).
  - Desain arsitektur 3-Layer (Client Runner, Orchestrator Hub, Merchant Node).
  - Blueprint interaktif arsitektur sistem (`agentic-commerce.html`) via Archify engine.
  - Deployment live blueprint di https://social.luxcyber.my.id/dl/arsitektur-agentic-commerce.html
- [/] In Progress:
  - Perancangan spesifikasi antarmuka Open Web Runner (Universal AI Shopping Portal).
- [ ] Next:
  - Implementasi prototype frontend web client (Voice & Text conversational UI).
  - Integrasi multi-merchant MCP routing di backend VPS.

## 🏛️ Detail Arsitektur Sistem

### 1. Layer 1: Client Runner (Universal Open Web App)
- **Host:** GitHub Pages / Netlify (0 cost, global CDN).
- **Fungsi:** Menyediakan antarmuka chat & suara percakapan bebas hambatan sandbox.
- **Teknologi:** Lightweight SPA (Tailwind + Vanilla JS/Vue), Speech-to-Text native browser.

### 2. Layer 2: Intelligence & Gateway Bridge (VPS Node)
- **AI Orchestrator:** 9Router (ag/gemini-3.8-medium & Groq Llama-3.3-70B) untuk pemahaman maksud user dan penghitungan matematika keranjang belanja.
- **MCP Registry Hub:** Database katalog dan skema protokol merchant UMKM lokal.
- **Universal Bridge Executor:** FastAPI daemon (:3890) yang mengeksekusi request order mutasi secara valid dan aman.

### 3. Layer 3: Merchant Node & Realtime Settlement
- **Store MCP Adapter:** Memvalidasi stok lokal dan mengunci order intent.
- **LuxWA Node (:3085):** Mengirimkan rincian pesanan dan instruksi pembayaran QRIS langsung ke WhatsApp kasir toko secara realtime.

## 📝 Catatan Audit
- Validasi delivery Archify passed: 9/9 automated composition checks.
