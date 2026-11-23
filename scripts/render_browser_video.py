"""
Browser-based Video Renderer via Playwright.
Renders HTML/CSS components to 1080x1920 frames and merges with studio voiceover.
Runs in GitHub Actions cloud runner for pixel-perfect typography and 0% VPS load.
"""
import os
import sys
import subprocess
from playwright.sync_api import sync_playwright
sys.path.append(os.path.dirname(__file__))
from generate_html_scene_v3 import get_html_for_time

WIDTH = 1080
HEIGHT = 1920
FPS = 30
DURATION_SEC = 40.12
TOTAL_FRAMES = int(FPS * DURATION_SEC)

def main():
    output_dir = "scripts/output"
    os.makedirs(output_dir, exist_ok=True)
    temp_video = os.path.join(output_dir, "temp_browser.mp4")
    final_video = os.path.join(output_dir, "mcp-browser-masterpiece.mp4")
    voice_audio = "assets/audio/vo_storytelling_full.mp3"

    print(f"Starting Browser Renderer: {TOTAL_FRAMES} frames ({DURATION_SEC}s @ {FPS} FPS)...")

    # Start Playwright
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": WIDTH, "height": HEIGHT})

        # Start FFmpeg pipe
        ffmpeg_cmd = [
            "ffmpeg", "-y",
            "-f", "image2pipe",
            "-vcodec", "mjpeg",
            "-r", str(FPS),
            "-i", "-",
            "-c:v", "libx264",
            "-preset", "veryfast",
            "-crf", "17",
            "-pix_fmt", "yuv420p",
            temp_video
        ]
        proc = subprocess.Popen(ffmpeg_cmd, stdin=subprocess.PIPE)
        assert proc.stdin is not None

        # Load HTML generator v4 (40.12s full sync)
        from generate_html_scene_v4 import get_html_for_time
        with open("templates/base.html", "r") as f:
            base_html = f.read()

        # Cache last rendered HTML to avoid re-rendering identical DOM if unchanged
        last_html = ""

        for i in range(TOTAL_FRAMES):
            t_sec = i / FPS
            page_content = get_html_for_time(t_sec)
            full_html = base_html.replace('<div class="container" id="app"></div>', f'<div class="container" id="app">{page_content}</div>')

            # Update content in browser
            page.set_content(full_html)
            screenshot_bytes = page.screenshot(type="jpeg", quality=95)
            proc.stdin.write(screenshot_bytes)

            if i % 150 == 0:
                print(f"Rendered frame {i}/{TOTAL_FRAMES} ({t_sec:.1f}s)...")

        proc.stdin.close()
        proc.wait()
        browser.close()

    print("Browser rendering complete. Merging natural studio audio...")
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
    print(f"Masterpiece MP4 Ready: {final_video}")

if __name__ == "__main__":
    main()
