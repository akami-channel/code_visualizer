#!/bin/python

import os, sys
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from PIL import ImageOps
import string
import math
import random
import textwrap

import io 
import fileinput
import sys
import re


img = Image.new('RGB', (200, 100))
d = ImageDraw.Draw(img)
d.text((20, 20), 'Hello', fill=(255, 0, 0))
text_width, text_height = d.textsize('Hello')
s = io.BytesIO()
img.save('foo.png')
in_memory_file = s.getvalue()



print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))

# with open("data/data.html", 'r', encoding='utf-8') as file:
#     contents = file.read()

