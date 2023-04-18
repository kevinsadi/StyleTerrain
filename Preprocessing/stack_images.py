"""
Authored: Kevin Sadi - 4.16.2023

Horizontally stacks images so that you can see what the images would look like if they were tiled. 
"""

import numpy as np
import os
from PIL import Image
import sys

################ FILE SETTINGS #########################

# This is the folder that contains the elevation .pkl files that you want to stitch
input_data_folder = "G:\My Drive\styleterrain\styleterrain-ada-pytorch\output\images\grad_desc"
output_data_folder = "output/grad_desc"

########################################################

# take list of elevation .npy files and create horizontal tilings of them. 
# One tiling for the rgb values and another tiling for the elevation values 
def stack_images_horizontally_no_overlap(elevation_images, rgb_images):
    np_elevation_imgs = np.hstack(elevation_images)
    np_rgb_imgs = np.hstack(rgb_images)
    
    os.makedirs(output_data_folder, exist_ok=True)

    elevation_imgs_comb = Image.fromarray(np_elevation_imgs)
    elevation_imgs_comb.save(os.path.join(output_data_folder, 'elevations_tiled.png'))   

    rgb_imgs_comb = Image.fromarray(np_rgb_imgs)
    rgb_imgs_comb.save(os.path.join(output_data_folder, 'rgbs_tiled.png'))   

# take list of elevation .npy files and create horizontal tilings of them. 
# One tiling for the rgb values and another tiling for the elevation values 
def stack_two_images_horizontally_with_overlap(elevation_images, rgb_images):
    midpoint = elevation_images[0].size[1] // 2

    elevation_left_image = np.asarray(elevation_images[0])[:, :midpoint]
    elevation_right_image = np.asarray(elevation_images[1])[:, midpoint:]
    rgb_left_image = np.asarray(rgb_images[0])[:, :midpoint]
    rgb_right_image = np.asarray(rgb_images[1])[:, midpoint:]
    
    np_elevation_imgs = np.hstack((elevation_left_image, elevation_right_image))

    np_rgb_imgs = np.hstack((rgb_left_image, rgb_right_image))
    
    os.makedirs(output_data_folder, exist_ok=True)

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
    #stack_images_horizontally_no_overlap(elevation_images, rgb_images)
    stack_two_images_horizontally_with_overlap(elevation_images, rgb_images)