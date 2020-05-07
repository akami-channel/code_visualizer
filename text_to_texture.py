import os, sys
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from PIL import ImageOps
import string
import math
import random
import textwrap

def text_on_image(outpath, text, index):
    #Define x and y for the text start
    y_text = 15
    x_text = random.randint(5, 50)
    random_width = 40 #(not so random...)

    #The line below wrap your text in lines based on width
    lines = textwrap.wrap(text, width = random_width)
    img = Image.new('RGB', (512, 512), (255, 255, 255))
    font_size = random.randint(12,17)
    draw = ImageDraw.Draw(img)
    average_font_size = 0

    for i in range(0, len(lines)):
        random_font_size = 1
        random_space = random.randint(0,1)
        change_font_size = random.randint(0,1)

        #All the modulo operations is just cheap random cases
        #To create some variation on the font size or spaces
        if change_font_size and i%3 == 0:
            random_font_size = random.uniform(0.7,1.5)
            font_size = int(font_size * random_font_size)
        if random_space and i%2 == 0:
            lines[i] = " "* 30
        
        #Loads the font
        #font = ImageFont.truetype("FONTNAME.ttf", font_size)
        #font = ImageFont.truetype("monospace.ttf", font_size)
        width, height = font.getsize(lines[i])
        #Draws the text on the image
        draw.text((x_text,y_text), lines[i], font=font, fill = (0, 0, 0))
        y_text += height
        average_font_size += font_size

    scratch_font_size = (average_font_size/(len(lines)+1))*2
    random_scratch = random.randint(0, 1)

    #Creates some borders around the text and saves image
    img = ImageOps.expand(img, border=20, fill='white')
    img.save('%sT_handtext_%s.jpg' %(outpath, index))

#Main loop. I am generating a string using random on the ascii letters, plus some spaces.
#Then I pass the string and the path to the main function.
for i in range(0,10):
    spaces_mult = random.randint(3, 20)
    text_on_image('sources/text_textures/', ''.join(random.choice(string.ascii_letters + spaces_mult*' ' + '\n') for _ in range(600)),i)

