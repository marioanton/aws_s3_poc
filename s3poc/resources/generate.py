#!/usr/bin/env python
from PIL import Image, ImageDraw
import os 

def generate_images():
    count = 0
    dir_path = os.path.dirname(os.path.realpath(__file__))
    while count < 2000:
        img = Image.new('RGB', (184, 64), color = 'red') # resize the images
        img.save('%s/images/pil_red%d.png'%(dir_path,count))
        count += 1
    print("%d images created"%(count))