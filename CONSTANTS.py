from os import listdir
from os.path import isfile, join

tile_size = 5
tile_paths = [f for f in listdir("./tiles") if isfile(join("./tiles", f))]