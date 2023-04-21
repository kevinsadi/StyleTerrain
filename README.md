# StyleTerrain 

StyleTerrain was a 1:1 project done in collaboration with Professor Greg Turk in the Spring of 2023. We build upon StyleGAN2 [Tero Kerras, et al.]. This project seeks to discover new ways to procedurally generate interconnected 2D height maps, textures, and slope maps that can then be leveraged to create infinite 3D terrain. Our main contributions include:

1. Ability to generate non-homogeneous content through manipulation of the constant 4x4x512 during training and generation
2. Modifying the architecture of the network to train on and produce high dimensional terrain vectors. These were formed by merging RGB data and elevation data into a single feature. This provides us with elevation and rgb data that are interdependent, but form a cohesive picture.
3. Combine deep features of multiple chunks of terrain to create cohesive and infinite terrain. We also explored using gradient descent on the w vectors used by the generator to create cohesive edges of terrain. 

# Running Locally
```
StyleTerrain/                       - main repo
├─ Documentation/                   - documentation for the project
├─ Preprocessing/                   - code used for preprocessing. look at readme for instructions to get environment setup
├─ styleterrain-ada-pytorch/        - repo for StyleGAN2 implementation of styleterrain
├─ SG2-Terrain.ipynb                - Google colab used to run the code for this project
```
Since this project relies on git submodules, you can clone this repo by using `git clone --recurse-submodules`. If you want to update from the origin, you can also use `git pull --recurse-submodules`. You could also simply work through the Google colab, which will clone the necessary repo for you.

## 0: Data Formation, Preprocessing, and Basic Training
Data for the project has been collected using Google Earth Engine. [Here](https://code.earthengine.google.com/36cca61d217d03cd4d600b42bb13a302) are the scripts that we used to collect our initial data. We trained our network from scratch by using 1000 images of 128 x 128 linked elevation and rgb data from the alps and various regions of the United States.

## 1: Create non-homogenous content
Unfortunately, we started to notice that our network would produce homogenous features. This was not what we wanted as we wanted to create general terrain from many regions. 
![Repeated Features](/Documentation/repeated_terrain.jpg "Repeated Terrain")

We were able to resolve this behavior by modifying the constant 4x4x512 data to be always random instead of learned. This created the variation in terrain we were hoping for. 

## 2: Allow High Dimensional Data 
At this point, we shifted our efforts towards 

## 3: Infinite Terrain
We were greatly inspired by the method used in [TileGAN](https://arxiv.org/abs/1904.12795).


