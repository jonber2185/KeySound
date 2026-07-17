# KeySound

> A Python background desktop application that plays customizable sound effects on keypresses and runs quietly in the system tray.

---

## Features

- **Custom Sound Effects** — plays specific WAV audio files mapped to key inputs (e.g., Enter, Space, Backspace, Default)
- **Low-Latency Audio** — pre-initialized Pygame mixer buffer to ensure near-instant audio playback without delay
- **System Tray Integration** — runs silently in the background taskbar notification area without cluttering your desktop or command prompt
- **Single Executable Support** — bundled with full support for standalone `.exe` binaries using PyInstaller

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3 |
| Audio Engine | [Pygame](https://www.pygame.org/) (`pygame.mixer`) |
| Global Keyboard Listener | [keyboard](https://github.com/boppreh/keyboard) |
| System Tray | [pystray](https://github.com/moses-palmer/pystray) |
| Image Processing | [Pillow (PIL)](https://python-pillow.org/) |
| Packaging | [PyInstaller](https://pyinstaller.org/) |

## Project Structure

```text
├── config.py       # Resource paths and sound mappings
├── tray.py         # System tray icon and exit logic
├── main.py         # App entry point and keyboard hook handling
├── icon.ico        # Tray icon file
└── sound/          # Audio files directory (.wav)
    ├── duck.wav
    ├── fat_big.wav
    ├── fat_long.wav
    └── fat_normal.wav
```

## How to Run

Download the latest release from the [Releases page](https://github.com/jonber2185/KeySound/releases).

### Option 1 - Windows EXE

1. Download `key_sound.exe` from the release.
2. Run `key_sound.exe`

### Option 2 — From source (Python)

1. Install the required dependencies:
```bash
pip install -r ./requirement.txt
```
2. Run main.py with Administrator privileges:
```bash
python main.py
```

## How To Quit

1. Look for the application icon in the System Tray.
2. Rignt-click the tray icon and select `quit` to exit the program.

## Note
- Global keyboard hooking on Windows requires administrator privileges in certain environments.