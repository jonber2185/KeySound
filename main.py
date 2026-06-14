import os
import sys
import pygame
import keyboard

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()

SOUND_DUCK = resource_path("sound/duck.wav")
SOUND_FAT_BIG = resource_path("sound/fat_big.wav")
SOUND_FAT_LONG = resource_path("sound/fat_long.wav")
SOUND_FAT_NORMAL = resource_path("sound/fat_normal.wav")

def load_sound(file_path):
    if not os.path.exists(file_path):
        print("Can not find sound file: " + file_path)
        return None
    return pygame.mixer.Sound(file_path)

sounds = {
    "default": load_sound(SOUND_DUCK),
    "enter": load_sound(SOUND_FAT_BIG),
    "backspace": load_sound(SOUND_FAT_LONG),
    "space": load_sound(SOUND_FAT_NORMAL)
}

def play_key_sound(event):
    if event.event_type == keyboard.KEY_DOWN:
        key_name = event.name
        if key_name in sounds and sounds[key_name] is not None:
            sounds[key_name].play()
        else: sounds["default"].play()

keyboard.hook(play_key_sound)
keyboard.wait()