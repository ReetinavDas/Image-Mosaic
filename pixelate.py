from turtle import width
from PIL import Image
from CONSTANTS import tile_size
import numpy as np

def pixelate(main_image):
    im_mos = Image.open(main_image)

    width = int(np.round(im_mos.size[0]/tile_size))
    length = int(np.round(im_mos.size[1]/tile_size))

    pixeled = im_mos.resize((width, length))

    return pixeled