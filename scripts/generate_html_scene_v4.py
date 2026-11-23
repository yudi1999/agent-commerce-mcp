"""
Generator HTML/CSS Sinkron Penuh 40.11 Detik (Durasi Nyata Audio Gemini Puck Utuh).
Timeline Scene:
- Scene 1: 0.00s - 6.35s (durasi 6.35s)
- Scene 2: 6.35s - 13.90s (durasi 7.55s)
- Scene 3: 13.90s - 21.98s (durasi 8.08s)
- Scene 4: 21.98s - 27.92s (durasi 5.94s)
- Scene 5: 27.92s - 34.27s (durasi 6.35s)
- Scene 6: 34.27s - 40.12s (durasi 5.85s)
"""
import math

def get_character_svg(t_sec, state="talking"):
    head_y = math.sin(t_sec * 6.0) * 4.0
    arm_angle = math.sin(t_sec * 8.0) * 6.0
    mouth_open = 8 + math.sin(t_sec * 14.0) * 6 if state == "talking" else 3

    return f"""
    <div style="display: flex; align-items: center; justify-content: center; margin-bottom: 24px;">
      <svg width="280" height="280" viewBox="0 0 280 280" fill="none" xmlns="http://www.w3.org/2000/svg">
        <!-- Body / Shoulders -->
        <path d="M60 250 C60 200, 100 180, 140 180 C180 180, 220 200, 220 250" stroke="#ffffff" stroke-width="5" stroke-linecap="round" fill="#181a24" />
        <path d="M125 180 L125 210 M155 180 L155 210" stroke="#ffffff" stroke-width="4" />
        
        <!-- Head (Bobbing) -->
        <g transform="translate(0, {head_y})">
          <circle cx="140" cy="115" r="55" fill="#14161f" stroke="#ffffff" stroke-width="5" />
          <path d="M95 105 Q120 60 155 70 Q180 75 190 95" stroke="#ff6b00" stroke-width="6" stroke-linecap="round" fill="none" />
          <circle cx="120" cy="115" r="5" fill="#ffffff" />
          <circle cx="160" cy="115" r="5" fill="#ffffff" />
          <ellipse cx="140" cy="142" rx="9" ry="{mouth_open}" fill="#ff453a" stroke="#ffffff" stroke-width="2" />
        </g>
        
        <!-- Arm & Smartphone -->
        <g transform="rotate({arm_angle} 190 220)">
          <path d="M190 210 Q215 200 230 170" stroke="#ffffff" stroke-width="6" stroke-linecap="round" fill="none" />
          <rect x="220" y="125" width="44" height="80" rx="8" fill="#0c0d12" stroke="#0088ff" stroke-width="4" />
          <rect x="226" y="135" width="32" height="60" rx="4" fill="#0088ff" opacity="0.3" />
          <circle cx="242" cy="120" r="12" stroke="#ff6b00" stroke-width="3" fill="none" opacity="0.8" />
          <circle cx="242" cy="120" r="22" stroke="#0088ff" stroke-width="3" fill="none" opacity="0.5" />
        </g>
      </svg>
    </div>
    """

def get_html_for_time(t_sec):
    # Scene 1: 0.00s - 6.35s
    if t_sec < 6.35:
        p1, p2, p3 = "active", "", ""
        badge = "POLA KONSUMEN"
        tag = "PERUBAHAN 2026"
        headline = 'Pernah sadar gak?<br><span class="highlight-orange">Orang makin malas buka aplikasi!</span>'
        character = get_character_svg(t_sec, state="talking")
        content = f"""
        {character}
        <div class="card" style="border-color: #ff6b00;">
          <div class="card-label"><span style="color: #ff6b00;">●</span> FENOMENA BARU</div>
          <div class="card-value" style="font-size: 38px;">
            Konsumen tidak mau lagi install 10 aplikasi toko yang bikin HP penuh dan lambat.
          </div>
        </div>
        """

    # Scene 2: 6.35s - 13.90s
    elif t_sec < 13.90:
        p1, p2, p3 = "active", "", ""
        badge = "POLA KONSUMEN"
        tag = "VOICE SHOPPING"
        headline = 'Tinggal bilang ke Asisten AI:<br><span class="highlight-blue">"Pesanin kopi susu 2 cup!"</span>'
        character = get_character_svg(t_sec, state="talking")
        
        wave_bars = ""
        for i in range(14):
            h = int(15 + 50 * abs(((t_sec * 6 + i * 0.45) % 1) - 0.5) * 2)
            wave_bars += f'<div style="width: 8px; height: {h}px; background: #0088ff; border-radius: 4px;"></div>'

        content = f"""
        {character}
        <div class="card" style="border-color: #0088ff; background: #101626;">
          <div class="card-label"><span style="color: #0088ff;">●</span> ASISTEN AI MEMPROSES SUARA...</div>
          <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 10px;">
            <div style="font-size: 34px; font-weight: 700; color: #ffffff;">
              "Siap, mencari menu kopi terdekat..."
            </div>
            <div style="display: flex; align-items: center; gap: 6px; height: 70px;">
              {wave_bars}
            </div>
          </div>
        </div>
        """

    # Scene 3: 13.90s - 21.98s
    elif t_sec < 21.98:
        p1, p2, p3 = "", "active", ""
        badge = "MASALAH BESAR"
        tag = "WEB TRADISIONAL"
        headline = 'Tapi masalahnya:<br><span class="highlight-red">AI ITU BUTA!</span> Gak bisa klik web ribet.'

        content = """
        <div style="display: flex; flex-direction: column; gap: 24px;">
          <div class="card" style="border-color: #ff453a; background: #1b1216; padding: 36px;">
            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #362024; padding-bottom: 16px; margin-bottom: 20px;">
              <div style="display: flex; gap: 8px;">
                <div style="width: 16px; height: 16px; background: #ff453a; border-radius: 50%;"></div>
                <div style="width: 16px; height: 16px; background: #ff9f0a; border-radius: 50%;"></div>
                <div style="width: 16px; height: 16px; background: #30d158; border-radius: 50%;"></div>
              </div>
              <div class="mono" style="font-size: 22px; color: #8e8e93;">https://tokokopi-biasa.com</div>
              <div style="background: #ff453a; color: #000; font-weight: 800; font-size: 16px; padding: 4px 10px; border-radius: 6px;">BLOCKED</div>
            </div>

            <div style="display: flex; flex-direction: column; gap: 16px;">
              <div style="background: #2a151b; border: 2px dashed #ff453a; padding: 20px; border-radius: 14px; text-align: center; color: #ff453a; font-weight: 800; font-size: 26px;">
                ⚠️ POPUP IKAN & BANNER PROMO MEMBLOKIR AI!
              </div>
              <div style="display: flex; gap: 14px;">
                <div style="flex: 1; background: #14161f; border: 1px solid #282b38; padding: 18px; border-radius: 12px; font-size: 20px;">
                  <span style="color: #717791;">Form Manual:</span><br><b>Kecamatan / RT RW?</b>
                </div>
                <div style="flex: 1; background: #14161f; border: 1px solid #ff453a; padding: 18px; border-radius: 12px; font-size: 20px; color: #ff453a;">
                  <span>Captcha:</span><br><b>Pilih Gambar Truk</b>
                </div>
              </div>
            </div>
          </div>

          <div class="card" style="border-color: #282b38; text-align: center;">
            <div style="font-size: 32px; font-weight: 800; color: #ff453a;">
              ⛔ AI Butuh Data Mesin, Bukan Desain Web!
            </div>
          </div>
        </div>
        """

    # Scene 4: 21.98s - 27.92s
    elif t_sec < 27.92:
        p1, p2, p3 = "", "", "active"
        badge = "SOLUSI RESMI"
        tag = "STANDAR GLOBAL"
        headline = 'Di sinilah <span class="highlight-green">Protokol MCP bekerja!</span> Toko nyambung langsung ke AI.'

        content = """
        <div style="display: flex; flex-direction: column; gap: 28px;">
          <div style="display: flex; align-items: center; justify-content: space-between; gap: 16px;">
            <div class="card" style="flex: 1; border-color: #25d366; padding: 28px; text-align: center;">
              <div style="font-size: 20px; color: #25d366; font-weight: 800;">🏪 TOKO ANDA</div>
              <div style="font-size: 32px; font-weight: 800; margin-top: 6px;">Katalog Menu</div>
              <div style="font-size: 20px; color: #717791; margin-top: 4px;">Harga & Stok Live</div>
            </div>

            <div style="display: flex; flex-direction: column; align-items: center; gap: 6px;">
              <div style="color: #ff6b00; font-size: 28px; font-weight: 800;">⚡</div>
              <div style="background: #ff6b00; color: #000; font-weight: 800; font-size: 18px; padding: 8px 14px; border-radius: 10px; white-space: nowrap;">
                PROTOKOL MCP
              </div>
              <div style="color: #ff6b00; font-size: 28px; font-weight: 800;">⚡</div>
            </div>

            <div class="card" style="flex: 1; border-color: #0088ff; padding: 28px; text-align: center;">
              <div style="font-size: 20px; color: #0088ff; font-weight: 800;">🧠 OTAK AI</div>
              <div style="font-size: 32px; font-weight: 800; margin-top: 6px;">Customer Agent</div>
              <div style="font-size: 20px; color: #717791; margin-top: 4px;">Langsung Eksekusi</div>
            </div>
          </div>

          <div class="card" style="border-color: #242838; padding: 32px;">
            <div style="display: flex; flex-direction: column; gap: 16px;">
              <div style="display: flex; align-items: center; gap: 16px; font-size: 26px; font-weight: 600;">
                <div style="width: 36px; height: 36px; background: #ff6b00; border-radius: 50%; color: #000; font-weight: 800; display: flex; align-items: center; justify-content: center; font-size: 20px;">1</div>
                <div>AI membaca stok & harga toko dalam 0.1 detik.</div>
              </div>
              <div style="display: flex; align-items: center; gap: 16px; font-size: 26px; font-weight: 600;">
                <div style="width: 36px; height: 36px; background: #ff6b00; border-radius: 50%; color: #000; font-weight: 800; display: flex; align-items: center; justify-content: center; font-size: 20px;">2</div>
                <div>Mengunci pesanan otomatis tanpa bentrok.</div>
              </div>
              <div style="display: flex; align-items: center; gap: 16px; font-size: 26px; font-weight: 600; color: #25d366;">
                <div style="width: 36px; height: 36px; background: #25d366; border-radius: 50%; color: #000; font-weight: 800; display: flex; align-items: center; justify-content: center; font-size: 20px;">3</div>
                <div>Bayar instan pakai token QRIS terenkripsi.</div>
              </div>
            </div>
          </div>
        </div>
        """

    # Scene 5: 27.92s - 34.27s
    elif t_sec < 34.27:
        p1, p2, p3 = "", "", "active"
        badge = "HASIL NYATA"
        tag = "NOTIFIKASI WA KASIR"
        headline = 'Orderan loncat ke <span class="highlight-green">WhatsApp Kasir Anda!</span> Komisi Ojol: 0%!'

        content = """
        <div style="display: flex; flex-direction: column; gap: 24px;">
          <div class="card" style="border-color: #25d366; background: #0f1c16; padding: 36px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
              <div style="font-size: 26px; font-weight: 800; color: #25d366; display: flex; align-items: center; gap: 10px;">
                <span>💬</span> NOTIFIKASI WA KASIR
              </div>
              <div class="mono" style="background: #25d366; color: #000; font-weight: 800; font-size: 18px; padding: 4px 12px; border-radius: 6px;">
                AUTO-ORDER
              </div>
            </div>

            <div style="background: #142920; border: 1px solid #25d366; border-radius: 16px; padding: 24px; font-size: 28px; line-height: 1.5;">
              <div style="font-weight: 800; color: #ffffff;">🔔 PESANAN MASUK DARI ASISTEN AI</div>
              <div style="color: #a3e6be; margin-top: 6px;">• 2 Cup Kopi Susu Gula Aren</div>
              <div style="font-weight: 800; color: #25d366; font-size: 34px; margin-top: 8px;">Total: Rp 36.000 (QRIS LUNAS ✓)</div>
            </div>
          </div>

          <div style="background: rgba(255,69,58,0.12); border: 3px dashed #ff453a; border-radius: 20px; padding: 26px; text-align: center;">
            <div style="font-size: 52px; font-weight: 900; color: #ff453a; letter-spacing: 1px;">
              POTONGAN KOMISI: 0%
            </div>
            <div style="font-size: 26px; color: #ffffff; font-weight: 700; margin-top: 6px;">
              100% uang pembayaran utuh milik pemilik toko!
            </div>
          </div>
        </div>
        """

    # Scene 6: 34.27s - 40.12s
    else:
        p1, p2, p3 = "", "", "active"
        badge = "KONSULTASI & PASANG"
        tag = "TERIMA BERES"
        headline = 'Mau toko Anda dipasangin terima beres?<br><span class="highlight-orange">Cukup DM / PC Sekarang!</span>'
        character = get_character_svg(t_sec, state="talking")
        content = f"""
        {character}
        <div class="card" style="background: #ff6b00; border-color: #ff6b00; text-align: center; padding: 44px; box-shadow: 0 0 50px rgba(255,107,0,0.4);">
          <div style="font-size: 50px; font-weight: 900; color: #000000; letter-spacing: -1px;">
            📩 CUKUP DM / PC SEKARANG
          </div>
          <div style="font-size: 30px; font-weight: 800; color: #1a1a1a; margin-top: 10px;">
            Jasa Instalasi Terima Beres • Konsultasi Gratis
          </div>
        </div>
        """

    full_page = f"""
    <div class="header-tier">
      <div class="header-tag">
        <span class="badge">● {badge}</span>
        <span class="tag-meta">{tag}</span>
      </div>
      <div class="headline">{headline}</div>
    </div>

    <div class="canvas">
      {content}
    </div>

    <div>
      <div class="footer-nav">
        <div class="nav-pill {p1}">01 KEBIASAAN</div>
        <div class="nav-pill {p2}">02 MASALAH AI</div>
        <div class="nav-pill {p3}">03 PROTOKOL MCP</div>
      </div>
      <div class="channel-footer">@Bener-Gak • Edukasi Teknologi</div>
    </div>
    """
    return full_page
