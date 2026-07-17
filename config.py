import os
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

ICON_PATH = resource_path("icon_toilet.ico")
SOUND_FILES = {
    "default": resource_path("sound/duck.wav"),
    "enter": resource_path("sound/fat_big.wav"),
    "backspace": resource_path("sound/fat_long.wav"),
    "space": resource_path("sound/fat_normal.wav"),
}