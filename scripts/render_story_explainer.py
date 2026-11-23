"""
Motion Explainer ala @benergak_v1 & video-shotcraft (Remotion/After Effects style).
- 30 Detik Durasi Sinkron Narasi Puck.
- Dynamic Visual Metaphors:
  1. Phone UI & Voice waveform (Detik 0 - 6.5s)
  2. The Blindfold / Glitch on traditional website (Detik 6.5 - 12.5s)
  3. The Glowing Cable / Bridge (Toko -> MCP -> Otak AI) (Detik 12.5 - 18.5s)
  4. WhatsApp Cashier Notification with QRIS Stamp 0% Komisi (Detik 18.5 - 24.5s)
  5. Cinematic CTA Lockup: DM / PC Sekarang (Detik 24.5 - 30.0s)
"""
import os
import math
import subprocess
from PIL import Image, ImageDraw, ImageFont

WIDTH, HEIGHT = 1080, 1920
FPS = 30
DURATION_SEC = 30.0
TOTAL_FRAMES = int(FPS * DURATION_SEC) # 900 frames

BG_DARK = (11, 13, 17)
ACCENT_GREEN = (37, 211, 102)
ACCENT_BLUE = (56, 139, 253)
ACCENT_PURPLE = (163, 113, 247)
ACCENT_RED = (248, 81, 73)
ACCENT_YELLOW = (245, 158, 11)
TEXT_WHITE = (240, 246, 252)
TEXT_MUTED = (139, 148, 158)

def get_font(size, bold=False):
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
    ]
    for p in candidates:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()

FONT_GIANT = get_font(88, bold=True)
FONT_HEAD = get_font(60, bold=True)
FONT_TITLE = get_font(44, bold=True)
FONT_BODY = get_font(36, bold=False)
FONT_BADGE = get_font(28, bold=True)
FONT_BIG_BADGE = get_font(38, bold=True)

def ease_out_cubic(t):
    t = max(0.0, min(1.0, t))
    return 1.0 - math.pow(1.0 - t, 3)

def ease_out_back(t):
    c1 = 1.70158
    c3 = c1 + 1
    t = max(0.0, min(1.0, t))
    return 1 + c3 * math.pow(t - 1, 3) + c1 * math.pow(t - 1, 2)

def draw_pill(draw, text, x, y, bg_color, text_color, font=FONT_BADGE, padding_x=40, padding_y=20):
    bbox = font.getbbox(text)
    w = bbox[2] - bbox[0] + padding_x
    h = bbox[3] - bbox[1] + padding_y
    draw.rounded_rectangle([x - w // 2, y - h // 2, x + w // 2, y + h // 2], radius=h // 2, fill=bg_color)
    draw.text((x, y), text, font=font, fill=text_color, anchor="mm")

def render_frame(frame_idx):
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_DARK)
    draw = ImageDraw.Draw(img)

    t_sec = frame_idx / FPS

    # 1. Background Grid with Perspective Flow
    grid_offset = int((frame_idx * 1.5) % 120)
    for gy in range(-120, HEIGHT + 120, 120):
        y_pos = gy + grid_offset
        draw.line([(0, y_pos), (WIDTH, y_pos)], fill=(16, 20, 26), width=1)
    for gx in range(0, WIDTH, 120):
        draw.line([(gx, 0), (gx, HEIGHT)], fill=(16, 20, 26), width=1)

    # =========================================================================
    # SCENE 1: (0.0s - 6.5s) "Pernah sadar gak? Orang makin malas buka aplikasi..."
    # Visual: Voice Waveform & AI Smartphone Shell
    # =========================================================================
    if t_sec < 6.5:
        p = ease_out_cubic(t_sec / 0.8)
        draw_pill(draw, "PERUBAHAN ZAMAN", WIDTH // 2, 380, (26, 36, 56), ACCENT_BLUE)
        
        y_title = int(520 - (1.0 - p) * 50)
        draw.text((WIDTH // 2, y_title), "Malas Buka Aplikasi?", font=FONT_GIANT, fill=TEXT_WHITE, anchor="mm")
        
        # Phone mockup container
        phone_y = int(680 - (1.0 - p) * 40)
        draw.rounded_rectangle([200, phone_y, WIDTH - 200, phone_y + 800], radius=44, fill=(18, 22, 30), outline=(45, 55, 72), width=3)
        # Dynamic animated audio waveform inside phone
        wave_cx = WIDTH // 2
        wave_cy = phone_y + 260
        num_bars = 18
        for b in range(num_bars):
            bx = wave_cx - (num_bars * 16) + (b * 32)
            wave_h = max(10, int(abs(25 + 55 * math.sin(t_sec * 8.0 + b * 0.45) * math.cos(t_sec * 4.0))))
            draw.rounded_rectangle([bx - 6, wave_cy - wave_h, bx + 6, wave_cy + wave_h], radius=6, fill=ACCENT_BLUE)

        draw.text((WIDTH // 2, phone_y + 390), "🎙️ Asisten AI Mendengarkan...", font=FONT_BADGE, fill=TEXT_MUTED, anchor="mm")

        # Chat Bubble Pops in
        if t_sec > 2.0:
            bubble_p = ease_out_back(min(1.0, (t_sec - 2.0) / 0.6))
            bubble_w = int(580 * bubble_p)
            bx1 = WIDTH // 2 - bubble_w // 2
            bx2 = WIDTH // 2 + bubble_w // 2
            draw.rounded_rectangle([bx1, phone_y + 480, bx2, phone_y + 640], radius=24, fill=(30, 41, 59), outline=ACCENT_BLUE, width=2)
            if bubble_p > 0.8:
                draw.text((WIDTH // 2, phone_y + 535), '"JARVIS, pesanin kopi susu', font=FONT_TITLE, fill=TEXT_WHITE, anchor="mm")
                draw.text((WIDTH // 2, phone_y + 590), 'langsung ke rumah."', font=FONT_TITLE, fill=ACCENT_BLUE, anchor="mm")

    # =========================================================================
    # SCENE 2: (6.5s - 12.5s) "Tapi masalahnya, AI itu buta! Gak bisa klik web ribet..."
    # Visual: Red Alert, "AI BUTA", Glitched Web Mockup with Cluttered Popups
    # =========================================================================
    elif t_sec < 12.5:
        local_t = t_sec - 6.5
        p = ease_out_cubic(local_t / 0.8)
        
        draw_pill(draw, "MASALAH BESAR", WIDTH // 2, 380, (48, 20, 20), ACCENT_RED)
        
        y_title = int(520 - (1.0 - p) * 50)
        draw.text((WIDTH // 2, y_title), "Tapi... AI Itu Buta!", font=FONT_GIANT, fill=ACCENT_RED, anchor="mm")

        # Mockup Browser Clutter / The Problem
        box_y = int(680 - (1.0 - p) * 40)
        draw.rounded_rectangle([140, box_y, WIDTH - 140, box_y + 820], radius=32, fill=(24, 18, 20), outline=(70, 30, 35), width=2)
        
        # Browser header mock
        draw.rounded_rectangle([140, box_y, WIDTH - 140, box_y + 80], radius=32, fill=(35, 22, 25))
        draw.ellipse([180, box_y + 28, 204, box_y + 52], fill=(239, 68, 68))
        draw.ellipse([220, box_y + 28, 244, box_y + 52], fill=(245, 158, 11))
        draw.ellipse([260, box_y + 28, 284, box_y + 52], fill=(16, 185, 129))
        draw.text((WIDTH // 2, box_y + 40), "https://website-toko-biasa.com", font=FONT_BADGE, fill=TEXT_MUTED, anchor="mm")

        # Cluttered Bad Elements that AI CANNOT click
        # Popup 1: Banner Diskon
        draw.rounded_rectangle([180, box_y + 140, WIDTH - 180, box_y + 300], radius=20, fill=(45, 25, 28), outline=ACCENT_RED, width=2)
        draw.text((WIDTH // 2, box_y + 200), "⚠️ POPUP PROMO DISKON 50%", font=FONT_TITLE, fill=ACCENT_RED, anchor="mm")
        draw.text((WIDTH // 2, box_y + 250), "AI gak bisa klik tombol close!", font=FONT_BODY, fill=TEXT_MUTED, anchor="mm")

        # Popup 2: Captcha / Formulir Alamat Ribet
        if local_t > 1.8:
            cap_p = ease_out_back(min(1.0, (local_t - 1.8) / 0.6))
            cy = int(box_y + 340 - (1.0 - cap_p) * 30)
            draw.rounded_rectangle([180, cy, WIDTH - 180, cy + 220], radius=20, fill=(35, 20, 24), outline=(245, 158, 11), width=2)
            draw.text((WIDTH // 2, cy + 80), "❌ FORMULIR ALAMAT BERBELIT", font=FONT_TITLE, fill=(245, 158, 11), anchor="mm")
            draw.text((WIDTH // 2, cy + 140), "AI bingung membaca antarmuka manusia", font=FONT_BODY, fill=TEXT_WHITE, anchor="mm")

        # Warning Badge
        draw_pill(draw, "AI BUTUH DATA MESIN, BUKAN GAMBAR", WIDTH // 2, box_y + 700, (60, 20, 25), (255, 100, 100), font=FONT_TITLE, padding_x=50, padding_y=30)

    # =========================================================================
    # SCENE 3: (12.5s - 18.5s) "Di sinilah MCP bekerja! Kabel data langsung dari toko ke otak AI..."
    # Visual: The Glowing Bridge / Cable (Toko Fisik <==== MCP ====> Otak AI)
    # =========================================================================
    elif t_sec < 18.5:
        local_t = t_sec - 12.5
        p = ease_out_cubic(local_t / 0.8)

        draw_pill(draw, "TEROBOSAN TEKNOLOGI", WIDTH // 2, 360, (20, 48, 30), ACCENT_GREEN)

        y_title = int(500 - (1.0 - p) * 50)
        draw.text((WIDTH // 2, y_title), "Solusinya: Protokol MCP!", font=FONT_GIANT, fill=ACCENT_GREEN, anchor="mm")

        bridge_y = 660
        # Card 1: TOKO UMKM (Kiri)
        draw.rounded_rectangle([100, bridge_y, 440, bridge_y + 320], radius=24, fill=(18, 28, 22), outline=ACCENT_GREEN, width=3)
        draw.text((270, bridge_y + 90), "🏪", font=get_font(70), anchor="mm")
        draw.text((270, bridge_y + 190), "TOKO ANDA", font=FONT_HEAD, fill=TEXT_WHITE, anchor="mm")
        draw.text((270, bridge_y + 250), "Katalog & Menu", font=FONT_BADGE, fill=TEXT_MUTED, anchor="mm")

        # Card 2: OTAK AI (Kanan)
        draw.rounded_rectangle([WIDTH - 440, bridge_y, WIDTH - 100, bridge_y + 320], radius=24, fill=(20, 28, 44), outline=ACCENT_BLUE, width=3)
        draw.text((WIDTH - 270, bridge_y + 90), "🧠", font=get_font(70), anchor="mm")
        draw.text((WIDTH - 270, bridge_y + 190), "ASISTEN AI", font=FONT_HEAD, fill=TEXT_WHITE, anchor="mm")
        draw.text((WIDTH - 270, bridge_y + 250), "Konsumen Cerdas", font=FONT_BADGE, fill=TEXT_MUTED, anchor="mm")

        # Glowing Pulse Cable connecting them
        pulse = (math.sin(local_t * 10.0) + 1.0) / 2.0
        cable_color = (int(37 + pulse * 100), int(211 + pulse * 44), int(102 + pulse * 100))
        draw.line([(440, bridge_y + 160), (WIDTH - 440, bridge_y + 160)], fill=cable_color, width=8)
        
        # Center Connector Badge (MCP)
        draw_pill(draw, "⚡ PROTOKOL MCP ⚡", WIDTH // 2, bridge_y + 160, (10, 40, 20), (50, 255, 130), font=FONT_BIG_BADGE, padding_x=60, padding_y=32)

        # Highlight Points below
        if local_t > 1.2:
            card2_p = ease_out_cubic((local_t - 1.2) / 0.8)
            c2_y = int(1120 - (1.0 - card2_p) * 40)
            draw.rounded_rectangle([120, c2_y, WIDTH - 120, c2_y + 280], radius=24, fill=(18, 24, 32), outline=(40, 50, 68), width=2)
            draw.text((170, c2_y + 70), "💡 Apa itu MCP?", font=FONT_HEAD, fill=ACCENT_GREEN)
            draw.text((170, c2_y + 140), "• Colokan resmi agar AI membaca toko Anda secara instan.", font=FONT_BODY, fill=TEXT_WHITE)
            draw.text((170, c2_y + 200), "• Bebas hambatan visual & otomatis terstandarisasi.", font=FONT_BODY, fill=TEXT_MUTED)

    # =========================================================================
    # SCENE 4: (18.5s - 24.5s) "Orderan langsung loncat ke WhatsApp kasir lengkap QRIS, komisi 0%..."
    # Visual: WhatsApp Cashier UI + Big Stamp "KOMISI 0%"
    # =========================================================================
    elif t_sec < 24.5:
        local_t = t_sec - 18.5
        p = ease_out_cubic(local_t / 0.8)

        draw_pill(draw, "HASIL LANGSUNG DI KASIR", WIDTH // 2, 360, (20, 48, 30), ACCENT_GREEN)

        y_title = int(500 - (1.0 - p) * 50)
        draw.text((WIDTH // 2, y_title), "Order Masuk ke WA Kasir!", font=FONT_GIANT, fill=TEXT_WHITE, anchor="mm")

        # WhatsApp Message Bubble Card
        wa_y = int(660 - (1.0 - p) * 40)
        draw.rounded_rectangle([100, wa_y, WIDTH - 100, wa_y + 540], radius=28, fill=(15, 30, 22), outline=ACCENT_GREEN, width=3)
        
        # WA header
        draw.rounded_rectangle([100, wa_y, WIDTH - 100, wa_y + 80], radius=28, fill=(20, 45, 32))
        draw.text((150, wa_y + 40), "💬 WhatsApp Kasir Toko", font=FONT_TITLE, fill=ACCENT_GREEN)

        # Message body
        draw.text((150, wa_y + 130), "🔔 *PESANAN BARU DARI AI!*", font=FONT_HEAD, fill=TEXT_WHITE)
        draw.text((150, wa_y + 200), "• 2x Kopi Susu Gula Aren", font=FONT_BODY, fill=TEXT_WHITE)
        draw.text((150, wa_y + 260), "• Kirim: Jl. Kemenangan No. 99", font=FONT_BODY, fill=TEXT_MUTED)
        draw.text((150, wa_y + 320), "• Total: Rp 36.000", font=FONT_BODY, fill=TEXT_WHITE)
        draw.text((150, wa_y + 380), "• Status: LUNAS VIA QRIS ✅", font=FONT_HEAD, fill=ACCENT_GREEN)

        # Big Stamp: POTONGAN KOMISI 0% (Melayang & Berotasi sedikit)
        if local_t > 1.0:
            stamp_p = ease_out_back(min(1.0, (local_t - 1.0) / 0.6))
            stamp_y = int(1300 - (1.0 - stamp_p) * 60)
            draw.rounded_rectangle([120, stamp_y, WIDTH - 120, stamp_y + 200], radius=24, fill=(48, 20, 20), outline=ACCENT_RED, width=4)
            draw.text((WIDTH // 2, stamp_y + 65), "POTONGAN OJOL: 0%", font=FONT_GIANT, fill=ACCENT_RED, anchor="mm")
            draw.text((WIDTH // 2, stamp_y + 140), "Uang 100% Masuk ke Rekening Toko Anda", font=FONT_BODY, fill=TEXT_WHITE, anchor="mm")

    # =========================================================================
    # SCENE 5: (24.5s - 30.0s) "Mau toko Anda dipasangin terima beres? Cukup DM atau PC sekarang juga!"
    # Visual: Hero Closing CTA Lockup
    # =========================================================================
    else:
        local_t = t_sec - 24.5
        p = ease_out_cubic(local_t / 0.8)

        draw_pill(draw, "JASA INSTALASI RESMI", WIDTH // 2, 400, (40, 24, 56), ACCENT_PURPLE)

        y_title = int(550 - (1.0 - p) * 50)
        draw.text((WIDTH // 2, y_title), "Mau Toko Anda", font=FONT_GIANT, fill=TEXT_WHITE, anchor="mm")
        draw.text((WIDTH // 2, y_title + 105), "Dipasangin Terima Beres?", font=FONT_GIANT, fill=ACCENT_PURPLE, anchor="mm")

        # CTA Hero Card
        cta_y = int(880 - (1.0 - p) * 40)
        draw.rounded_rectangle([100, cta_y, WIDTH - 100, cta_y + 440], radius=32, fill=(20, 24, 36), outline=ACCENT_BLUE, width=3)
        
        draw.text((WIDTH // 2, cta_y + 80), "KONSULTASI & JASA SETUP:", font=FONT_TITLE, fill=TEXT_MUTED, anchor="mm")
        draw.text((WIDTH // 2, cta_y + 180), "📩 Cukup DM / PC Sekarang", font=FONT_GIANT, fill=ACCENT_BLUE, anchor="mm")
        
        draw.line([(180, cta_y + 260), (WIDTH - 180, cta_y + 260)], fill=(40, 50, 70), width=2)
        
        draw.text((WIDTH // 2, cta_y + 330), "• Kami pasangkan dari awal sampai siap", font=FONT_BODY, fill=TEXT_WHITE, anchor="mm")
        draw.text((WIDTH // 2, cta_y + 380), "• Toko langsung bisa dipesan via AI!", font=FONT_BODY, fill=ACCENT_GREEN, anchor="mm")

        # Final Trust Badge
        draw_pill(draw, "⚡ KUOTA INSTALASI TERBATAS ⚡", WIDTH // 2, 1460, (26, 36, 56), ACCENT_BLUE, font=FONT_TITLE, padding_x=60, padding_y=30)

    return img

def main():
    out_dir = "scripts/output"
    os.makedirs(out_dir, exist_ok=True)
    frames_dir = "/tmp/story_frames"
    os.makedirs(frames_dir, exist_ok=True)

    print(f"Rendering {TOTAL_FRAMES} frames ({DURATION_SEC}s @ {FPS} FPS)...")
    for i in range(TOTAL_FRAMES):
        frame = render_frame(i)
        frame.save(f"{frames_dir}/frame_{i:05d}.png")
        if i % 150 == 0:
            print(f"Progress: frame {i}/{TOTAL_FRAMES} ({(i/TOTAL_FRAMES)*100:.1f}%)")

    voice_path = "assets/audio/vo_storytelling.mp3"
    final_video = f"{out_dir}/mcp-benergak-story.mp4"

    cmd = [
        "ffmpeg", "-y",
        "-framerate", str(FPS),
        "-i", f"{frames_dir}/frame_%05d.png",
        "-i", voice_path,
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        "-crf", "18",
        "-preset", "fast",
        "-c:a", "aac",
        "-b:a", "192k",
        "-shortest",
        final_video
    ]
    print("Compiling video with FFmpeg + Storytelling Voiceover...")
    subprocess.run(cmd, check=True)
    print(f"SUCCESS! Explainer video created at: {final_video}")

if __name__ == "__main__":
    main()
