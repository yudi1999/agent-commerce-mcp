"""
Motion Masterpiece: Edukasi Protokol MCP untuk Toko/UMKM
Standar: motion-design-mastery (iart-ai/motion-skills standards)
Kaidah:
1. One Focal Point per Scene (Zero Overcrowding).
2. Asymmetric snappy easing (ease-out cubic bezier).
3. 3-Layer Motion (Primary Hero, Secondary Support, Ambient Grid).
4. Kinetic Big Typography (Hormozi / Apple Style, 1-3 kata punchy).
5. Offloaded ke GitHub Actions Runner.
"""
import os
import math
import subprocess
from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1920
FPS = 30
DURATION_SEC = 24
TOTAL_FRAMES = FPS * DURATION_SEC

# Obsidian Apple/Stripe-grade Dark Palette
BG_COLOR = (11, 13, 17)        # Pure Slate Night (#0b0d11)
CARD_BG = (20, 24, 33)         # Clean Elevated Card (#141821)
CARD_BORDER = (38, 44, 58)     # Precise border (#262c3a)
TEXT_HERO = (255, 255, 255)
TEXT_MUTED = (145, 155, 175)
ACCENT_GREEN = (37, 211, 102)  # WhatsApp/Success Green
ACCENT_BLUE = (64, 150, 255)   # Tech Blue
ACCENT_ORANGE = (255, 120, 50) # Problem/Warning Orange

def get_font(size, bold=False):
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

font_giant = get_font(76, bold=True)
font_hero = get_font(58, bold=True)
font_title = get_font(44, bold=True)
font_body = get_font(32, bold=False)
font_label = get_font(24, bold=True)
font_sub = get_font(26, bold=False)

def ease_out_cubic(t):
    t = max(0.0, min(1.0, t))
    return 1.0 - math.pow(1.0 - t, 3)

def ease_in_out(t):
    t = max(0.0, min(1.0, t))
    return t * t * (3.0 - 2.0 * t)

def spring_pop(t, damping=12.0, freq=18.0):
    t = max(0.0, t)
    return 1.0 - math.exp(-damping * t) * math.cos(freq * t)

# 4 Babak Bersih (One Focal Point Per Shot):
# Shot 1: 0.0s - 5.5s  -> THE SHIFT (Cara Belanja Berubah: Website Ditinggalkan)
# Shot 2: 5.5s - 11.0s -> THE PROBLEM (AI 'Buta' Lihat Web Gambar & Tombol)
# Shot 3: 11.0s - 17.5s -> THE HERO: MCP (Colokan Langsung Toko ke Otak AI)
# Shot 4: 17.5s - 24.0s -> THE PAYOFF & CTA (WhatsApp Kasir Ting! Jasa Pasang Terima Beres)

def render_frame(frame_idx):
    t = frame_idx / FPS
    img = Image.new("RGB", (W, H), BG_COLOR)
    draw = ImageDraw.Draw(img)

    # Ambient Layer: Subtle Grid Pattern (Zero Noise)
    grid_gap = 120
    for x in range(0, W, grid_gap):
        draw.line((x, 0, x, H), fill=(16, 20, 26), width=1)
    for y in range(0, H, grid_gap):
        draw.line((0, y, W, y), fill=(16, 20, 26), width=1)

    # Permanent Minimal Top Pill
    draw.rounded_rectangle((W // 2 - 190, 80, W // 2 + 190, 140), radius=30, fill=(18, 22, 30), outline=CARD_BORDER, width=1)
    draw.ellipse((W // 2 - 165, 103, W // 2 - 151, 117), fill=ACCENT_BLUE)
    draw.text((W // 2 - 135, 96), "JARVIS COMMERCE ARCHITECTURE", font=font_label, fill=TEXT_MUTED)

    # ================= SHOT 1: THE SHIFT (0.0s - 5.5s) =================
    if t < 5.5:
        progress = ease_out_cubic(min(1.0, t / 0.8))
        alpha_y = int(340 - (1.0 - progress) * 80)
        
        # Primary Hero Text
        draw.text((100, alpha_y), "Zaman Web\nSudah Lewat.", font=font_giant, fill=TEXT_HERO)
        
        # Secondary Card: Chat prompt to AI (Follow-through at t >= 1.2s)
        if t >= 1.2:
            card_p = ease_out_cubic(min(1.0, (t - 1.2) / 0.7))
            card_y = int(720 - (1.0 - card_p) * 60)
            
            box = (90, card_y, W - 90, card_y + 440)
            draw.rounded_rectangle(box, radius=24, fill=CARD_BG, outline=CARD_BORDER, width=2)
            
            # Simulated Chat input
            draw.text((140, card_y + 50), "CUSTOMER KE ASISTEN AI:", font=font_label, fill=ACCENT_BLUE)
            draw.text((140, card_y + 110), "\"Pesan kopi susu 2 cup,\nkirim ke rumah sekarang.\"", font=font_title, fill=TEXT_HERO)
            
            # Micro badge
            draw.rounded_rectangle((140, card_y + 270, 480, card_y + 350), radius=14, fill=(28, 36, 52))
            draw.text((170, card_y + 295), "⚡ Tanpa Buka Browser", font=font_body, fill=ACCENT_BLUE)

        # Bottom Safe Caption
        if t >= 2.8:
            draw.text((W // 2 - 380, 1550), "Pelanggan kini belanja lewat AI,", font=font_body, fill=TEXT_MUTED)
            draw.text((W // 2 - 380, 1600), "bukan mengklik website lagi.", font=font_title, fill=TEXT_HERO)

    # ================= SHOT 2: THE PROBLEM (5.5s - 11.0s) =================
    elif t < 11.0:
        local_t = t - 5.5
        progress = ease_out_cubic(min(1.0, local_t / 0.8))
        y_pos = int(340 - (1.0 - progress) * 80)

        draw.text((100, y_pos), "Tapi, AI 'Buta'\nLihat Website.", font=font_giant, fill=ACCENT_ORANGE)

        if local_t >= 1.0:
            card_p = ease_out_cubic(min(1.0, (local_t - 1.0) / 0.7))
            card_y = int(700 - (1.0 - card_p) * 60)
            
            box = (90, card_y, W - 90, card_y + 480)
            draw.rounded_rectangle(box, radius=24, fill=(28, 18, 16), outline=ACCENT_ORANGE, width=2)
            
            draw.text((140, card_y + 50), "KENAPA WEBSITE GAGAL?", font=font_label, fill=ACCENT_ORANGE)
            draw.text((140, card_y + 110), "AI Tidak Bisa Klik Banner.", font=font_title, fill=TEXT_HERO)
            draw.text((140, card_y + 180), "Website penuh popup, iklan, dan tombol\nyang membingungkan asisten AI.\n\nAI butuh JALUR DATA RESMI.", font=font_body, fill=(220, 200, 200))

        if local_t >= 2.5:
            draw.text((W // 2 - 380, 1550), "Toko tanpa jalur data mesin...", font=font_body, fill=TEXT_MUTED)
            draw.text((W // 2 - 380, 1600), "Akan diabaikan oleh agen AI.", font=font_title, fill=ACCENT_ORANGE)

    # ================= SHOT 3: THE HERO - MCP (11.0s - 17.5s) =================
    elif t < 17.5:
        local_t = t - 11.0
        progress = ease_out_cubic(min(1.0, local_t / 0.8))
        y_pos = int(320 - (1.0 - progress) * 80)

        draw.text((100, y_pos), "Solusinya:\nProtokol MCP.", font=font_giant, fill=ACCENT_BLUE)

        if local_t >= 1.0:
            card_p = ease_out_cubic(min(1.0, (local_t - 1.0) / 0.7))
            card_y = int(680 - (1.0 - card_p) * 60)
            
            box = (90, card_y, W - 90, card_y + 560)
            draw.rounded_rectangle(box, radius=24, fill=CARD_BG, outline=ACCENT_BLUE, width=2)
            
            draw.text((140, card_y + 50), "MODEL CONTEXT PROTOCOL", font=font_label, fill=ACCENT_BLUE)
            draw.text((140, card_y + 105), "Colokan USB Toko Anda.", font=font_title, fill=TEXT_HERO)

            # Elegant 3-Step Flow Diagram
            items = [
                ("1. AI Baca Menu", "Harga & stok terbaca instan dan akurat."),
                ("2. AI Kunci Order", "Pesanan otomatis masuk ke antrean."),
                ("3. Lunas via QRIS", "Uang 100% milik toko, 0% komisi.")
            ]
            iy = card_y + 190
            for title, desc in items:
                draw.text((140, iy), title, font=font_title, fill=TEXT_HERO)
                draw.text((140, iy + 45), desc, font=font_sub, fill=TEXT_MUTED)
                iy += 105

        if local_t >= 3.0:
            draw.text((W // 2 - 360, 1550), "Jalur resmi antara toko Anda", font=font_body, fill=TEXT_MUTED)
            draw.text((W // 2 - 360, 1600), "dengan semua Asisten AI.", font=font_title, fill=ACCENT_BLUE)

    # ================= SHOT 4: THE RESULT & CTA (17.5s - 24.0s) =================
    else:
        local_t = t - 17.5
        progress = ease_out_cubic(min(1.0, local_t / 0.8))
        y_pos = int(300 - (1.0 - progress) * 80)

        draw.text((100, y_pos), "Pesanan Masuk\nKe WhatsApp.", font=font_giant, fill=ACCENT_GREEN)

        if local_t >= 0.8:
            card_p = ease_out_cubic(min(1.0, (local_t - 0.8) / 0.7))
            card_y = int(640 - (1.0 - card_p) * 60)
            
            # Clean WhatsApp simulated notification
            box = (90, card_y, W - 90, card_y + 360)
            draw.rounded_rectangle(box, radius=24, fill=(18, 30, 24), outline=ACCENT_GREEN, width=2)
            
            draw.text((140, card_y + 40), "📱 NOTIFIKASI KASIR TOKO (WHATSAPP)", font=font_label, fill=ACCENT_GREEN)
            draw.text((140, card_y + 90), "Pesanan Baru dari AI Customer!", font=font_title, fill=TEXT_HERO)
            draw.text((140, card_y + 155), "• Kopi Susu Gula Aren (2 cup)\n• Total: Rp 36.000 (Lunas QRIS)\n• Alamat: Jl. Kemenangan No. 99", font=font_body, fill=(210, 235, 220))
            draw.text((140, card_y + 280), "✓ Kasir tinggal racik & serahkan kurir.", font=font_label, fill=ACCENT_GREEN)

        # Clean Final Action Block
        if local_t >= 2.5:
            cta_box = (90, 1100, W - 90, 1500)
            draw.rounded_rectangle(cta_box, radius=24, fill=CARD_BG, outline=CARD_BORDER, width=2)
            
            draw.text((140, 1140), "JASA INSTALASI TERIMA BERES", font=font_label, fill=ACCENT_BLUE)
            draw.text((140, 1185), "Daftarkan Toko Anda Sekarang", font=font_title, fill=TEXT_HERO)
            draw.text((140, 1250), "Kami siapkan sistemnya sampai jalan.\nPemilik UMKM tidak perlu paham coding.", font=font_body, fill=TEXT_MUTED)

            draw.rounded_rectangle((140, 1340, W - 140, 1440), radius=16, fill=(25, 60, 35))
            draw.text((170, 1370), "WhatsApp Konsultasi: 0896-2382-9690", font=font_body, fill=TEXT_HERO)

    return img

def main():
    frames_dir = "scripts/frames_masterpiece"
    os.makedirs(frames_dir, exist_ok=True)
    os.makedirs("scripts/output", exist_ok=True)

    print(f"Rendering {TOTAL_FRAMES} high-craft frames ({DURATION_SEC}s @ {FPS} FPS)...")
    for f in range(TOTAL_FRAMES):
        frame_img = render_frame(f)
        frame_path = os.path.join(frames_dir, f"frame_{f:05d}.png")
        frame_img.save(frame_path, "PNG")
        if f % 120 == 0:
            print(f"Rendered {f}/{TOTAL_FRAMES} frames ({(f/TOTAL_FRAMES)*100:.1f}%)")

    print("Frames ready. Generating tactile audio and compiling via FFmpeg...")
    import generate_sfx
    generate_sfx.generate_sfx("scripts/audio")

    # Audio cue timing matched to 4 distinct shot entrances
    cmd = [
        "ffmpeg", "-y",
        "-r", str(FPS),
        "-i", "scripts/frames_masterpiece/frame_%05d.png",
        "-i", "scripts/audio/tap.wav",
        "-i", "scripts/audio/ding.wav",
        "-i", "scripts/audio/success.wav",
        "-filter_complex",
        "[1:a]adelay=300|300[a1];"
        "[1:a]adelay=1200|1200[a2];"
        "[1:a]adelay=5500|5500[a3];"
        "[1:a]adelay=11000|11000[a4];"
        "[2:a]adelay=17500|17500[a5];"
        "[3:a]adelay=20000|20000[a6];"
        "[a1][a2][a3][a4][a5][a6]amix=inputs=6:normalize=0[aout]",
        "-c:v", "libx264",
        "-preset", "medium",
        "-crf", "18",
        "-pix_fmt", "yuv420p",
        "-map", "0:v",
        "-map", "[aout]",
        "-shortest",
        "scripts/output/mcp-motion-masterpiece.mp4"
    ]
    subprocess.run(cmd, check=True)
    print("Masterpiece compiled successfully: scripts/output/mcp-motion-masterpiece.mp4")

if __name__ == "__main__":
    main()
