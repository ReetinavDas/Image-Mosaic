from tiles import calc_tiles
from CONSTANTS import *
from pixelate import pixelate
from matching import match
from PIL import Image

def main():
    colors = calc_tiles()

    input_photo = "input_photos/mountain.jpg"

    starting = Image.open(input_photo)

    pixeled = pixelate(input_photo)

    mosaic = match(pixeled, colors)

    im_mos = Image.new("RGB", starting.size)

    for i in range(pixeled.size[0]):
        for j in range(pixeled.size[1]):
            x, y = i*tile_size, j*tile_size

            index = mosaic[i, j]

            im_mos.paste(Image.open("tiles/" + tile_paths[index]).resize((tile_size, tile_size)), (x,y,x+tile_size,y+tile_size))

    im_mos.show()


main()
