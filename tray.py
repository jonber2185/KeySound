import os
import pystray
from pystray import MenuItem as item
from PIL import Image
from config import ICON_PATH

def on_quit(icon, item):
    icon.stop()
    os._exit(0)

def setup_tray():
    if os.path.exists(ICON_PATH):
        image = Image.open(ICON_PATH)
    else:
        image = Image.new('RGBA', (64, 64), color=(0, 0, 0, 0))

    menu = (
        item('quit', on_quit),
    )
    
    tray_icon = pystray.Icon("key_sound_app", image, "keyboard sound program", menu)
    tray_icon.run()