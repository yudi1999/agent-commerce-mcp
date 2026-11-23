"""
Render 9:16 Authentic UI Motion Video (1080x1920 @ 30 FPS).
Screen Studio Pan/Zoom Camera, Zero-Slop Professional Aesthetics, Tactile SFX.
Offloaded to GitHub Actions runner for zero VPS load.
"""
import os
import math
import subprocess
from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1920
FPS = 30
DURATION_SEC = 24
TOTAL_FRAMES = FPS * DURATION_SEC

# Anti-slop neutral palette: Obsidian Dark UI & Crisp WhatsApp Green / QRIS Accents
BG_DARK = (15, 17, 21)         # Neutral Slate Dark
CARD_BG = (24, 27, 34)         # Elevated Surface
TEXT_PRIMARY = (240, 243, 246)
TEXT_MUTED = (139, 148, 158)
BORDER_COLOR = (48, 54, 61)
ACCENT_GREEN = (37, 211, 102)  # WhatsApp authentic brand green
ACCENT_BLUE = (31, 111, 235)   # Agent brand blue
ACCENT_RED = (248, 81, 73)     # QRIS logo red
CARD_LIGHT = (255, 255, 255)

def get_font(size, bold=False):
    # Try standard system truetype fonts
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
    ]
    for c in candidates:
        if os.path.exists(c):
            try:
                return ImageFont.truetype(c, size)
            except Exception:
                pass
    return ImageFont.load_default()

font_title = get_font(52, bold=True)
font_subtitle = get_font(32, bold=False)
font_body = get_font(28, bold=False)
font_badge = get_font(24, bold=True)
font_small = get_font(22, bold=False)
font_mono = get_font(26, bold=True)

def ease_in_out(t):
    t = max(0.0, min(1.0, t))
    return t * t * (3.0 - 2.0 * t)

def draw_rounded_rect(draw, bbox, radius, fill, outline=None, width=1):
    draw.rounded_rectangle(bbox, radius=radius, fill=fill, outline=outline, width=width)

def render_frame(frame_idx):
    t_sec = frame_idx / FPS
    
    # Base canvas (Obsidian Slate Studio background)
    img = Image.new("RGB", (W, H), BG_DARK)
    draw = ImageDraw.Draw(img)

    # 1. Permanent Professional Header (Anti-Slop Brand Header)
    draw_rounded_rect(draw, (80, 80, W - 80, 180), radius=16, fill=CARD_BG, outline=BORDER_COLOR, width=1)
    draw.text((120, 105), "JARVIS AGENT-TO-BUSINESS BRIDGE", font=font_badge, fill=TEXT_MUTED)
    draw.text((120, 132), "E-Commerce Otomatis Tanpa Potongan 20%", font=font_subtitle, fill=TEXT_PRIMARY)
    
    # Status indicator: MCP Live
    draw.ellipse((W - 140, 122, W - 120, 142), fill=ACCENT_GREEN)

    # ================= SCENE SEQUENCING =================
    # Scene 1: 0.0s - 7.0s -> Customer Chat UI (User order kopi via AI)
    # Scene 2: 7.0s - 13.0s -> Merchant MCP Protocol / QRIS Instant Payment
    # Scene 3: 13.0s - 19.0s -> WhatsApp Toko Notification (Kasir terima pesanan)
    # Scene 4: 19.0s - 24.0s -> Outro Summary (Benefit UMKM & Call-to-Action)

    # Target Camera Keyframes (Dynamic Screen Studio Pan & Zoom)
    # (timestamp, zoom, center_x, center_y)
    cam_zoom = 1.0
    cam_x = W / 2
    cam_y = H / 2

    if t_sec < 7.0:
        # Camera zooms slightly into the chat interface
        p = ease_in_out(t_sec / 2.0)
        cam_zoom = 1.0 + 0.18 * p
        cam_x = W / 2
        cam_y = 650

        # Draw Phone Chassis / Chat Interface
        phone_box = (100, 240, W - 100, 1600)
        draw_rounded_rect(draw, phone_box, radius=24, fill=CARD_BG, outline=BORDER_COLOR, width=2)
        
        # Phone top bar
        draw.text((140, 275), "💬 Asisten Pribadi AI (JARVIS)", font=font_badge, fill=ACCENT_BLUE)
        draw.line((100, 325, W - 100, 325), fill=BORDER_COLOR, width=1)
        
        # User Bubble (Right)
        if t_sec >= 0.8:
            user_b = (W - 560, 360, W - 140, 480)
            draw_rounded_rect(draw, user_b, radius=18, fill=ACCENT_BLUE)
            draw.text((W - 530, 385), "Pesan Kopi Susu Aren 2 cup", font=font_body, fill=CARD_LIGHT)
            draw.text((W - 530, 425), "kirim ke Jl. Kemenangan No. 99", font=font_small, fill=(210, 230, 255))

        # AI Agent Action (Left)
        if t_sec >= 2.4:
            agent_b = (140, 520, W - 240, 680)
            draw_rounded_rect(draw, agent_b, radius=18, fill=(30, 35, 45), outline=(55, 65, 80), width=1)
            draw.text((170, 545), "⚡ Menghubungi Toko Kopi via Protokol MCP...", font=font_small, fill=ACCENT_GREEN)
            draw.text((170, 580), "• Toko Ditemukan: Kedai Kopi Lokal", font=font_body, fill=TEXT_PRIMARY)
            draw.text((170, 620), "• Stok Tersedia: 50 | Total: Rp 36.000", font=font_body, fill=TEXT_PRIMARY)

        # AI Confirmation
        if t_sec >= 4.5:
            conf_b = (140, 710, W - 200, 890)
            draw_rounded_rect(draw, conf_b, radius=18, fill=(30, 35, 45), outline=ACCENT_GREEN, width=1)
            draw.text((170, 735), "✓ Pesanan Terkunci! Menyiapkan QRIS...", font=font_badge, fill=ACCENT_GREEN)
            draw.text((170, 780), "Total: Rp 36.000 (Bebas Biaya Layanan)", font=font_body, fill=TEXT_PRIMARY)
            draw.text((170, 825), "Meneruskan data ke WhatsApp Kasir Toko...", font=font_small, fill=TEXT_MUTED)

    elif t_sec < 13.0:
        # Scene 2: Merchant MCP Tool Call & QRIS
        p = ease_in_out((t_sec - 7.0) / 1.5)
        cam_zoom = 1.05 + 0.15 * p
        cam_x = W / 2
        cam_y = 800

        # Card: MCP Engine Inspect
        box_mcp = (100, 260, W - 100, 720)
        draw_rounded_rect(draw, box_mcp, radius=20, fill=(20, 23, 29), outline=ACCENT_BLUE, width=2)
        draw.text((140, 295), "PROTOKOL MCP ENGINE (MERCHANT API)", font=font_badge, fill=ACCENT_BLUE)
        
        # Tool call representation (Clean monospace)
        draw.text((140, 350), "Tool: buat_pesanan()", font=font_mono, fill=TEXT_PRIMARY)
        draw.text((140, 395), "• Produk  : Kopi Susu Gula Aren", font=font_body, fill=TEXT_MUTED)
        draw.text((140, 435), "• Qty     : 2 cup (Rp 18.000 / cup)", font=font_body, fill=TEXT_MUTED)
        draw.text((140, 475), "• Total   : Rp 36.000", font=font_body, fill=TEXT_PRIMARY)
        draw.text((140, 515), "• Lokasi  : Karawang, Jawa Barat", font=font_body, fill=TEXT_MUTED)
        draw.text((140, 560), "Status: ORDER_LOCKED [TTL: 10m]", font=font_mono, fill=ACCENT_GREEN)

        # Card: QRIS Instant Pay
        if t_sec >= 9.5:
            box_qris = (100, 760, W - 100, 1500)
            draw_rounded_rect(draw, box_qris, radius=20, fill=CARD_BG, outline=BORDER_COLOR, width=1)
            draw.text((140, 800), "PEMBAYARAN QRIS NASIONAL", font=font_badge, fill=ACCENT_RED)
            draw.text((140, 840), "Dana 100% Langsung Masuk Rekening UMKM", font=font_small, fill=TEXT_MUTED)
            
            # QR Code Box simulation
            qr_box = (W // 2 - 160, 910, W // 2 + 160, 1230)
            draw_rounded_rect(draw, qr_box, radius=16, fill=CARD_LIGHT)
            # Simulated QR pattern
            draw.rectangle((W // 2 - 130, 940, W // 2 - 50, 1020), fill=BG_DARK)
            draw.rectangle((W // 2 + 50, 940, W // 2 + 130, 1020), fill=BG_DARK)
            draw.rectangle((W // 2 - 130, 1120, W // 2 - 50, 1200), fill=BG_DARK)
            draw.rectangle((W // 2 - 20, 1040, W // 2 + 30, 1090), fill=BG_DARK)
            draw.rectangle((W // 2 + 60, 1130, W // 2 + 110, 1180), fill=BG_DARK)

            if t_sec >= 11.0:
                # Stamp Paid
                paid_box = (W // 2 - 220, 1300, W // 2 + 220, 1420)
                draw_rounded_rect(draw, paid_box, radius=18, fill=(15, 60, 30), outline=ACCENT_GREEN, width=2)
                draw.text((W // 2 - 160, 1340), "✓ PEMBAYARAN LUNAS", font=font_badge, fill=ACCENT_GREEN)

    elif t_sec < 19.0:
        # Scene 3: Kasir UMKM Phone - WhatsApp Notification
        p = ease_in_out((t_sec - 13.0) / 1.5)
        cam_zoom = 1.02 + 0.16 * p
        cam_x = W / 2
        cam_y = 750

        # WhatsApp UI container
        wa_box = (100, 250, W - 100, 1550)
        draw_rounded_rect(draw, wa_box, radius=24, fill=(18, 22, 28), outline=ACCENT_GREEN, width=2)
        
        # WhatsApp Top Bar
        draw_rounded_rect(draw, (100, 250, W - 100, 350), radius=24, fill=(7, 94, 84))
        draw.text((140, 280), "📱 WhatsApp Kasir Toko", font=font_subtitle, fill=CARD_LIGHT)
        draw.text((140, 318), "Online • Notifikasi Otomatis", font=font_small, fill=(200, 240, 230))

        # WA Notification Bubble (Green border, rich card)
        if t_sec >= 14.0:
            bubble = (130, 380, W - 130, 1080)
            draw_rounded_rect(draw, bubble, radius=18, fill=(32, 44, 51), outline=(45, 60, 70), width=1)
            
            draw.text((160, 410), "🔔 *PESANAN BARU DARI ASISTEN AI*", font=font_badge, fill=ACCENT_GREEN)
            draw.line((160, 455, W - 160, 455), fill=(50, 65, 75), width=1)
            
            draw.text((160, 480), "📋 No. Pesanan : #ORD-1001", font=font_body, fill=TEXT_PRIMARY)
            draw.text((160, 530), "👤 Pemesan     : Tuan Yudi (via AI)", font=font_body, fill=TEXT_PRIMARY)
            draw.text((160, 580), "📍 Alamat      : Jl. Kemenangan No. 99", font=font_body, fill=TEXT_PRIMARY)
            draw.text((160, 630), "☕ Produk      : Kopi Susu Gula Aren (2 cup)", font=font_body, fill=TEXT_PRIMARY)
            draw.text((160, 680), "💰 Total       : Rp 36.000", font=font_subtitle, fill=ACCENT_GREEN)
            draw.text((160, 735), "💳 Status      : LUNAS VIA QRIS", font=font_badge, fill=ACCENT_GREEN)
            
            draw.line((160, 790, W - 160, 790), fill=(50, 65, 75), width=1)
            draw.text((160, 815), "👉 Tindakan Kasir:", font=font_badge, fill=TEXT_PRIMARY)
            draw.text((160, 855), "Toko tinggal racik kopi & siapkan kurir.", font=font_body, fill=TEXT_MUTED)
            draw.text((160, 895), "Tidak perlu input manual atau hitung uang.", font=font_small, fill=TEXT_MUTED)

        # Callout card
        if t_sec >= 16.5:
            bot_box = (130, 1120, W - 130, 1420)
            draw_rounded_rect(draw, bot_box, radius=18, fill=(24, 27, 34), outline=BORDER_COLOR, width=1)
            draw.text((160, 1150), "KEUNGGULAN BUAT PEMILIK UMKM:", font=font_badge, fill=TEXT_PRIMARY)
            draw.text((160, 1205), "✓ Pemilik toko tidak perlu paham AI / coding", font=font_body, fill=TEXT_PRIMARY)
            draw.text((160, 1255), "✓ Cukup pegang HP WhatsApp kasir seperti biasa", font=font_body, fill=TEXT_PRIMARY)
            draw.text((160, 1305), "✓ 0% Potongan Komisi Ojol", font=font_body, fill=ACCENT_GREEN)

    else:
        # Scene 4: Outro CTA (Materi Kampanye & Jasa Pasang Terima Beres)
        cam_zoom = 1.0
        cam_x = W / 2
        cam_y = H / 2

        outro_box = (90, 260, W - 90, 1650)
        draw_rounded_rect(draw, outro_box, radius=24, fill=CARD_BG, outline=BORDER_COLOR, width=2)
        
        draw.text((140, 320), "SOLUSI TOKO PINTAR AI (UMKM)", font=font_title, fill=TEXT_PRIMARY)
        draw.text((140, 395), "Bawa Bisnis Anda Masuk ke Ekosistem AI Masa Depan", font=font_subtitle, fill=ACCENT_BLUE)
        
        draw.line((140, 460, W - 140, 460), fill=BORDER_COLOR, width=1)

        # 3 Value Pillars
        pillars = [
            ("1. Jasa Pasang Terima Beres", "Kami yang daftarkan menu dan hubungkan ke WhatsApp toko."),
            ("2. Transaksi Langsung & QRIS", "Uang 100% milik pemilik warung, tanpa potongan 20%."),
            ("3. Siap Dipanggil Asisten AI", "Pelanggan cukup pesan via AI di HP mereka kapan saja.")
        ]
        
        curr_y = 510
        for title, desc in pillars:
            draw_rounded_rect(draw, (140, curr_y, W - 140, curr_y + 160), radius=16, fill=(18, 21, 26), outline=BORDER_COLOR, width=1)
            draw.text((170, curr_y + 30), title, font=font_badge, fill=TEXT_PRIMARY)
            draw.text((170, curr_y + 80), desc, font=font_body, fill=TEXT_MUTED)
            curr_y += 190

        # CTA Banner
        cta_box = (140, 1280, W - 140, 1540)
        draw_rounded_rect(draw, cta_box, radius=20, fill=(15, 45, 25), outline=ACCENT_GREEN, width=2)
        draw.text((W // 2 - 320, 1340), "KONSULTASI & PASANG SEKARANG", font=font_subtitle, fill=ACCENT_GREEN)
        draw.text((W // 2 - 280, 1400), "Dibuat & Didukung oleh Tim Luxcyber", font=font_body, fill=CARD_LIGHT)
        draw.text((W // 2 - 230, 1450), "WhatsApp: 0896-2382-9690", font=font_badge, fill=TEXT_PRIMARY)

    # 2. Virtual Camera Dynamic Crop & Resize (Screen Studio Pan & Zoom)
    if cam_zoom > 1.005:
        crop_w = int(W / cam_zoom)
        crop_h = int(H / cam_zoom)
        crop_x = max(0, min(W - crop_w, int(cam_x - crop_w / 2)))
        crop_y = max(0, min(H - crop_h, int(cam_y - crop_h / 2)))
        cropped = img.crop((crop_x, crop_y, crop_x + crop_w, crop_y + crop_h))
        return cropped.resize((W, H), Image.Resampling.BILINEAR)

    return img

def main():
    frames_dir = "scripts/frames"
    os.makedirs(frames_dir, exist_ok=True)
    os.makedirs("scripts/output", exist_ok=True)

    print(f"Generating {TOTAL_FRAMES} frames ({DURATION_SEC}s @ {FPS} FPS)...")
    for f in range(TOTAL_FRAMES):
        frame_img = render_frame(f)
        frame_path = os.path.join(frames_dir, f"frame_{f:05d}.png")
        frame_img.save(frame_path, "PNG")
        if f % 120 == 0:
            print(f"Rendered {f}/{TOTAL_FRAMES} frames ({(f/TOTAL_FRAMES)*100:.1f}%)")

    print("All frames rendered. Compiling video with FFmpeg...")

    # Audio synthesis
    import generate_sfx
    generate_sfx.generate_sfx("scripts/audio")

    # Combine video & audio via FFmpeg
    # SFX cue timing:
    # 0.8s: tap
    # 2.4s: tap
    # 4.5s: tap
    # 7.0s: tap
    # 11.0s: success
    # 14.0s: ding (WA arrival)
    # 16.5s: tap
    
    cmd = [
        "ffmpeg", "-y",
        "-r", str(FPS),
        "-i", "scripts/frames/frame_%05d.png",
        "-i", "scripts/audio/tap.wav",
        "-i", "scripts/audio/ding.wav",
        "-i", "scripts/audio/success.wav",
        "-filter_complex",
        "[1:a]adelay=800|800[a1];"
        "[1:a]adelay=2400|2400[a2];"
        "[1:a]adelay=4500|4500[a3];"
        "[1:a]adelay=7000|7000[a4];"
        "[3:a]adelay=11000|11000[a5];"
        "[2:a]adelay=14000|14000[a6];"
        "[1:a]adelay=16500|16500[a7];"
        "[a1][a2][a3][a4][a5][a6][a7]amix=inputs=7:normalize=0[aout]",
        "-c:v", "libx264",
        "-preset", "medium",
        "-crf", "18",
        "-pix_fmt", "yuv420p",
        "-map", "0:v",
        "-map", "[aout]",
        "-shortest",
        "scripts/output/agent-commerce-mcp-demo.mp4"
    ]
    
    subprocess.run(cmd, check=True)
    print("Video production completed: scripts/output/agent-commerce-mcp-demo.mp4")

if __name__ == "__main__":
    main()
