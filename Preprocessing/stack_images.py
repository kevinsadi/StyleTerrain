"""
Authored: Kevin Sadi - 4.16.2023

Horizontally stacks images so that you can see what the images would look like if they were tiled. 
"""

import numpy as np
import os
from PIL import Image
import sys

################ FILE SETTINGS #########################

# THIS IS THE FOLDER THAT CONTAINS ALL THE FILES YOU WANT TO CONVERT
input_data_folder = "G:\My Drive\styleterrain\styleterrain-ada-pytorch\output\images\stitch"

file1 = 'preswap'
file2 = 'postswap'

output_data_folder = "output/rotate"

########################################################

# take list of elevation .npy files and create horizontal tilings of them. 
# One tiling for the rgb values and another tiling for the elevation values 
def stack_images_horizontally_no_overlap(elevation_images, rgb_images):
    np_elevation_imgs = np.hstack(elevation_images)
    np_rgb_imgs = np.hstack(rgb_images)
    
    elevation_imgs_comb = Image.fromarray(np_elevation_imgs)
    elevation_imgs_comb.save(os.path.join(output_data_folder, 'elevations_tiled.png'))   

    rgb_imgs_comb = Image.fromarray(np_rgb_imgs)
    rgb_imgs_comb.save(os.path.join(output_data_folder, 'rgbs_tiled.png'))   

"""
Given input data folder, create a list for elevation images and a list for rgb images
The lists contain PIL `Image`s.
"""
def split_images(input_data_folder):
    elevation_images = []
    rgb_images = []
    for file in os.listdir(input_data_folder):
        file_directory = os.path.join(input_data_folder, file)

        merged_data = np.squeeze(np.load(file_directory))

        elevation_data = merged_data[:, :, :1]
        rgb_data = merged_data[:, :, 1:4]

        elevation_image = Image.fromarray(np.squeeze(elevation_data.astype(np.uint8)), mode='L')
        rgb_image = Image.fromarray(rgb_data).convert('RGB')

        elevation_images.append(elevation_image)
        rgb_images.append(rgb_image)
    return (elevation_images, rgb_images)


if __name__ == "__main__":
    elevation_images, rgb_images = split_images(input_data_folder)
    stack_images_horizontally_no_overlap(elevation_images, rgb_images)
