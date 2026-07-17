# pyinstaller --noconsole --onefile --add-data "sound;sound" --add-data "icon_toilet.ico;." --icon=icon_toilet.ico main.py
import os
import threading
import pygame
import keyboard
from config import SOUND_FILES
from tray import setup_tray


# 44.1kHz, 16bit, stereo channel, buffer
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()

def load_sound(file_path):
    if not os.path.exists(file_path):
        print("Can not find sound file: " + file_path)
        return None
    return pygame.mixer.Sound(file_path)

sounds = {key: load_sound(path) for key, path in SOUND_FILES.items()}

def play_key_sound(event):
    if event.event_type == keyboard.KEY_DOWN:
        key_name = event.name
        if key_name in sounds and sounds[key_name] is not None:
            sounds[key_name].play()
        else:
            if sounds.get("default") is not None:
                sounds["default"].play()

if __name__ == "__main__":
    keyboard.hook(play_key_sound)

    tray_thread = threading.Thread(target=setup_tray, daemon=True)
    tray_thread.start()

    keyboard.wait()