#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 13:36:25 2022

@author: leandre
"""

# Importing libraries
import matplotlib.pyplot as plt
from pathlib import Path
import skimage as sk
import skimage.io as skio
import skimage.transform as skt


plt.close('all')

# Defining path     ### To be modified ###
dirpath: Path = Path.cwd()


def encode(f_img2hide, f_support, save_filename=None):
    """
    Hides image with name 'f_img2hide' behind image with name 'f_support'

    Parameters :
        - f_img2hide : name of image to be hidden
        - f_support : name of support image
        - save_filename : name to give generated mixed image upon save
    Returns :
        mixed_img : image with 'f_img2hide' image hidden in 'f_support' image
    """
    # Extracting images
    path_img2hide = dirpath / f_img2hide
    path_support = dirpath / f_support

    img2hide = skio.imread(path_img2hide)
    support_img = skio.imread(path_support)

    # Displaying original images
    plt.figure(figsize=(12, 8))
    plt.subplot(1, 2, 1)
    plt.imshow(support_img)
    plt.title("Support Image")
    plt.axis('off')
    plt.subplot(1, 2, 2)
    plt.imshow(img2hide)
    plt.title("Image to hide")
    plt.axis('off')
    plt.tight_layout()
    plt.show()

    # Resizing support image if necessary
    if img2hide.shape != support_img.shape:
        support_img = skt.resize(support_img, img2hide.shape)
        support_img = sk.img_as_ubyte(support_img)

    # Mixed image computation
    mixed_img = (support_img & 240) | (img2hide >> 4)

    # Displaying mixed image
    plt.figure(figsize=(8, 8))
    plt.imshow(mixed_img)
    plt.title("Mixed image")
    plt.axis('off')

    # Saving mixed image
    if save_filename:
        save_filepath = dirpath / save_filename
        plt.imsave(save_filepath, mixed_img)

    return mixed_img


f_img2hide = r'img_to_hide.png'     # ### To be modified ###
f_support = r'support_img.png'      # ### To be modified ###
save_filename = "mixed_img.png"     # ### To be modified ###

mixed_img = encode(f_img2hide, f_support, save_filename)
