"""
Generator HTML/CSS v5: Motion Graphics Dinamis Tingkat Tinggi
Resep yang ditambahkan:
1. Dynamic Camera Breathing / Micro-Zoom halus antar transisi.
2. Animated Live SVG Character (Blinking eyes, mouth shapes, bobbing, phone energy ring).
3. Laser Beam Pulse & Particle Flow pada pipa MCP (Scene 4).
4. Slam-In Stamp Effect dengan haptic visual bounce (Scene 5 - Potongan Komisi 0%).
5. Cyber Glitch Alert & Scanlines pada Browser Crash (Scene 3).
6. Floating App Icons dengan depth & parallax effect (Scene 1).
"""
import math

def get_character_svg(t_sec, state="talking"):
    # Breathing and head bobbing
    head_y = math.sin(t_sec * 6.5) * 5.0
    arm_angle = math.sin(t_sec * 8.0) * 8.0
    mouth_open = 8 + math.sin(t_sec * 15.0) * 7 if state == "talking" else 3
    
    # Blinking logic: eyes blink closed for 0.15s every 3.2s
    is_blink = (t_sec % 3.2) < 0.15
    eye_h = 1 if is_blink else 6
    eye_rx = 5 if not is_blink else 5
    eye_ry = eye_h

    # Energy pulse rings from smartphone
    pulse1 = (t_sec * 35) % 40
    pulse2 = ((t_sec * 35) + 20) % 40

    return f"""
    <div style="display: flex; align-items: center; justify-content: center; margin-bottom: 20px;">
      <svg width="290" height="290" viewBox="0 0 290 290" fill="none" xmlns="http://www.w3.org/2000/svg">
        <!-- Soft Glow behind character -->
        <circle cx="145" cy="145" r="95" fill="rgba(255,107,0,0.06)" />

        <!-- Body / Shoulders with subtle sway -->
        <path d="M65 255 C65 200, 105 180, 145 180 C185 180, 225 200, 225 255" stroke="#ffffff" stroke-width="5" stroke-linecap="round" fill="#181a24" />
        <path d="M130 180 L130 215 M160 180 L160 215" stroke="#ffffff" stroke-width="4" />
        
        <!-- Head (Bobbing & Expressive) -->
        <g transform="translate(0, {head_y})">
          <!-- Head Base -->
          <circle cx="145" cy="115" r="56" fill="#14161f" stroke="#ffffff" stroke-width="5" />
          <!-- Animated Hair Tuft -->
          <path d="M98 105 Q125 55 160 68 Q185 75 196 95" stroke="#ff6b00" stroke-width="6" stroke-linecap="round" fill="none" />
          
          <!-- Eyes with Real-time Blinking -->
          <ellipse cx="125" cy="115" rx="{eye_rx}" ry="{eye_ry}" fill="#ffffff" />
          <ellipse cx="165" cy="115" rx="{eye_rx}" ry="{eye_ry}" fill="#ffffff" />
          
          <!-- Mouth Talking Animation -->
          <ellipse cx="145" cy="143" rx="10" ry="{mouth_open}" fill="#ff453a" stroke="#ffffff" stroke-width="2" />
        </g>
        
        <!-- Dynamic Arm Holding Smartphone -->
        <g transform="rotate({arm_angle} 195 220)">
          <path d="M195 210 Q220 195 235 165" stroke="#ffffff" stroke-width="6" stroke-linecap="round" fill="none" />
          <!-- Phone Body -->
          <rect x="225" y="120" width="46" height="84" rx="10" fill="#0c0d12" stroke="#0088ff" stroke-width="4" />
          <rect x="231" y="130" width="34" height="64" rx="5" fill="#0088ff" opacity="0.35" />
          
          <!-- Energy Shockwave Rings from Phone -->
          <circle cx="248" cy="115" r="{pulse1}" stroke="#ff6b00" stroke-width="3" fill="none" opacity="{max(0, 1 - pulse1/40)}" />
          <circle cx="248" cy="115" r="{pulse2}" stroke="#0088ff" stroke-width="3" fill="none" opacity="{max(0, 1 - pulse2/40)}" />
        </g>
      </svg>
    </div>
    """

def get_html_for_time(t_sec):
    # Scene 1: 0.00s - 6.35s (Pola Belanja: Floating App Icons & Frustrasi Konsumen)
    if t_sec < 6.35:
        p1, p2, p3 = "active", "", ""
        badge = "POLA KONSUMEN"
        tag = "PERUBAHAN 2026"
        headline = 'Pernah sadar gak?<br><span class="highlight-orange">Orang makin malas buka aplikasi!</span>'
        character = get_character_svg(t_sec, state="talking")

        # Floating icons animation
        float1 = math.sin(t_sec * 4.0) * 8
        float2 = math.cos(t_sec * 3.5) * 8
        float3 = math.sin(t_sec * 5.0) * 7

        content = f"""
        {character}
        <!-- Floating App Icons Chaos -->
        <div style="display: flex; justify-content: center; gap: 20px; margin-bottom: 24px;">
          <div style="background: #181a24; border: 2px solid #ff453a; padding: 14px 22px; border-radius: 16px; transform: translateY({float1}px); font-size: 24px; font-weight: 700; color: #ff453a; display: flex; align-items: center; gap: 8px;">
            <span>❌</span> App Toko A (450MB)
          </div>
          <div style="background: #181a24; border: 2px solid #ff453a; padding: 14px 22px; border-radius: 16px; transform: translateY({float2}px); font-size: 24px; font-weight: 700; color: #ff453a; display: flex; align-items: center; gap: 8px;">
            <span>❌</span> App Resto B (380MB)
          </div>
          <div style="background: #181a24; border: 2px solid #ff453a; padding: 14px 22px; border-radius: 16px; transform: translateY({float3}px); font-size: 24px; font-weight: 700; color: #ff453a; display: flex; align-items: center; gap: 8px;">
            <span>❌</span> App C (290MB)
          </div>
        </div>

        <div class="card pop-in" style="border-color: #ff6b00; box-shadow: 0 10px 30px rgba(255,107,0,0.15);">
          <div class="card-label"><span style="color: #ff6b00;">●</span> FENOMENA BARU</div>
          <div class="card-value" style="font-size: 36px; line-height: 1.4;">
            Memori HP penuh, login ribet, dan promo spam bikin orang meninggalkan aplikasi toko jadul.
          </div>
        </div>
        """

    # Scene 2: 6.35s - 13.90s (Voice Order ke AI dengan Live Soundwave & Glow)
    elif t_sec < 13.90:
        p1, p2, p3 = "active", "", ""
        badge = "POLA KONSUMEN"
        tag = "VOICE SHOPPING"
        headline = 'Tinggal bilang ke Asisten AI:<br><span class="highlight-blue">"Pesanin kopi susu 2 cup!"</span>'
        character = get_character_svg(t_sec, state="talking")

        # Live Dynamic Equalizer wave with particle bounce
        wave_bars = ""
        for i in range(18):
            h = int(14 + 65 * abs(math.sin(t_sec * 7.5 + i * 0.4)) * math.cos(t_sec * 3.0 + i * 0.15))
            color = "#0088ff" if i % 2 == 0 else "#25d366"
            wave_bars += f'<div style="width: 8px; height: {h}px; background: {color}; border-radius: 4px; box-shadow: 0 0 12px {color};"></div>'

        content = f"""
        {character}
        <div class="card glow-active" style="border-color: #0088ff; background: #0c1424; padding: 36px;">
          <div class="card-label" style="display: flex; justify-content: space-between; align-items: center;">
            <span style="color: #0088ff; font-weight: 800;">● ASISTEN AI MEMPROSES SUARA REAL-TIME...</span>
            <span class="mono" style="color: #25d366; background: rgba(37,211,102,0.15); padding: 4px 10px; border-radius: 6px;">LISTENING 100%</span>
          </div>

          <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 18px;">
            <div style="font-size: 34px; font-weight: 800; color: #ffffff;">
              "Mencari kedai terdekat & cek stok menu..."
            </div>
            <div style="display: flex; align-items: center; gap: 7px; height: 80px;">
              {wave_bars}
            </div>
          </div>
        </div>
        """

    # Scene 3: 13.90s - 21.98s (The Obstacle: Cyber Glitch & AI Buta Web)
    elif t_sec < 21.98:
        p1, p2, p3 = "", "active", ""
        badge = "MASALAH BESAR"
        tag = "WEB TRADISIONAL"
        headline = 'Tapi masalahnya:<br><span class="highlight-red">AI ITU BUTA!</span> Gak bisa klik web ribet.'

        content = """
        <div style="display: flex; flex-direction: column; gap: 24px;">
          <!-- Glitchy Error Browser Mockup -->
          <div class="card glitch-box" style="border-color: #ff453a; background: #1a0f12; padding: 36px; box-shadow: 0 0 40px rgba(255,69,58,0.25);">
            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #3d1c22; padding-bottom: 16px; margin-bottom: 20px;">
              <div style="display: flex; gap: 8px;">
                <div style="width: 16px; height: 16px; background: #ff453a; border-radius: 50%;"></div>
                <div style="width: 16px; height: 16px; background: #ff9f0a; border-radius: 50%;"></div>
                <div style="width: 16px; height: 16px; background: #30d158; border-radius: 50%;"></div>
              </div>
              <div class="mono" style="font-size: 22px; color: #ff453a; font-weight: 700;">https://tokokopi-biasa.com [PARSING_FAILED]</div>
              <div style="background: #ff453a; color: #000; font-weight: 900; font-size: 16px; padding: 6px 14px; border-radius: 6px; letter-spacing: 1px;">CRASH</div>
            </div>

            <div style="display: flex; flex-direction: column; gap: 18px;">
              <!-- Flashing Promo Trap -->
              <div style="background: rgba(255,69,58,0.15); border: 2px dashed #ff453a; padding: 22px; border-radius: 14px; text-align: center; color: #ff453a; font-weight: 900; font-size: 28px;">
                🚨 POPUP DISKON 50% & BANNER FLOATING NONGOL!
              </div>

              <!-- Broken Form Elements -->
              <div style="display: flex; gap: 16px;">
                <div style="flex: 1; background: #14161f; border: 2px solid #362024; padding: 20px; border-radius: 12px; font-size: 20px;">
                  <span style="color: #8e8e93;">Dropdown Bertingkat:</span><br>
                  <b style="color: #ff453a;">Pilih Kelurahan / Kode Pos?</b>
                </div>
                <div style="flex: 1; background: #14161f; border: 2px solid #ff453a; padding: 20px; border-radius: 12px; font-size: 20px; color: #ff453a;">
                  <span>Captcha Robot:</span><br>
                  <b>Klik Semua Gambar Bus</b> ❌
                </div>
              </div>
            </div>
          </div>

          <div class="card" style="border-color: #ff453a; text-align: center; background: #120b0d;">
            <div style="font-size: 34px; font-weight: 900; color: #ff453a; letter-spacing: -0.5px;">
              ⛔ AI Butuh Jalur Data Mesin, Bukan Gambar Cantik!
            </div>
          </div>
        </div>
        """

    # Scene 4: 21.98s - 27.92s (Solusi Protokol MCP dengan Data Laser Pulse)
    elif t_sec < 27.92:
        p1, p2, p3 = "", "", "active"
        badge = "SOLUSI RESMI"
        tag = "STANDAR GLOBAL"
        headline = 'Di sinilah <span class="highlight-green">Protokol MCP bekerja!</span> Toko nyambung langsung ke AI.'

        # Animated beam pulse position
        beam_offset = int((t_sec * 60) % 100)

        content = f"""
        <div style="display: flex; flex-direction: column; gap: 26px;">
          <!-- Glowing Interactive Bridge Nodes -->
          <div style="display: flex; align-items: center; justify-content: space-between; gap: 16px;">
            <div class="card" style="flex: 1; border-color: #25d366; padding: 28px; text-align: center; box-shadow: 0 0 30px rgba(37,211,102,0.15);">
              <div style="font-size: 22px; color: #25d366; font-weight: 800;">🏪 TOKO ANDA</div>
              <div style="font-size: 32px; font-weight: 900; margin-top: 6px;">Katalog Menu</div>
              <div style="font-size: 20px; color: #717791; margin-top: 4px;">Harga & Stok Live</div>
            </div>

            <!-- Pulsing Energy Pipe -->
            <div style="display: flex; flex-direction: column; align-items: center; gap: 4px; position: relative;">
              <div style="font-size: 28px; color: #ff6b00; animation: pulseGlow 1s infinite;">⚡</div>
              <div style="background: linear-gradient(90deg, #ff6b00, #ff8800); color: #000; font-weight: 900; font-size: 19px; padding: 10px 18px; border-radius: 12px; white-space: nowrap; box-shadow: 0 0 25px rgba(255,107,0,0.5);">
                PROTOKOL MCP
              </div>
              <div style="font-size: 28px; color: #ff6b00; animation: pulseGlow 1s infinite;">⚡</div>
            </div>

            <div class="card" style="flex: 1; border-color: #0088ff; padding: 28px; text-align: center; box-shadow: 0 0 30px rgba(0,136,255,0.15);">
              <div style="font-size: 22px; color: #0088ff; font-weight: 800;">🧠 OTAK AI</div>
              <div style="font-size: 32px; font-weight: 900; margin-top: 6px;">Customer Agent</div>
              <div style="font-size: 20px; color: #717791; margin-top: 4px;">Langsung Eksekusi</div>
            </div>
          </div>

          <!-- Structured Benefit Cards with Pop-in -->
          <div class="card" style="border-color: #242838; padding: 32px; background: #0c0e14;">
            <div style="display: flex; flex-direction: column; gap: 18px;">
              <div style="display: flex; align-items: center; gap: 16px; font-size: 26px; font-weight: 700;">
                <div style="width: 40px; height: 40px; background: #ff6b00; border-radius: 50%; color: #000; font-weight: 900; display: flex; align-items: center; justify-content: center; font-size: 22px;">1</div>
                <div>AI membaca stok & harga toko dalam <span style="color: #ff6b00;">0.1 detik</span>.</div>
              </div>
              <div style="display: flex; align-items: center; gap: 16px; font-size: 26px; font-weight: 700;">
                <div style="width: 40px; height: 40px; background: #ff6b00; border-radius: 50%; color: #000; font-weight: 900; display: flex; align-items: center; justify-content: center; font-size: 22px;">2</div>
                <div>Mengunci pesanan otomatis tanpa takut stok bentrok.</div>
              </div>
              <div style="display: flex; align-items: center; gap: 16px; font-size: 26px; font-weight: 700; color: #25d366;">
                <div style="width: 40px; height: 40px; background: #25d366; border-radius: 50%; color: #000; font-weight: 900; display: flex; align-items: center; justify-content: center; font-size: 22px;">3</div>
                <div>Bayar instan pakai token QRIS terenkripsi aman.</div>
              </div>
            </div>
          </div>
        </div>
        """

    # Scene 5: 27.92s - 34.27s (Payoff: WA Kasir & Slam-In Stamp Potongan 0%)
    elif t_sec < 34.27:
        p1, p2, p3 = "", "", "active"
        badge = "HASIL NYATA"
        tag = "NOTIFIKASI WA KASIR"
        headline = 'Orderan loncat ke <span class="highlight-green">WhatsApp Kasir Anda!</span> Komisi Ojol: 0%!'

        content = """
        <div style="display: flex; flex-direction: column; gap: 24px;">
          <!-- WA Kasir Card -->
          <div class="card" style="border-color: #25d366; background: #0c1812; padding: 36px; box-shadow: 0 0 35px rgba(37,211,102,0.2);">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
              <div style="font-size: 26px; font-weight: 900; color: #25d366; display: flex; align-items: center; gap: 10px;">
                <span>💬</span> WHATSAPP TOKO KASIR
              </div>
              <div class="mono" style="background: #25d366; color: #000; font-weight: 900; font-size: 18px; padding: 4px 14px; border-radius: 6px;">
                AUTO-ORDER
              </div>
            </div>

            <div style="background: #12241b; border: 1.5px solid #25d366; border-radius: 16px; padding: 24px; font-size: 28px; line-height: 1.5;">
              <div style="font-weight: 900; color: #ffffff;">🔔 PESANAN MASUK DARI ASISTEN AI</div>
              <div style="color: #a3e6be; margin-top: 6px; font-size: 26px;">• 2 Cup Kopi Susu Gula Aren</div>
              <div style="font-weight: 900; color: #25d366; font-size: 36px; margin-top: 8px;">Total: Rp 36.000 (QRIS LUNAS ✓)</div>
            </div>
          </div>

          <!-- Slam-in Heavy Stamp 0% Potongan Komisi -->
          <div class="slam-in" style="background: rgba(255,69,58,0.14); border: 4px dashed #ff453a; border-radius: 24px; padding: 26px; text-align: center; box-shadow: 0 0 50px rgba(255,69,58,0.3);">
            <div style="font-size: 56px; font-weight: 950; color: #ff453a; letter-spacing: 2px;">
              POTONGAN KOMISI: 0%
            </div>
            <div style="font-size: 26px; color: #ffffff; font-weight: 800; margin-top: 6px;">
              100% uang pembayaran utuh masuk rekening pemilik toko!
            </div>
          </div>
        </div>
        """

    # Scene 6: 34.27s - 40.12s (Penutup & Call to Action DM/PC dengan Karakter Tersenyum)
    else:
        p1, p2, p3 = "", "", "active"
        badge = "KONSULTASI & PASANG"
        tag = "TERIMA BERES"
        headline = 'Mau toko Anda dipasangin terima beres?<br><span class="highlight-orange">Cukup DM / PC Sekarang!</span>'
        character = get_character_svg(t_sec, state="talking")

        content = f"""
        {character}
        <!-- Glow CTA Card -->
        <div class="card glow-active" style="background: #ff6b00; border-color: #ff6b00; text-align: center; padding: 46px; box-shadow: 0 0 60px rgba(255,107,0,0.5); transform: scale(1.02);">
          <div style="font-size: 52px; font-weight: 950; color: #000000; letter-spacing: -1px;">
            📩 CUKUP DM / PC SEKARANG
          </div>
          <div style="font-size: 32px; font-weight: 800; color: #1a1a1a; margin-top: 10px;">
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
