# Introduction
Implementation of the Bit Plane Complexity Segmentation algorithm to hide data in images by Eiji Kawaguchi and Richard O.
The algorithm replaces the complex regions of the image (that the eye cannot make a sense of anyway) with the hidden data. Enabling a **storage capacity of 60-40%** of the original image size, which is significantly higher than other steganography techniques such as LSB (Least Significant Bit).

## Coding style
The code is fully object oriented, here is a description of the main classes :

- **HostImage(BW/Color)** : A vessel image, in black and white or in color.
- **BitPlane64(ConjugateBit)** : An 8*8 block of pixel.
- **SecretData** : The data to hide.
- **Encoder** : His goal is to hide the data into the vessel.
- **Decoder** : His goal is to retrieve the data from the vessel.
