# clipocr

Replace an image containing text on the system clipboard with the text itself.

Tested only on MacOS, but should work across platforms.

Thanks to Google's excellent [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) software, the wondrous and powerful [Pillow](https://python-pillow.org/), [Pyperclip](https://github.com/asweigart/pyperclip), and [Python Tesseract](https://github.com/madmaze/pytesseract) libraries, as well as the beautiful simplicity of the Python language itself, clipocr's source code is substantially shorter than this README file.

## Installation

1. Install the tesseract OCR engine. On MacOS, assuming you have homebrew installed:

```bash
brew install tesseract
```

2. Clone the clipocr git repo and enter the project directory:
```bash
git clone https://github.com/benglazer/clipocr.git
cd clipocr
```

3. (optional) Create a virtualenv to isolate clipocr's environment. Assuming you have [pyenv](https://github.com/pyenv/pyenv) with [virtualenv support](https://github.com/pyenv/pyenv-virtualenv) already installed:
```bash
pyenv virtualenv clipocr
pyenv local clipocr
```

4. From the project directory, install Python dependencies:
```bash
pip install -r requirements.txt
```

### MacOS shortcut assignment

One convenient way to access `clipocr` is to attach it to a keyboard shortcut. To do this on MacOS, you can combine Automator with Keyboard Shortcuts, both built into MacOS.

You must first install `clipocr` and its dependencies as described above.

**Step 1: Create a Quick Action in Automator.**

1. Open Automator.
2. Select Quick Action from the New Workflow menu that appears on load.
3. Set "Workflow receives current" to "no input".
4. Drag "Run Shell Script" from the Actions library to the workflow stage.
5. With /bin/zsh (default) selected as your Shell, enter the command to run clipocr in the command textarea. You'll want to adapt this to your details, but in my case (username "benglazer", pyenv-generated virtualenv "clipocr"), this looks like:
```bash
PATH=/opt/homebrew/bin:$PATH /Users/benglazer/.pyenv/versions/clipocr/bin/python /Users/benglazer/dev/benglazer/clipocr/clipocr.py
```
6. Save the Quick Action and name it "clipocr".

**Step 2: Attach the new Quick Action to a Keyboard Shortcut.**

1. Open System Settings.
2. Navigate to the Keyboard section.
3. Click the "Keyboard Shortcuts..." button.
4. Locate "clipocr" under Services->General.
5. Select the checkbox on the left.
6. Double click "none" (or existing shortcut) to its right supply a keyboard shortcut; I use ⌃⌥⇧⌘O (ctrl-alt-shift-meta-O).

## Usage

Simply copy an image containing text to your system clipboard and run:
```bash
clipocr.py
```
... or use the shortcut, if you created one.

After executing the script, an image on the clipboard will be replaced with text extracted from that image. If an image was not found, an error is printed.
