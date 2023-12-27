import imp
from CONSTANTS import tile_paths
from scipy import spatial
import numpy as np
from PIL import Image

def match(pixelated, colors):

    tree = spatial.KDTree(colors)

    matching = np.zeros((pixelated.size[0], pixelated.size[1]), dtype = np.uint32)

    for i in range(pixelated.size[0]):
        for j in range(pixelated.size[1]):
            pixel = pixelated.getpixel((i,j))
            match = tree.query(pixel)
            matching[i,j] = match[1]

    return matching
