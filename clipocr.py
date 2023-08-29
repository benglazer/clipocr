#!/usr/bin/env python

import sys

import pytesseract
import pyperclip
from PIL import ImageGrab


# Check whether clipboard contains an image
image = ImageGrab.grabclipboard()
if image is None:
    print("Clipboard does not contain an image")
    sys.exit(1)

# Perform OCR on the image
text = pytesseract.image_to_string(image)

# Replace image in clipboard with OCR output
pyperclip.copy(text)
