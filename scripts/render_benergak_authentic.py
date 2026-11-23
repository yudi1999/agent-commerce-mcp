# Part 1: Imports, Constants, Fonts
import os
import sys
import math
import subprocess
from PIL import Image, ImageDraw, ImageFont

WIDTH = 1080
HEIGHT = 1920
FPS = 30
DURATION_SEC = 30.0
TOTAL_FRAMES = int(FPS * DURATION_SEC)

# Color Palette Persis @benergak_v1
BG_DARK = (15, 17, 23)        # Very dark slate/black
TEXT_WHITE = (255, 255, 255)
TEXT_MUTED = (140, 145, 160)
ACCENT_ORANGE = (255, 107, 0) # BenerGak Signature Orange
ACCENT_BLUE = (0, 149, 255)   # AI Circuit Blue
ACCENT_GREEN = (37, 211, 102) # WhatsApp & Success Green
ACCENT_RED = (255, 69, 58)    # Warning Red
CARD_BG = (24, 28, 38)
CARD_BORDER = (45, 52, 70)

def get_font(size, bold=False):
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
    ]
    for c in candidates:
        if os.path.exists(c):
            return ImageFont.truetype(c, size)
    return ImageFont.load_default()

FONT_CATEGORY = get_font(28, bold=True)
FONT_HEADLINE = get_font(46, bold=True)
FONT_SUB = get_font(32, bold=False)
FONT_LABEL = get_font(26, bold=True)
FONT_PILL = get_font(24, bold=True)
FONT_HERO = get_font(56, bold=True)

def draw_header_and_footer(draw, t_sec, category, headline, active_pill_idx):
    # Top Header Band
    draw.rounded_rectangle([60, 80, 60 + 260, 80 + 54], radius=12, fill=CARD_BG, outline=CARD_BORDER, width=2)
    draw.text((60 + 130, 80 + 27), f"● {category}", font=FONT_CATEGORY, fill=ACCENT_ORANGE, anchor="mm")
    
    # Headline (Max 2 baris)
    draw.text((60, 165), headline, font=FONT_HEADLINE, fill=TEXT_WHITE, anchor="la")
    
    # Bottom Pills (01, 02, 03) ala BenerGak
    pills = ["01 KEBIASAAN", "02 MASALAH AI", "03 PROTOKOL MCP"]
    pill_w = 300
    pill_gap = 20
    start_x = (WIDTH - (3 * pill_w + 2 * pill_gap)) // 2
    pill_y = HEIGHT - 220
    
    for idx, name in enumerate(pills):
        px = start_x + idx * (pill_w + pill_gap)
        is_active = (idx == active_pill_idx)
        bg = ACCENT_ORANGE if is_active else CARD_BG
        txt_c = (0, 0, 0) if is_active else TEXT_MUTED
        border_c = ACCENT_ORANGE if is_active else CARD_BORDER
        draw.rounded_rectangle([px, pill_y, px + pill_w, pill_y + 56], radius=28, fill=bg, outline=border_c, width=2)
        draw.text((px + pill_w // 2, pill_y + 28), name, font=FONT_PILL, fill=txt_c, anchor="mm")
    
    # Watermark Channel Footer
    draw.text((WIDTH // 2, HEIGHT - 110), "@Bener-Gak • Edukasi Teknologi", font=FONT_LABEL, fill=TEXT_MUTED, anchor="mm")

def draw_character_and_phone(draw, cx, cy, t_sec):
    # Minimalist line-art character holding phone (ala BenerGak)
    # Head & smiling curve
    draw.ellipse([cx - 45, cy - 140, cx + 45, cy - 50], outline=TEXT_WHITE, width=4)
    draw.arc([cx - 20, cy - 100, cx + 20, cy - 70], start=20, end=160, fill=TEXT_WHITE, width=3) # Smile
    
    # Shoulders & Body
    draw.arc([cx - 100, cy - 50, cx + 100, cy + 90], start=180, end=0, fill=TEXT_WHITE, width=4)
    
    # Arm holding smartphone
    draw.line([cx + 60, cy - 10, cx + 130, cy + 30], fill=TEXT_WHITE, width=4)
    phone_x = cx + 150
    phone_y = cy - 20
    draw.rounded_rectangle([phone_x - 35, phone_y - 65, phone_x + 35, phone_y + 65], radius=10, fill=CARD_BG, outline=TEXT_WHITE, width=3)
    
    # Audio waves radiating from phone
    pulse = int(t_sec * 12) % 4
    for r in range(1, 4):
        arc_col = ACCENT_BLUE if r <= pulse else CARD_BORDER
        draw.arc([phone_x + 25 + (r*15), phone_y - (r*15), phone_x + 55 + (r*25), phone_y + (r*15)], start=-60, end=60, fill=arc_col, width=3)

def draw_dotted_flow(draw, p1, p2, t_sec, color=ACCENT_BLUE):
    # Moving dotted connection line
    x1, y1 = p1
    x2, y2 = p2
    dist = math.hypot(x2 - x1, y2 - y1)
    steps = int(dist // 22)
    offset = (t_sec * 30) % 22
    for s in range(steps):
        frac = (s * 22 + offset) / dist
        if 0.0 <= frac <= 1.0:
            px = x1 + frac * (x2 - x1)
            py = y1 + frac * (y2 - y1)
            draw.ellipse([px - 4, py - 4, px + 4, py + 4], fill=color)

def render_frame(frame_idx):
    t_sec = frame_idx / FPS
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_DARK)
    draw = ImageDraw.Draw(img)
    
    # ---------------- SCENE 1: Detik 0 - 6.5s (Kebiasaan Baru) ----------------
    if t_sec < 6.5:
        draw_header_and_footer(draw, t_sec, "POLA KONSUMEN", "Pernah sadar gak?\nSekarang orang makin malas buka aplikasi.", 0)
        
        # Karakter orang pegang HP
        draw_character_and_phone(draw, 340, 750, t_sec)
        
        # Balon Ucapan ke Asisten AI
        bubble_y = 500
        draw.rounded_rectangle([480, bubble_y, 1000, bubble_y + 160], radius=18, fill=CARD_BG, outline=ACCENT_BLUE, width=3)
        draw.text((510, bubble_y + 35), "🗣️ Voice Command:", font=FONT_LABEL, fill=ACCENT_ORANGE)
        draw.text((510, bubble_y + 80), '"Pesan kopi susu 2 cup,\nlangsung kirim ke rumah!"', font=FONT_SUB, fill=TEXT_WHITE)
        
        # Ikon Asisten AI Target
        ai_box_y = 960
        draw.rounded_rectangle([180, ai_box_y, 900, ai_box_y + 220], radius=24, fill=CARD_BG, outline=CARD_BORDER, width=2)
        draw.text((220, ai_box_y + 40), "🤖 ASISTEN AI PRIBADI (DI HP)", font=FONT_LABEL, fill=ACCENT_BLUE)
        draw.text((220, ai_box_y + 90), "Status: Menerima Perintah Suara...", font=FONT_HEADLINE, fill=TEXT_WHITE)
        draw.text((220, ai_box_y + 155), "Mencari toko kopi terdekat via internet...", font=FONT_SUB, fill=TEXT_MUTED)
        
        # Dotted flow dari HP ke AI Box
        draw_dotted_flow(draw, (490, 730), (540, ai_box_y), t_sec, ACCENT_BLUE)

    # ---------------- SCENE 2: Detik 6.5 - 13.0s (Masalah AI Buta) ----------------
    elif t_sec < 13.0:
        draw_header_and_footer(draw, t_sec, "KEBUNTUAN SISTEM", "Tapi masalahnya: AI itu buta!\nAI gak bisa belanja di web biasa.", 1)
        
        # Mockup Browser Toko Tradisional yang Error
        web_y = 440
        draw.rounded_rectangle([120, web_y, 960, web_y + 460], radius=20, fill=CARD_BG, outline=ACCENT_RED, width=3)
        
        # Browser header dots
        draw.ellipse([160, web_y + 30, 180, web_y + 50], fill=ACCENT_RED)
        draw.ellipse([195, web_y + 30, 215, web_y + 50], fill=ACCENT_ORANGE)
        draw.ellipse([230, web_y + 30, 250, web_y + 50], fill=ACCENT_GREEN)
        draw.text((280, web_y + 25), "https://tokokopi-biasa.com", font=FONT_LABEL, fill=TEXT_MUTED)
        
        # Web clutter items yang membingungkan AI
        draw.rounded_rectangle([160, web_y + 90, 920, web_y + 180], radius=12, fill=(60, 20, 25), outline=ACCENT_RED, width=2)
        draw.text((540, web_y + 135), "⚠️ POPUP PROMO & BANNER IKAN BERKEDIP", font=FONT_LABEL, fill=TEXT_WHITE, anchor="mm")
        
        draw.rounded_rectangle([160, web_y + 210, 520, web_y + 310], radius=12, fill=CARD_BG, outline=CARD_BORDER, width=2)
        draw.text((185, web_y + 245), "Form Alamat Manual", font=FONT_LABEL, fill=TEXT_MUTED)
        draw.text((185, web_y + 275), "Kecamatan / Kode Pos?", font=FONT_SUB, fill=TEXT_WHITE)
        
        draw.rounded_rectangle([560, web_y + 210, 920, web_y + 310], radius=12, fill=CARD_BG, outline=CARD_BORDER, width=2)
        draw.text((585, web_y + 245), "Captcha Gambar", font=FONT_LABEL, fill=TEXT_MUTED)
        draw.text((585, web_y + 275), "Pilih gambar lampu lalu lintas", font=FONT_SUB, fill=ACCENT_RED)
        
        draw.text((540, web_y + 380), "⛔ AI TIDAK BISA KLIK TOMBOL MANUAL!", font=FONT_HEADLINE, fill=ACCENT_RED, anchor="mm")
        
        # Penjelasan Diagram Bawah
        box_bot_y = 960
        draw.rounded_rectangle([120, box_bot_y, 960, box_bot_y + 260], radius=20, fill=(30, 15, 20), outline=ACCENT_RED, width=2)
        draw.text((160, box_bot_y + 40), "❌ KENAPA WEB BIASA GAGAL?", font=FONT_LABEL, fill=ACCENT_RED)
        draw.text((160, box_bot_y + 95), "1. Website dibuat untuk mata manusia, bukan AI.", font=FONT_SUB, fill=TEXT_WHITE)
        draw.text((160, box_bot_y + 150), "2. Tombol dan banner justru memblokir asisten AI.", font=FONT_SUB, fill=TEXT_WHITE)
        draw.text((160, box_bot_y + 205), "3. AI butuh jalur data langsung (Machine Protocol).", font=FONT_SUB, fill=ACCENT_ORANGE)

    # ---------------- SCENE 3: Detik 13.0 - 21.0s (Solusi Protokol MCP) ----------------
    elif t_sec < 21.0:
        draw_header_and_footer(draw, t_sec, "SOLUSI PROTOKOL", "Di sinilah protokol MCP bekerja.\nJalur data resmi langsung ke AI.", 2)
        
        # Sisi Kiri: Toko UMKM
        toko_x = 100
        box_y = 500
        box_w = 360
        box_h = 240
        draw.rounded_rectangle([toko_x, box_y, toko_x + box_w, box_y + box_h], radius=20, fill=CARD_BG, outline=ACCENT_GREEN, width=3)
        draw.text((toko_x + box_w//2, box_y + 40), "🏪 TOKO ANDA", font=FONT_LABEL, fill=ACCENT_GREEN, anchor="mm")
        draw.text((toko_x + box_w//2, box_y + 95), "Menu Kopi & Stok", font=FONT_HEADLINE, fill=TEXT_WHITE, anchor="mm")
        draw.text((toko_x + box_w//2, box_y + 155), "Tersedia 50 Cup Ready", font=FONT_SUB, fill=TEXT_MUTED, anchor="mm")
        draw.text((toko_x + box_w//2, box_y + 195), "● Terhubung via MCP", font=FONT_LABEL, fill=ACCENT_GREEN, anchor="mm")
        
        # Sisi Kanan: Otak AI Pelanggan
        ai_x = WIDTH - 100 - box_w
        draw.rounded_rectangle([ai_x, box_y, ai_x + box_w, box_y + box_h], radius=20, fill=CARD_BG, outline=ACCENT_BLUE, width=3)
        draw.text((ai_x + box_w//2, box_y + 40), "🧠 ASISTEN AI", font=FONT_LABEL, fill=ACCENT_BLUE, anchor="mm")
        draw.text((ai_x + box_w//2, box_y + 95), "Customer Agent", font=FONT_HEADLINE, fill=TEXT_WHITE, anchor="mm")
        draw.text((ai_x + box_w//2, box_y + 155), "Membaca Katalog Instan", font=FONT_SUB, fill=TEXT_MUTED, anchor="mm")
        draw.text((ai_x + box_w//2, box_y + 195), "● Siap Eksekusi Beli", font=FONT_LABEL, fill=ACCENT_BLUE, anchor="mm")
        
        # Pipa Jembatan Tengah (MCP Bridge)
        pipe_x1 = toko_x + box_w
        pipe_x2 = ai_x
        pipe_cy = box_y + box_h // 2
        draw.line([pipe_x1, pipe_cy, pipe_x2, pipe_cy], fill=CARD_BORDER, width=8)
        draw_dotted_flow(draw, (pipe_x1, pipe_cy), (pipe_x2, pipe_cy), t_sec, ACCENT_ORANGE)
        
        # Badge Tengah "PROTOKOL MCP"
        badge_w = 260
        badge_h = 70
        badge_x = (WIDTH - badge_w) // 2
        draw.rounded_rectangle([badge_x, pipe_cy - badge_h//2, badge_x + badge_w, pipe_cy + badge_h//2], radius=16, fill=(35, 20, 10), outline=ACCENT_ORANGE, width=3)
        draw.text((WIDTH // 2, pipe_cy), "⚡ PROTOKOL MCP ⚡", font=FONT_LABEL, fill=ACCENT_ORANGE, anchor="mm")
        
        # 3 Poin Keunggulan (Card Bawah)
        bot_y = 820
        draw.rounded_rectangle([100, bot_y, WIDTH - 100, bot_y + 360], radius=24, fill=CARD_BG, outline=CARD_BORDER, width=2)
        draw.text((150, bot_y + 50), "BAGAIMANA CARA KERJANYA?", font=FONT_LABEL, fill=ACCENT_ORANGE)
        draw.text((150, bot_y + 115), "1. AI membaca daftar menu toko tanpa buka browser.", font=FONT_SUB, fill=TEXT_WHITE)
        draw.text((150, bot_y + 185), "2. AI otomatis kunci stok dan hitung total pesanan.", font=FONT_SUB, fill=TEXT_WHITE)
        draw.text((150, bot_y + 255), "3. AI bayar instan pakai token QRIS terenkripsi.", font=FONT_SUB, fill=ACCENT_GREEN)

    # ---------------- SCENE 4: Detik 21.0 - 30.0s (Hasil & Call-to-Action) ----------------
    else:
        draw_header_and_footer(draw, t_sec, "HASIL OPERASIONAL", "Orderan masuk WA Kasir Anda.\nKomisi Ojol: 0% Bersih!", 2)
        
        # Mockup Layar WhatsApp Kasir
        wa_y = 440
        draw.rounded_rectangle([120, wa_y, WIDTH - 120, wa_y + 380], radius=24, fill=CARD_BG, outline=ACCENT_GREEN, width=3)
        
        # WA Top Header
        draw.rounded_rectangle([120, wa_y, WIDTH - 120, wa_y + 70], radius=24, fill=(15, 35, 25))
        draw.text((160, wa_y + 35), "💬 WhatsApp Toko • Pesanan Masuk!", font=FONT_LABEL, fill=ACCENT_GREEN, anchor="lm")
        
        # WA Message Bubble
        draw.rounded_rectangle([160, wa_y + 95, WIDTH - 160, wa_y + 340], radius=16, fill=(20, 45, 35), outline=ACCENT_GREEN, width=2)
        draw.text((190, wa_y + 130), "🔔 PESANAN BARU VIA ASISTEN AI!", font=FONT_LABEL, fill=TEXT_WHITE)
        draw.text((190, wa_y + 175), "• 2 Cup Kopi Susu Gula Aren", font=FONT_HEADLINE, fill=TEXT_WHITE)
        draw.text((190, wa_y + 235), "• Total: Rp 36.000 (QRIS LUNAS ✓)", font=FONT_HEADLINE, fill=ACCENT_GREEN)
        draw.text((190, wa_y + 290), "• Kirim ke: Jl. Kemenangan No. 99", font=FONT_SUB, fill=TEXT_MUTED)
        
        # Stempel Merah Komisi 0%
        stamp_y = 860
        draw.rounded_rectangle([140, stamp_y, WIDTH - 140, stamp_y + 150], radius=18, fill=(45, 15, 20), outline=ACCENT_RED, width=4)
        draw.text((WIDTH // 2, stamp_y + 50), "POTONGAN KOMISI: 0%", font=FONT_HERO, fill=ACCENT_RED, anchor="mm")
        draw.text((WIDTH // 2, stamp_y + 105), "Semua keuntungan 100% masuk rekening toko Anda!", font=FONT_SUB, fill=TEXT_WHITE, anchor="mm")
        
        # Call To Action Box (DM/PC Sekarang)
        cta_y = 1050
        draw.rounded_rectangle([120, cta_y, WIDTH - 120, cta_y + 180], radius=24, fill=ACCENT_ORANGE)
        draw.text((WIDTH // 2, cta_y + 55), "📩 CUKUP DM / PC SEKARANG", font=FONT_HERO, fill=(0, 0, 0), anchor="mm")
        draw.text((WIDTH // 2, cta_y + 120), "Jasa Pasang Terima Beres • Konsultasi Gratis", font=FONT_HEADLINE, fill=(0, 0, 0), anchor="mm")
    
    return img

def main():
    output_dir = "scripts/output"
    os.makedirs(output_dir, exist_ok=True)
    temp_video = os.path.join(output_dir, "temp_benergak.mp4")
    final_video = os.path.join(output_dir, "mcp-benergak-authentic.mp4")
    voice_audio = "assets/audio/vo_storytelling.mp3"
    
    print(f"Rendering {TOTAL_FRAMES} frames (30.0s @ {FPS} FPS)...")
    
    # Pipe frames directly to FFmpeg
    ffmpeg_cmd = [
        "ffmpeg", "-y",
        "-f", "rawvideo",
        "-vcodec", "rawvideo",
        "-s", f"{WIDTH}x{HEIGHT}",
        "-pix_fmt", "rgb24",
        "-r", str(FPS),
        "-i", "-",
        "-c:v", "libx264",
        "-preset", "veryfast",
        "-crf", "18",
        "-pix_fmt", "yuv420p",
        temp_video
    ]
    
    proc = subprocess.Popen(ffmpeg_cmd, stdin=subprocess.PIPE)
    assert proc.stdin is not None
    for i in range(TOTAL_FRAMES):
        frame = render_frame(i)
        proc.stdin.write(frame.tobytes())
        if i % 150 == 0:
            print(f"Frame {i}/{TOTAL_FRAMES} ({i/FPS:.1f}s) done.")
            
    proc.stdin.close()
    proc.wait()
    print("Video stream created. Merging natural studio audio...")
    
    # Merge with audio
    merge_cmd = [
        "ffmpeg", "-y",
        "-i", temp_video,
        "-i", voice_audio,
        "-c:v", "copy",
        "-c:a", "aac",
        "-b:a", "192k",
        "-shortest",
        final_video
    ]
    subprocess.run(merge_cmd, check=True)
    print(f"Masterpiece Video Render Complete -> {final_video}")

if __name__ == "__main__":
    main()
