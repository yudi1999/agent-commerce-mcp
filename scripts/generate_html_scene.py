import sys
import json

def get_html_for_time(t_sec):
    # Scene 1: Detik 0 - 6.5s (Pola Belanja Baru: Voice Order ke AI)
    if t_sec < 6.5:
        p1_active = "active"
        p2_active = ""
        p3_active = ""
        badge = "POLA KONSUMEN"
        tag_meta = "TRANSISI 2026"
        headline = 'Pernah sadar gak? Sekarang orang <span class="highlight-orange">makin malas buka aplikasi.</span>'
        
        # Audio wave bar heights calculation
        wave_bars = ""
        for i in range(16):
            h = int(20 + 60 * abs(((t_sec * 5 + i * 0.4) % 1) - 0.5) * 2)
            wave_bars += f'<div style="width: 8px; height: {h}px; background: #0088ff; border-radius: 4px;"></div>'

        content = f"""
        <div style="display: flex; flex-direction: column; gap: 32px;">
          <!-- Card User Voice Command -->
          <div class="card" style="border-color: #ff6b00;">
            <div class="card-label"><span style="color: #ff6b00;">●</span> PERINTAH SUARA KONSUMEN</div>
            <div class="card-value" style="font-size: 40px; color: #ffffff;">
              "Pesan kopi susu 2 cup, langsung kirim ke rumah ya!"
            </div>
          </div>

          <!-- Card AI Assistant Status -->
          <div class="card" style="border-color: #0088ff; background: #101524;">
            <div class="card-label"><span style="color: #0088ff;">●</span> ASISTEN AI PRIBADI DI SMARTPHONE</div>
            <div style="display: flex; align-items: center; justify-content: space-between; margin-top: 10px;">
              <div style="display: flex; align-items: center; gap: 18px;">
                <div style="width: 56px; height: 56px; background: #0088ff; border-radius: 16px; display: flex; align-items: center; justify-content: center; font-size: 28px;">🤖</div>
                <div>
                  <div style="font-size: 32px; font-weight: 700;">Asisten AI Merespons...</div>
                  <div style="font-size: 24px; color: #717791; margin-top: 4px;">Mencari kedai kopi terdekat & termurah</div>
                </div>
              </div>
              <div style="display: flex; align-items: center; gap: 8px; height: 80px;">
                {wave_bars}
              </div>
            </div>
          </div>
        </div>
        """

    # Scene 2: Detik 6.5 - 13.0s (Kebuntuan: AI Buta di Website Biasa)
    elif t_sec < 13.0:
        p1_active = ""
        p2_active = "active"
        p3_active = ""
        badge = "KEBUNTUAN SISTEM"
        tag_meta = "MASALAH WEB TRADISIONAL"
        headline = 'Tapi masalahnya: <span class="highlight-red">AI itu buta!</span> AI gak bisa klik website biasa.'

        content = """
        <div style="display: flex; flex-direction: column; gap: 32px;">
          <!-- Mockup Web Rusak / Buntu -->
          <div class="card" style="border-color: #ff453a; background: #1a1215;">
            <div style="display: flex; justify-content: space-between; align-items: center; padding-bottom: 20px; border-bottom: 1px solid #362024; margin-bottom: 24px;">
              <div style="display: flex; gap: 10px;">
                <div style="width: 16px; height: 16px; background: #ff453a; border-radius: 50%;"></div>
                <div style="width: 16px; height: 16px; background: #ff9f0a; border-radius: 50%;"></div>
                <div style="width: 16px; height: 16px; background: #30d158; border-radius: 50%;"></div>
              </div>
              <div class="mono" style="font-size: 20px; color: #8e8e93;">https://tokokopi-biasa.com</div>
              <div style="font-size: 18px; color: #ff453a; font-weight: 700;">BLOCKED</div>
            </div>

            <!-- Clutter UI Items -->
            <div style="display: flex; flex-direction: column; gap: 16px;">
              <div style="background: #2a161b; border: 1px dashed #ff453a; padding: 20px; border-radius: 16px; text-align: center; color: #ff453a; font-weight: 700; font-size: 24px;">
                ⚠️ POPUP BANNER DISKON & PROMO GAMBAR (AI GAGAL KLIK)
              </div>
              <div style="display: flex; gap: 16px;">
                <div style="flex: 1; background: #14161f; border: 1px solid #282b38; padding: 20px; border-radius: 16px;">
                  <div style="font-size: 18px; color: #717791;">Form Alamat Manual</div>
                  <div style="font-size: 24px; font-weight: 700; color: #ffffff; margin-top: 4px;">Kecamatan / RT RW?</div>
                </div>
                <div style="flex: 1; background: #14161f; border: 1px solid #ff453a; padding: 20px; border-radius: 16px;">
                  <div style="font-size: 18px; color: #ff453a;">Captcha Verifikasi</div>
                  <div style="font-size: 24px; font-weight: 700; color: #ffffff; margin-top: 4px;">Pilih Lampu Merah</div>
                </div>
              </div>
            </div>
          </div>

          <!-- Insight Box -->
          <div class="card" style="border-color: #282b38;">
            <div style="font-size: 28px; font-weight: 700; color: #ffffff; display: flex; align-items: center; gap: 14px;">
              <span style="font-size: 36px;">⛔</span>
              <div>
                <div>AI tidak membaca desain visual website.</div>
                <div style="font-size: 22px; color: #ff9f0a; font-weight: 600; margin-top: 4px;">AI butuh protokol data mesin terstandarisasi.</div>
              </div>
            </div>
          </div>
        </div>
        """

    # Scene 3: Detik 13.0 - 21.0s (Solusi: Protokol MCP Jalur Resmi)
    elif t_sec < 21.0:
        p1_active = ""
        p2_active = ""
        p3_active = "active"
        badge = "SOLUSI PROTOKOL"
        tag_meta = "STANDAR GLOBAL MCP"
        headline = 'Di sinilah <span class="highlight-green">protokol MCP bekerja.</span> Jalur resmi toko ke otak AI.'

        content = """
        <div style="display: flex; flex-direction: column; gap: 32px;">
          <!-- 2 Nodes Connected -->
          <div style="display: flex; align-items: center; justify-content: space-between; gap: 20px;">
            <!-- Node Toko -->
            <div class="card" style="flex: 1; border-color: #25d366; padding: 32px;">
              <div style="font-size: 20px; color: #25d366; font-weight: 700;">🏪 TOKO ANDA</div>
              <div style="font-size: 34px; font-weight: 800; margin-top: 8px;">Katalog Menu</div>
              <div style="font-size: 22px; color: #717791; margin-top: 6px;">Stok 50 Cup Ready</div>
              <div style="margin-top: 14px; font-size: 18px; color: #25d366; background: rgba(37,211,102,0.15); display: inline-block; padding: 4px 12px; border-radius: 6px;">
                ● Live Database
              </div>
            </div>

            <!-- Bridge Badge -->
            <div style="text-align: center; display: flex; flex-direction: column; align-items: center; gap: 8px;">
              <div style="font-size: 32px; color: #ff6b00;">➔</div>
              <div style="background: #ff6b00; color: #000; font-weight: 800; font-size: 20px; padding: 8px 16px; border-radius: 12px; white-space: nowrap;">
                MCP BRIDGE
              </div>
              <div style="font-size: 32px; color: #ff6b00;">➔</div>
            </div>

            <!-- Node AI -->
            <div class="card" style="flex: 1; border-color: #0088ff; padding: 32px;">
              <div style="font-size: 20px; color: #0088ff; font-weight: 700;">🤖 ASISTEN AI</div>
              <div style="font-size: 34px; font-weight: 800; margin-top: 8px;">Customer Bot</div>
              <div style="font-size: 22px; color: #717791; margin-top: 6px;">Baca Harga Instan</div>
              <div style="margin-top: 14px; font-size: 18px; color: #0088ff; background: rgba(0,136,255,0.15); display: inline-block; padding: 4px 12px; border-radius: 6px;">
                ● Langsung Pesan
              </div>
            </div>
          </div>

          <!-- Feature Bullets -->
          <div class="card" style="border-color: #242838;">
            <div style="display: flex; flex-direction: column; gap: 18px;">
              <div style="display: flex; align-items: center; gap: 16px;">
                <div style="width: 32px; height: 32px; background: #ff6b00; border-radius: 50%; color: #000; font-weight: 800; display: flex; align-items: center; justify-content: center; font-size: 18px;">1</div>
                <div style="font-size: 26px; font-weight: 600;">AI mengecek harga dan stok menu dalam 0.1 detik.</div>
              </div>
              <div style="display: flex; align-items: center; gap: 16px;">
                <div style="width: 32px; height: 32px; background: #ff6b00; border-radius: 50%; color: #000; font-weight: 800; display: flex; align-items: center; justify-content: center; font-size: 18px;">2</div>
                <div style="font-size: 26px; font-weight: 600;">Mengunci pesanan otomatis tanpa resiko bentrok stok.</div>
              </div>
              <div style="display: flex; align-items: center; gap: 16px;">
                <div style="width: 32px; height: 32px; background: #25d366; border-radius: 50%; color: #000; font-weight: 800; display: flex; align-items: center; justify-content: center; font-size: 18px;">3</div>
                <div style="font-size: 26px; font-weight: 600; color: #25d366;">Menghasilkan pembayaran QRIS resmi terverifikasi.</div>
              </div>
            </div>
          </div>
        </div>
        """

    # Scene 4: Detik 21.0 - 30.0s (Hasil Nyata & Call To Action)
    else:
        p1_active = ""
        p2_active = ""
        p3_active = "active"
        badge = "HASIL OPERASIONAL"
        tag_meta = "INTEGRASI UMKM"
        headline = 'Orderan masuk <span class="highlight-green">langsung ke WA Kasir.</span> Komisi Ojol 0%!'

        content = """
        <div style="display: flex; flex-direction: column; gap: 28px;">
          <!-- WA Notification Card -->
          <div class="card" style="border-color: #25d366; background: #0f1c16;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
              <div style="display: flex; align-items: center; gap: 12px; font-size: 24px; font-weight: 700; color: #25d366;">
                <span>💬</span> WHATSAPP KASIR TOKO
              </div>
              <div class="mono" style="background: #25d366; color: #000; font-weight: 700; font-size: 18px; padding: 4px 12px; border-radius: 6px;">
                ORDER BARU
              </div>
            </div>
            <div style="background: #142920; border: 1px solid #25d366; border-radius: 18px; padding: 24px; font-size: 26px; line-height: 1.5;">
              <div style="font-weight: 700; color: #ffffff;">🔔 PESANAN MASUK DARI ASISTEN AI</div>
              <div style="color: #a3e6be; margin-top: 6px;">• 2 Cup Kopi Susu Gula Aren</div>
              <div style="font-weight: 800; color: #25d366; font-size: 32px; margin-top: 8px;">Total: Rp 36.000 (QRIS LUNAS ✓)</div>
              <div style="color: #717791; font-size: 20px; margin-top: 6px;">Alamat: Jl. Kemenangan No. 99</div>
            </div>
          </div>

          <!-- Stempel 0% Potongan -->
          <div style="background: rgba(255,69,58,0.12); border: 2px dashed #ff453a; border-radius: 20px; padding: 24px; text-align: center;">
            <div style="font-size: 44px; font-weight: 800; color: #ff453a; letter-spacing: 1px;">
              POTONGAN KOMISI: 0%
            </div>
            <div style="font-size: 24px; color: #ffffff; margin-top: 4px; font-weight: 600;">
              Uang penjualan 100% utuh masuk ke rekening Anda!
            </div>
          </div>

          <!-- Call to Action Card -->
          <div class="card" style="background: #ff6b00; border-color: #ff6b00; text-align: center; padding: 36px;">
            <div style="font-size: 42px; font-weight: 800; color: #000000; letter-spacing: -0.5px;">
              📩 CUKUP DM / PC SEKARANG
            </div>
            <div style="font-size: 26px; font-weight: 700; color: #222222; margin-top: 6px;">
              Jasa Instalasi Terima Beres • Konsultasi Gratis
            </div>
          </div>
        </div>
        """

    full_page = f"""
    <div class="header-tier">
      <div class="header-tag">
        <span class="badge">● {badge}</span>
        <span class="tag-meta">{tag_meta}</span>
      </div>
      <div class="headline">{headline}</div>
    </div>

    <div class="canvas">
      {content}
    </div>

    <div>
      <div class="footer-nav">
        <div class="nav-pill {p1_active}">01 KEBIASAAN</div>
        <div class="nav-pill {p2_active}">02 MASALAH AI</div>
        <div class="nav-pill {p3_active}">03 PROTOKOL MCP</div>
      </div>
      <div class="channel-footer">@Bener-Gak • Edukasi Teknologi</div>
    </div>
    """
    return full_page

if __name__ == "__main__":
    t = float(sys.argv[1]) if len(sys.argv) > 1 else 0.0
    with open("templates/base.html", "r") as f:
        base = f.read()
    page = get_html_for_time(t)
    rendered = base.replace('<div class="container" id="app"></div>', f'<div class="container" id="app">{page}</div>')
    print(rendered)
