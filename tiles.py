from CONSTANTS import *
from PIL import Image
import numpy as np

def calc_tiles():
    
    #print(tile_paths[1])
    avg_colors = []
    for i in range(len(tile_paths)):
        if tile_paths[i][-4:] != ".jpg":
            continue
        else:
            img = Image.open("./tiles/" + tile_paths[i], "r")
            img.resize((tile_size, tile_size))
            avg_colors.append(np.array(img).mean(axis=0).mean(axis=0))

    return avg_colors

