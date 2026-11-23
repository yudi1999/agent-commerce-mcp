"""
Video Edukasi MCP untuk Publik / UMKM: "Kenapa Toko Wajib Punya MCP di Era AI?"
Format 9:16 (1080x1920 @ 30 FPS, durasi 30 detik).
Standar: motion-graphics-craft & antislop-ui.
Offloaded ke GitHub Actions Runner.
"""
import os
import math
import subprocess
from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1920
FPS = 30
DURATION_SEC = 30
TOTAL_FRAMES = FPS * DURATION_SEC

# Anti-slop neutral palette: Obsidian Slate Dark UI & Crisp Accents
BG_DARK = (15, 17, 21)         # Neutral Slate Dark (#0f1115)
CARD_BG = (24, 27, 34)         # Elevated Surface (#181b22)
TEXT_PRIMARY = (240, 243, 246)
TEXT_MUTED = (139, 148, 158)
BORDER_COLOR = (48, 54, 61)
ACCENT_GREEN = (37, 211, 102)  # WhatsApp authentic green
ACCENT_BLUE = (56, 139, 253)   # Agent blue
ACCENT_YELLOW = (227, 179, 65) # Attention / Hook highlight
ACCENT_RED = (248, 81, 73)     # Problem indicator
CARD_LIGHT = (255, 255, 255)

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

font_title = get_font(50, bold=True)
font_subtitle = get_font(34, bold=False)
font_body = get_font(28, bold=False)
font_badge = get_font(24, bold=True)
font_small = get_font(22, bold=False)
font_mono = get_font(26, bold=True)

# Safe typography for karaoke captions (Center band safe zone)
font_caption_bold = get_font(52, bold=True)

def ease_in_out(t):
    t = max(0.0, min(1.0, t))
    return t * t * (3.0 - 2.0 * t)

def draw_rounded_rect(draw, bbox, radius, fill, outline=None, width=1):
    draw.rounded_rectangle(bbox, radius=radius, fill=fill, outline=outline, width=width)

# Storyboard Karaoke Script (Paced to voice narration cues)
# 0s - 7s: Hook -> Cara orang belanja berubah.
# 7s - 14s: Masalah -> Web manual & potongan komisi 20% vs AI Agent.
# 14s - 22s: Solusi -> Apa itu MCP? Colokan USB data toko ke otak AI.
# 22s - 30s: Eksekusi -> Jasa pasang terima beres untuk UMKM lokal.

CAPTIONS = [
    # (start_s, end_s, text, keyword_highlight)
    (0.5, 3.2, "Orang tidak belanja lewat browser lagi.", "tidak belanja"),
    (3.5, 6.8, "Mereka menyuruh Asisten AI di HP mereka.", "Asisten AI"),
    (7.2, 10.2, "Tapi AI tidak bisa baca website yang ribet.", "tidak bisa baca"),
    (10.5, 13.8, "AI butuh protokol resmi: namanya MCP.", "MCP"),
    (14.2, 17.5, "MCP adalah colokan langsung ke toko Anda.", "colokan langsung"),
    (17.8, 21.5, "Order AI masuk WhatsApp kasir, komisi 0%.", "komisi 0%"),
    (22.0, 25.5, "Pemilik UMKM tidak perlu paham coding.", "tidak perlu paham"),
    (26.0, 29.5, "Kami pasang terima beres. Mulai sekarang!", "terima beres"),
]

def render_frame(frame_idx):
    t_sec = frame_idx / FPS
    
    img = Image.new("RGB", (W, H), BG_DARK)
    draw = ImageDraw.Draw(img)

    # 1. Permanent Header Brand
    draw_rounded_rect(draw, (80, 80, W - 80, 180), radius=16, fill=CARD_BG, outline=BORDER_COLOR, width=1)
    draw.text((120, 105), "EDUKASI TEKNOLOGI UMKM", font=font_badge, fill=TEXT_MUTED)
    draw.text((120, 132), "Masa Depan Belanja: Protokol MCP", font=font_subtitle, fill=TEXT_PRIMARY)
    draw.ellipse((W - 140, 122, W - 120, 142), fill=ACCENT_BLUE)

    # Virtual Camera Pan & Zoom (Pattern interrupts on transitions)
    cam_zoom = 1.0
    cam_x = W / 2
    cam_y = H / 2

    # Dynamic Scene Rendering
    if t_sec < 7.0:
        # Scene 1: Hook (Perubahan Perilaku Belanja)
        # Snap zoom on frame 1 to grab retention
        p = ease_in_out(t_sec / 1.5)
        cam_zoom = 1.08 - 0.08 * p if t_sec < 1.5 else 1.0 + 0.05 * math.sin(t_sec)
        cam_y = 650

        card_box = (100, 240, W - 100, 820)
        draw_rounded_rect(draw, card_box, radius=20, fill=CARD_BG, outline=BORDER_COLOR, width=1)
        
        draw.text((140, 280), "DULU (2020 - 2024)", font=font_badge, fill=TEXT_MUTED)
        draw.text((140, 320), "Buka 5 Aplikasi Berbeda", font=font_title, fill=ACCENT_RED)
        draw.text((140, 385), "• Scroll ratusan produk membingungkan\n• Bayar biaya aplikasi & admin mahal\n• Isi form alamat berulang-ulang", font=font_body, fill=TEXT_MUTED)
        
        if t_sec >= 2.5:
            now_box = (100, 860, W - 100, 1440)
            draw_rounded_rect(draw, now_box, radius=20, fill=(20, 28, 40), outline=ACCENT_BLUE, width=2)
            draw.text((140, 900), "SEKARANG (ERA AGENTIC AI)", font=font_badge, fill=ACCENT_BLUE)
            draw.text((140, 940), "Cukup Perintah 1 Kalimat ke AI", font=font_title, fill=TEXT_PRIMARY)
            
            prompt_bubble = (140, 1020, W - 140, 1140)
            draw_rounded_rect(draw, prompt_bubble, radius=16, fill=(30, 42, 60))
            draw.text((170, 1055), "\"JARVIS, carikan kopi susu terdekat kirim ke rumah.\"", font=font_body, fill=TEXT_PRIMARY)
            
            draw.text((140, 1180), "✓ AI yang riset, AI yang checkout, AI yang urus.", font=font_body, fill=ACCENT_GREEN)
            draw.text((140, 1225), "Pelanggan tidak mau lagi buka web manual.", font=font_small, fill=TEXT_MUTED)

    elif t_sec < 14.0:
        # Scene 2: The Problem (Kenapa Web Biasa Ditinggalkan?)
        p = ease_in_out((t_sec - 7.0) / 1.5)
        cam_zoom = 1.0 + 0.10 * p
        cam_y = 750

        prob_box = (100, 240, W - 100, 800)
        draw_rounded_rect(draw, prob_box, radius=20, fill=(35, 20, 22), outline=ACCENT_RED, width=2)
        draw.text((140, 280), "MASALAH PADA WEBSITE TRADISIONAL", font=font_badge, fill=ACCENT_RED)
        draw.text((140, 320), "AI 'Buta' Melihat Banner & Tombol", font=font_title, fill=TEXT_PRIMARY)
        draw.text((140, 395), "Asisten AI di HP pelanggan tidak membaca visual cantik.\nAI membaca STRUKTUR DATA MESIN.\n\nJika toko Anda cuma punya web gambar biasa,\nAI pelanggan akan memilih toko kompetitor yang siap.", font=font_body, fill=TEXT_PRIMARY)

        if t_sec >= 10.0:
            sol_box = (100, 840, W - 100, 1420)
            draw_rounded_rect(draw, sol_box, radius=20, fill=(18, 28, 22), outline=ACCENT_GREEN, width=2)
            draw.text((140, 880), "KUNCI REVOLUSI: MCP", font=font_badge, fill=ACCENT_GREEN)
            draw.text((140, 920), "Model Context Protocol", font=font_title, fill=TEXT_PRIMARY)
            draw.text((140, 995), "Standar global dari Anthropic & komunitas AI internasional\nagar AI bisa berbicara langsung dengan database toko Anda\nsecara aman, instan, dan resmi.", font=font_body, fill=TEXT_PRIMARY)

    elif t_sec < 22.0:
        # Scene 3: Solusi Analogi Awam (Colokan USB Toko)
        p = ease_in_out((t_sec - 14.0) / 1.5)
        cam_zoom = 1.05 + 0.08 * p
        cam_y = 800

        usb_box = (100, 240, W - 100, 840)
        draw_rounded_rect(draw, usb_box, radius=20, fill=CARD_BG, outline=ACCENT_BLUE, width=2)
        draw.text((140, 280), "ANALOGI SEDERHANA: APA ITU MCP?", font=font_badge, fill=ACCENT_BLUE)
        draw.text((140, 325), "MCP = Colokan USB Toko Anda", font=font_title, fill=TEXT_PRIMARY)
        
        # Diagram representasi: [Toko UMKM] <== MCP ==> [Otak AI Pelanggan]
        draw_rounded_rect(draw, (140, 420, 400, 560), radius=14, fill=(30, 36, 45))
        draw.text((160, 470), "TOKO UMKM\n(Menu/Stok)", font=font_badge, fill=TEXT_PRIMARY)

        # Connector line
        draw.line((400, 490, W - 400, 490), fill=ACCENT_GREEN, width=4)
        draw_rounded_rect(draw, (W // 2 - 90, 460, W // 2 + 90, 520), radius=10, fill=ACCENT_GREEN)
        draw.text((W // 2 - 50, 478), "MCP", font=font_mono, fill=(10, 20, 15))

        draw_rounded_rect(draw, (W - 400, 420, W - 140, 560), radius=14, fill=(30, 36, 45))
        draw.text((W - 370, 470), "OTAK AI\n(Customer)", font=font_badge, fill=ACCENT_BLUE)

        draw.text((140, 610), "Begitu colokan MCP dipasang:\n1. AI otomatis tahu stok & menu hari ini\n2. AI memesankan produk langsung ke sistem Anda\n3. Pembayaran langsung via QRIS, 0% komisi ojol", font=font_body, fill=TEXT_PRIMARY)

        # Kasir WhatsApp Preview
        if t_sec >= 18.0:
            wa_prev = (100, 880, W - 100, 1420)
            draw_rounded_rect(draw, wa_prev, radius=20, fill=(18, 22, 28), outline=ACCENT_GREEN, width=2)
            draw.text((140, 920), "📱 Notifikasi Masuk ke WhatsApp Kasir Toko", font=font_badge, fill=ACCENT_GREEN)
            draw.text((140, 970), "Kasir tinggal terima pesan seperti biasa:\n\"Pesanan AI Baru: Kopi Susu 2 cup (LUNAS QRIS)\"", font=font_body, fill=TEXT_PRIMARY)
            draw.text((140, 1070), "Pemilik warung tidak perlu beli alat mahal tambahan.", font=font_subtitle, fill=ACCENT_YELLOW)

    else:
        # Scene 4: Penawaran & Edukasi Jasa (Call to Action)
        cam_zoom = 1.0
        cam_x = W / 2
        cam_y = H / 2

        cta_box = (90, 240, W - 90, 1460)
        draw_rounded_rect(draw, cta_box, radius=24, fill=CARD_BG, outline=BORDER_COLOR, width=2)
        
        draw.text((140, 290), "JASA INSTALASI TOKO PINTAR AI", font=font_badge, fill=ACCENT_BLUE)
        draw.text((140, 335), "Kami Pasangkan Terima Beres", font=font_title, fill=TEXT_PRIMARY)
        draw.text((140, 400), "Daftarkan bisnis Anda ke ekosistem AI sebelum kompetitor.", font=font_subtitle, fill=TEXT_MUTED)

        pillars = [
            ("1. Input & Sinkronisasi Menu", "Menu toko Anda dibuatkan protokol MCP resmi."),
            ("2. Sambungkan ke WhatsApp Kasir", "Pesanan AI langsung bunyi di HP kasir tanpa delay."),
            ("3. Uang 100% Milik Anda", "QRIS langsung ke rekening pemilik, bebas potongan 20%."),
            ("4. Pendampingan & Training", "Kami ajarkan sampai kasir dan staf paham.")
        ]
        curr_y = 480
        for p_title, p_desc in pillars:
            draw_rounded_rect(draw, (140, curr_y, W - 140, curr_y + 130), radius=14, fill=(18, 21, 26), outline=BORDER_COLOR)
            draw.text((165, curr_y + 22), p_title, font=font_badge, fill=TEXT_PRIMARY)
            draw.text((165, curr_y + 68), p_desc, font=font_body, fill=TEXT_MUTED)
            curr_y += 150

        # Action banner
        draw_rounded_rect(draw, (140, 1140, W - 140, 1380), radius=18, fill=(15, 50, 25), outline=ACCENT_GREEN, width=2)
        draw.text((W // 2 - 270, 1180), "KONSULTASI GRATIS SEKARANG", font=font_subtitle, fill=ACCENT_GREEN)
        draw.text((W // 2 - 240, 1240), "Hubungi Tim Luxcyber via WhatsApp:", font=font_body, fill=CARD_LIGHT)
        draw.text((W // 2 - 160, 1290), "0896-2382-9690", font=font_title, fill=TEXT_PRIMARY)

    # 3. Dynamic Karaoke Captions Overlay (Safe Area Band: y=1520 to y=1680)
    # Clear of bottom 280px (y > 1640 is safe margin)
    curr_caption = None
    for start_s, end_s, text, kw in CAPTIONS:
        if start_s <= t_sec <= end_s:
            curr_caption = (text, kw)
            break
            
    if curr_caption:
        text, kw = curr_caption
        # Caption box background
        cap_box = (100, 1540, W - 100, 1680)
        draw_rounded_rect(draw, cap_box, radius=18, fill=(12, 14, 18, 230), outline=(60, 70, 85), width=1)
        
        # Word highlight rendering
        words = text.split(" ")
        x_cursor = 140
        y_cursor = 1585
        
        for w in words:
            is_active = w.lower() in kw.lower()
            color = ACCENT_YELLOW if is_active else TEXT_PRIMARY
            font_use = font_caption_bold if is_active else font_body
            draw.text((x_cursor, y_cursor), w + " ", font=font_use, fill=color)
            # Estimate advance width
            x_cursor += int(len(w) * 22) + 16

    # 4. Virtual Camera Crop & Scale
    if cam_zoom > 1.005:
        crop_w = int(W / cam_zoom)
        crop_h = int(H / cam_zoom)
        crop_x = max(0, min(W - crop_w, int(cam_x - crop_w / 2)))
        crop_y = max(0, min(H - crop_h, int(cam_y - crop_h / 2)))
        cropped = img.crop((crop_x, crop_y, crop_x + crop_w, crop_y + crop_h))
        return cropped.resize((W, H), Image.Resampling.BILINEAR)

    return img

def main():
    frames_dir = "scripts/frames_edukasi"
    os.makedirs(frames_dir, exist_ok=True)
    os.makedirs("scripts/output", exist_ok=True)

    print(f"Generating {TOTAL_FRAMES} frames ({DURATION_SEC}s @ {FPS} FPS)...")
    for f in range(TOTAL_FRAMES):
        frame_img = render_frame(f)
        frame_path = os.path.join(frames_dir, f"frame_{f:05d}.png")
        frame_img.save(frame_path, "PNG")
        if f % 150 == 0:
            print(f"Rendered {f}/{TOTAL_FRAMES} frames ({(f/TOTAL_FRAMES)*100:.1f}%)")

    print("Frames ready. Generating SFX and compiling video with FFmpeg...")
    import generate_sfx
    generate_sfx.generate_sfx("scripts/audio")

    # FFmpeg command with pattern interrupts cues
    cmd = [
        "ffmpeg", "-y",
        "-r", str(FPS),
        "-i", "scripts/frames_edukasi/frame_%05d.png",
        "-i", "scripts/audio/tap.wav",
        "-i", "scripts/audio/ding.wav",
        "-i", "scripts/audio/success.wav",
        "-filter_complex",
        "[1:a]adelay=500|500[a1];"
        "[1:a]adelay=2500|2500[a2];"
        "[1:a]adelay=7200|7200[a3];"
        "[1:a]adelay=10500|10500[a4];"
        "[1:a]adelay=14200|14200[a5];"
        "[2:a]adelay=18000|18000[a6];"
        "[3:a]adelay=26000|26000[a7];"
        "[a1][a2][a3][a4][a5][a6][a7]amix=inputs=7:normalize=0[aout]",
        "-c:v", "libx264",
        "-preset", "medium",
        "-crf", "18",
        "-pix_fmt", "yuv420p",
        "-map", "0:v",
        "-map", "[aout]",
        "-shortest",
        "scripts/output/edukasi-mcp-umkm.mp4"
    ]
    subprocess.run(cmd, check=True)
    print("Video production completed: scripts/output/edukasi-mcp-umkm.mp4")

if __name__ == "__main__":
    main()
