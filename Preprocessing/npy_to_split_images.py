# Authored by Kevin Sadi
# This script's primary purpose is to take merged data and split it up again. Also to visualize that merged data.

import numpy as np
import os
from PIL import Image
import sys

################ FILE SETTINGS #########################

# THIS IS THE FOLDER THAT CONTAINS ALL THE FILES YOU WANT TO CONVERT
input_data_folder = "G:\My Drive\styleterrain\styleterrain-ada-pytorch\output\images\stitch"

output_data_folder = "output/rotate"

################ REST OF THE CODE ######################

#input_data = sys.argv[1]

for file in os.listdir(input_data_folder):
    print(f'Converting {os.path.join(input_data_folder, file)}')
    file_directory = os.path.join(input_data_folder, file)

    #merged_data = np.load(os.path.join(input_data_folder, input_image_name))
    merged_data = np.squeeze(np.load(file_directory))

    elevation_data = merged_data[:, :, :1]
    rgb_data = merged_data[:, :, 1:4]

    print(f"the merged data size: {merged_data.shape}")
    print(f"the elevation data size: {elevation_data.shape}")
    print(f"the rgb data size: {rgb_data.shape}")

    os.makedirs(output_data_folder, exist_ok=True)

    elevation_image = Image.fromarray(np.squeeze(elevation_data.astype(np.uint8)), mode='L')
    rgb_image = Image.fromarray(rgb_data).convert('RGB')

    elevation_image.save(os.path.join(output_data_folder, f'{file}_elevation.png'))
    rgb_image.save(os.path.join(output_data_folder, f'{file}_rgb.png'))
