"""
Motion Masterpiece v2: Edukasi Protokol MCP dengan Natural Studio Voiceover (Gemini Puck).
Call-to-Action disesuaikan: DM / PC (tanpa nomor WA).
Visual Standard: motion-design-mastery & remotion-claude-mastery.
One Focal Point, Staggered Spring Easing, Crisp Giant Typography.
"""
import os
import math
import subprocess
from PIL import Image, ImageDraw, ImageFont

WIDTH, HEIGHT = 1080, 1920
FPS = 30
DURATION_SEC = 22.0
TOTAL_FRAMES = int(FPS * DURATION_SEC) # 660 frames

BG_DARK = (11, 13, 17)
ACCENT_GREEN = (37, 211, 102)
ACCENT_BLUE = (56, 139, 253)
ACCENT_PURPLE = (163, 113, 247)
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

FONT_HERO = get_font(84, bold=True)
FONT_TITLE = get_font(52, bold=True)
FONT_BODY = get_font(40, bold=False)
FONT_BADGE = get_font(30, bold=True)
FONT_CTA = get_font(56, bold=True)

def ease_out_cubic(t):
    t = max(0.0, min(1.0, t))
    return 1.0 - math.pow(1.0 - t, 3)

def draw_badge(draw, text, x, y, bg_color, text_color):
    bbox = FONT_BADGE.getbbox(text)
    w = bbox[2] - bbox[0] + 48
    h = bbox[3] - bbox[1] + 28
    draw.rounded_rectangle([x - w // 2, y - h // 2, x + w // 2, y + h // 2], radius=14, fill=bg_color)
    draw.text((x, y), text, font=FONT_BADGE, fill=text_color, anchor="mm")

def render_frame(frame_idx):
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_DARK)
    draw = ImageDraw.Draw(img)

    # Ambient subtle grid
    for gx in range(0, WIDTH, 120):
        draw.line([(gx, 0), (gx, HEIGHT)], fill=(18, 22, 28), width=1)
    for gy in range(0, HEIGHT, 120):
        draw.line([(0, gy), (WIDTH, gy)], fill=(18, 22, 28), width=1)

    t_sec = frame_idx / FPS

    # SCENE 1: 0 - 5.5s (Hook: Era Baru Belanja via Asisten AI)
    if t_sec < 5.5:
        progress = ease_out_cubic(t_sec / 0.8)
        draw_badge(draw, "TRANSISI PERILAKU", WIDTH // 2, 420, (26, 32, 44), ACCENT_BLUE)
        
        y_hero = int(680 - (1.0 - progress) * 80)
        draw.text((WIDTH // 2, y_hero), "Orang Tidak Lagi", font=FONT_HERO, fill=TEXT_WHITE, anchor="mm")
        draw.text((WIDTH // 2, y_hero + 105), "Buka Browser.", font=FONT_HERO, fill=ACCENT_BLUE, anchor="mm")

        if t_sec > 1.2:
            card_p = ease_out_cubic((t_sec - 1.2) / 0.8)
            card_y = int(1080 - (1.0 - card_p) * 60)
            draw.rounded_rectangle([120, card_y, WIDTH - 120, card_y + 240], radius=24, fill=(20, 24, 32), outline=(40, 48, 60), width=2)
            draw.text((170, card_y + 60), "🎙️ Perintah Konsumen ke AI:", font=FONT_BADGE, fill=ACCENT_GREEN)
            draw.text((170, card_y + 130), '"Pesan kopi susu 2 cup, kirim ke rumah."', font=FONT_BODY, fill=TEXT_WHITE)

    # SCENE 2: 5.5 - 11.0s (The Problem: AI Butuh Protokol Resmi)
    elif t_sec < 11.0:
        local_t = t_sec - 5.5
        progress = ease_out_cubic(local_t / 0.8)
        draw_badge(draw, "TANTANGAN MESIN", WIDTH // 2, 420, (36, 20, 20), (248, 81, 73))

        y_hero = int(680 - (1.0 - progress) * 80)
        draw.text((WIDTH // 2, y_hero), "AI Tidak Bisa Baca", font=FONT_HERO, fill=TEXT_WHITE, anchor="mm")
        draw.text((WIDTH // 2, y_hero + 105), "Website yang Ribet.", font=FONT_HERO, fill=(248, 81, 73), anchor="mm")

        if local_t > 1.2:
            card_p = ease_out_cubic((local_t - 1.2) / 0.8)
            card_y = int(1080 - (1.0 - card_p) * 60)
            draw.rounded_rectangle([120, card_y, WIDTH - 120, card_y + 260], radius=24, fill=(20, 24, 32), outline=(40, 48, 60), width=2)
            draw.text((170, card_y + 60), "❌ Kendala Web Biasa:", font=FONT_BADGE, fill=(248, 81, 73))
            draw.text((170, card_y + 120), "• AI 'buta' melihat banner promosi.", font=FONT_BODY, fill=TEXT_WHITE)
            draw.text((170, card_y + 180), "• AI butuh standar data resmi.", font=FONT_BODY, fill=TEXT_MUTED)

    # SCENE 3: 11.0 - 16.5s (The Solution: Protokol MCP & Order Masuk WA)
    elif t_sec < 16.5:
        local_t = t_sec - 11.0
        progress = ease_out_cubic(local_t / 0.8)
        draw_badge(draw, "SOLUSI RESMI", WIDTH // 2, 400, (20, 36, 26), ACCENT_GREEN)

        y_hero = int(640 - (1.0 - progress) * 80)
        draw.text((WIDTH // 2, y_hero), "Protokol MCP", font=FONT_HERO, fill=ACCENT_GREEN, anchor="mm")
        draw.text((WIDTH // 2, y_hero + 100), "Jembatan Langsung ke Toko.", font=FONT_TITLE, fill=TEXT_WHITE, anchor="mm")

        if local_t > 1.0:
            card_p = ease_out_cubic((local_t - 1.0) / 0.8)
            card_y = int(980 - (1.0 - card_p) * 60)
            draw.rounded_rectangle([120, card_y, WIDTH - 120, card_y + 360], radius=24, fill=(18, 28, 22), outline=(37, 211, 102), width=2)
            draw.text((170, card_y + 55), "🔔 NOTIFIKASI WHATSAPP KASIR", font=FONT_BADGE, fill=ACCENT_GREEN)
            draw.text((170, card_y + 125), "• Pesanan AI langsung masuk WA toko", font=FONT_BODY, fill=TEXT_WHITE)
            draw.text((170, card_y + 195), "• Bukti bayar QRIS otomatis terverifikasi", font=FONT_BODY, fill=TEXT_WHITE)
            draw.text((170, card_y + 265), "• Bebas potongan komisi 20% ojol", font=FONT_BODY, fill=ACCENT_GREEN)

    # SCENE 4: 16.5 - 22.0s (CTA: Jasa Instalasi Terima Beres - DM / PC)
    else:
        local_t = t_sec - 16.5
        progress = ease_out_cubic(local_t / 0.8)
        draw_badge(draw, "LAYANAN TERIMA BERES", WIDTH // 2, 420, (32, 22, 44), ACCENT_PURPLE)

        y_hero = int(680 - (1.0 - progress) * 80)
        draw.text((WIDTH // 2, y_hero), "Siapkan Toko Anda", font=FONT_HERO, fill=TEXT_WHITE, anchor="mm")
        draw.text((WIDTH // 2, y_hero + 105), "Untuk Era AI.", font=FONT_HERO, fill=ACCENT_PURPLE, anchor="mm")

        if local_t > 0.8:
            card_p = ease_out_cubic((local_t - 0.8) / 0.8)
            card_y = int(1060 - (1.0 - card_p) * 60)
            draw.rounded_rectangle([120, card_y, WIDTH - 120, card_y + 320], radius=28, fill=(22, 26, 36), outline=(56, 139, 253), width=2)
            
            draw.text((WIDTH // 2, card_y + 80), "KONSULTASI & JASA PASANG", font=FONT_BADGE, fill=ACCENT_BLUE, anchor="mm")
            draw.text((WIDTH // 2, card_y + 160), "📩 Cukup DM / PC Sekarang", font=FONT_CTA, fill=TEXT_WHITE, anchor="mm")
            draw.text((WIDTH // 2, card_y + 235), "Kami pasangkan sampai siap terima order", font=FONT_BODY, fill=TEXT_MUTED, anchor="mm")

    return img

def main():
    out_dir = "scripts/output"
    os.makedirs(out_dir, exist_ok=True)
    frames_dir = "/tmp/mcp_voice_frames"
    os.makedirs(frames_dir, exist_ok=True)

    print(f"Rendering {TOTAL_FRAMES} frames ({DURATION_SEC}s @ {FPS} FPS)...")
    for i in range(TOTAL_FRAMES):
        frame = render_frame(i)
        frame.save(f"{frames_dir}/frame_{i:05d}.png")
        if i % 90 == 0:
            print(f"Progress: frame {i}/{TOTAL_FRAMES} ({(i/TOTAL_FRAMES)*100:.1f}%)")

    voice_path = "assets/audio/voiceover.mp3"
    final_video = f"{out_dir}/mcp-voice-masterpiece.mp4"

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
    print("Compiling video with FFmpeg + natural studio voiceover...")
    subprocess.run(cmd, check=True)
    print(f"SUCCESS! Masterpiece video with studio voice created at: {final_video}")

if __name__ == "__main__":
    main()
