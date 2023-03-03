# Preprocessing

Data that we scrape using regions in Google Earth Engine return these giant diagrams. However, we want to crop these into the resolution of our desired dataset. This script is for doing that. 

## Setup 
This setup was inspired by Judy Hoffman's notes for setting up conda environments for Computer Vision.

1. Install Miniconda. It doesn’t matter whether you use Python 2 or 3 because we will create our own
environment that uses 3 anyways.
2. Open the terminal
    (a) On Windows: open the installed Conda prompt to run the command.
1. Navigate to the folder "proj3_configs" where you have the conda configuration files.
2. Create the conda environment for this project
    (a) On Windows: conda env create -f proj3_env_win.yml
3. Activate the newly created environment: use the command `conda activate research`
4. Use the command `python crop_data.py`