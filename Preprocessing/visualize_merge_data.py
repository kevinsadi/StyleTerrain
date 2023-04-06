# Authored by Kevin Sadi
# This script's primary purpose is to take merged data and split it up again. Also to visualize that merged data.

import numpy as np
import os
from PIL import Image

################ FILE SETTINGS #########################

input_data_folder = "input"
input_image_name = 'fakes000352.npy'

output_data_folder = "output/split_files"

################ REST OF THE COE ######################

merged_data = np.load(os.path.join(input_data_folder, input_image_name))

elevation_data = merged_data[:, :, :1]
rgb_data = merged_data[:, :, 1:4]

print(f"the elevation data size: {elevation_data.shape}")
print(f"the elevation data size: {rgb_data.shape}")

os.makedirs(output_data_folder, exist_ok=True)

elevation_image = Image.fromarray(np.squeeze(elevation_data.astype(np.uint8)), mode='L')
rgb_image = Image.fromarray(rgb_data).convert('RGB')

elevation_image.save(os.path.join(output_data_folder, "elevation.png"))
rgb_image.save(os.path.join(output_data_folder, "rgb.png"))
