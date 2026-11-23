import wave
import struct
import math
import os

SAMPLE_RATE = 44100

def generate_sfx(output_dir):
    os.makedirs(output_dir, exist_ok=True)
    
    # 1. Haptic Tap (iOS style tactile click)
    tap_path = os.path.join(output_dir, "tap.wav")
    num_samples = int(SAMPLE_RATE * 0.04)
    data = bytearray()
    for i in range(num_samples):
        t = i / SAMPLE_RATE
        env = math.exp(-t * 110.0)
        freq = 80.0 + (320.0 - 80.0) * math.exp(-t * 120.0)
        sample = int(32767.0 * env * 0.85 * math.sin(2.0 * math.pi * freq * t))
        data.extend(struct.pack("<h", max(-32768, min(32767, sample))))
    with wave.open(tap_path, "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SAMPLE_RATE); w.writeframes(data)
        
    # 2. Ding / Notification Chime (WhatsApp arrival)
    bell_path = os.path.join(output_dir, "ding.wav")
    num_samples = int(SAMPLE_RATE * 0.8)
    data = bytearray()
    for i in range(num_samples):
        t = i / SAMPLE_RATE
        env = math.exp(-t * 5.5)
        h1 = math.sin(2.0 * math.pi * 1046.5 * t) # C6
        h2 = 0.5 * math.sin(2.0 * math.pi * 2093.0 * t) # C7
        sample = int(32767.0 * env * 0.7 * (h1 + h2))
        data.extend(struct.pack("<h", max(-32768, min(32767, sample))))
    with wave.open(bell_path, "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SAMPLE_RATE); w.writeframes(data)

    # 3. QRIS Success Chime
    qris_path = os.path.join(output_dir, "success.wav")
    num_samples = int(SAMPLE_RATE * 1.0)
    data = bytearray()
    for i in range(num_samples):
        t = i / SAMPLE_RATE
        env = math.exp(-t * 4.0)
        # major chord: E6 (1318.5) + G#6 (1661.2) + B6 (1975.5)
        h1 = math.sin(2.0 * math.pi * 1318.5 * t)
        h2 = 0.6 * math.sin(2.0 * math.pi * 1661.2 * t)
        h3 = 0.4 * math.sin(2.0 * math.pi * 1975.5 * t)
        sample = int(32767.0 * env * 0.6 * (h1 + h2 + h3))
        data.extend(struct.pack("<h", max(-32768, min(32767, sample))))
    with wave.open(qris_path, "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SAMPLE_RATE); w.writeframes(data)

if __name__ == "__main__":
    generate_sfx("scripts/audio")
    print("SFX generated successfully.")
