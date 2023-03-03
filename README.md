# StyleTerrain 

This project seeks to discover new ways to procedurally generate 2D height maps, textures, and slope maps that can then be leveraged to create 3D terrain. Traditionally, procedural creation of height maps is done by stacking varying wavelengths of perlin noise.

StyleGAN is a generative adverserial network created by NVidia that creates realistic images by training on a large dataset of existing images. It is known for having a high degree of control over the Style and content of the image, borrowing closely from style transfer literature. It leads to automatically learned and unsupervised separation of high-level attributes of images, and thus we thought it would work excellently for terrain generation.. 

Since the publication of StyleGAN, NVidia has released StyleGAN2, StyleGAN2-ADA, StyleGAN3. Each provides iterative improvements with different goals in mind. We modify these architectures and use certain features from each architecture in our own design.

In our project, we use StyleGAN's generative model to instead create Terrain. Terrain presents its own unique challenges when compared to other types of images. Specifically, even when training with a large and diverse dataset, it seems StyleGAN2-ADA consistently creates the same type of feature in a patch. We theorize this is due to it trying to find some common feature between all of the images when creating it's own novel images. We seek to improve this functionality as we explore procedural generation of terrain using GANs.  


### Figure 1: Repeated Terrain
![Repeated Features](/Documentation/repeated_terrain.jpg "Repeated Terrain")


# Directory Structure
```
StyleTerrain/                       - main repo
├─ Documentation/                   - documentation for the project
├─ styleterrain-ada-pytorch/        - repo for StyleGAN2 implementation of styleterrain
```
Since this project relies on git submodules, you can clone this repo by using `git clone --recurse-submodules`. If you want to update from the origin, you can also use `git pull --recurse-submodules`


# Collecting Data
Data for the project has been collected using Google Earth Engine. Below are snippets used to get data.

[Elevation Data](https://code.earthengine.google.com/36cca61d217d03cd4d600b42bb13a302)

# Google Colab Files
[SG2TERRAIN Google Colab](https://colab.research.google.com/drive/1Za6B0U355xvsaDbwVgnCDN9UVPHliNFw?usp=sharing)

# StyleGAN2

https://user-images.githubusercontent.com/34428034/221030059-efa8086f-7d0d-4051-a426-7f750e1e50e0.mp4

