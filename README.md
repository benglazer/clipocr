# clipocr

Replace an image containing text on the system clipboard with the text itself.

Tested only on MacOS, but should work across platforms.

## Installation

Install dependencies via:
```commandline
pip install -r requirements.txt
```

## Usage

Simply copy an image containing text to your system clipboard and run:
```commandline
clipocr.py
```

After running that script, an image on the clipboard will be replaced with text extracted from that image. If an image was not found, an error is printed.

Thanks to the wondrous and powerful [Pillow](https://python-pillow.org/), [Python Tesseract](https://github.com/madmaze/pytesseract), and [Pyperclip](https://github.com/asweigart/pyperclip) libraries, as well as the beautiful simplicity of the Python language itself, clipocr's source code is shorter than this README file.
