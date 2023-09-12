# clipocr

Replace an image containing text on the system clipboard with the text itself.

Tested only on MacOS, but should work across platforms.

Thanks to the wondrous and powerful [Pillow](https://python-pillow.org/), [Python Tesseract](https://github.com/madmaze/pytesseract), and [Pyperclip](https://github.com/asweigart/pyperclip) libraries, as well as the beautiful simplicity of the Python language itself, clipocr's source code is shorter than this README file.

## Installation

1. Install the tesseract OCR engine. On MacOS, assuming you have homebrew installed:

```zsh
brew install tesseract
```

2. Clone the clipocr git repo and enter the project directory:
```zsh
git clone https://github.com/benglazer/clipocr.git
cd clipocr
```

3. (optional) Create a virtualenv to isolate clipocr's environment. Assuming you have [pyenv](https://github.com/pyenv/pyenv) with [virtualenv support](https://github.com/pyenv/pyenv-virtualenv) already installed:
```zsh
pyenv virtualenv clipocr
pyenv local clipocr
```

4. From the project directory, install dependencies:
```zsh
pip install -r requirements.txt
```

## Usage

Simply copy an image containing text to your system clipboard and run:
```zsh
clipocr.py
```

After executing the script, an image on the clipboard will be replaced with text extracted from that image. If an image was not found, an error is printed.
