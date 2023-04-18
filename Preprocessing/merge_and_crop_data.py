from PIL import Image
import numpy as np
import os
Image.MAX_IMAGE_PIXELS = 962986000

################ FILE SETTINGS #########################
input_data_folder_location = "large_data/merge"
elevation_image_name = "Elevation_Data_1.tif"
satellite_image_name = "RGB_Sattelite_Data_But_Cute_and_Quirky.tif"
output_resolution = 128

output_name = "elevation"
output_dir = 'output/npy_files'

################ REST OF THE COE ######################

"""
# This file takes in two images with the same width and height
# it then crops the data into a dimension requested, but also combines the images to create images with more than 3 channels
# This is used to take elevation data and rgb satellite data taken from the same region and create trainable .npy files from it
"""

# combine images

elevation_image = Image.open(os.path.join(input_data_folder_location, elevation_image_name))
satellite_image = Image.open(os.path.join(input_data_folder_location, satellite_image_name))
try:
    assert elevation_image.size == satellite_image.size, "input images do not have the same width and height"
except AssertionError as e:
    print(e)
width, height = elevation_image.size

np_elevation = np.asarray(elevation_image)
np_elevation = np.expand_dims(np_elevation, axis=2)
np_rgb = np.asarray(satellite_image)
np_high_dim_data = np.append(np_elevation, np_rgb, axis = 2)

print(f"combined_image shape is : {np_high_dim_data.shape}")

# crop combined images
itr = 0
pad = '0'
len_padding = 8
os.makedirs(output_dir, exist_ok=True)

for i in range(0, width - output_resolution, output_resolution):
    for j in range(0, height - output_resolution, output_resolution):
        box = (i, j, i + output_resolution, j + output_resolution)
        cropped_img = np_high_dim_data[i:i+output_resolution, j:j+output_resolution, :]
        filename = f'{output_name}_{itr:{pad}{len_padding}}.npy' # give file name some padding
        print(filename)
        np.save(os.path.join(output_dir, filename), cropped_img)
        itr = itr + 1
