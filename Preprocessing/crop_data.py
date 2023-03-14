from PIL import Image
import numpy as np
import os

Image.MAX_IMAGE_PIXELS = 962986000

large_image = Image.open("large_data/geragh.tif")

width, height = large_image.size
output_resolution = 128

np_image = np.asarray(large_image)
print(np_image.shape)

itr = 0
pad = '0'
len_padding = 8

file_stem = "elevation"
output_dir = 'output/npy_files'
os.makedirs(output_dir, exist_ok=True)

for i in range(0, width - output_resolution, output_resolution):
    for j in range(0, height - output_resolution, output_resolution):
        box = (i, j, i + output_resolution, j + output_resolution)
        cropped_img = large_image.crop(box)
        filename = f'{file_stem}_{itr:{pad}{len_padding}}.npy' # give file name some padding
        print(filename)
        cropped_img.save(os.path.join(output_dir, filename))
        itr = itr + 1