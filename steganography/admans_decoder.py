#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 19:53:01 2022

@author: leandre
"""

# Importing libraries
import matplotlib.pyplot as plt
from pathlib import Path
import skimage.io as skio

# Defining path     ### To be modified ###
dirpath: Path = Path.cwd()


def decoder(f_mixed):
    """
    Extracts hidden image from mixed image with name 'f_mixed'.

    Parameters :
        - f_mixed : name of mixed image
    Returns :
        decoded : extracted image
    """

    # Loading image
    path_mixed = dirpath / f_mixed
    mixed = skio.imread(path_mixed)

    # Displaying encoded image
    plt.figure(figsize=(8, 8))
    plt.imshow(mixed)
    plt.title("Encoded image")
    plt.axis('off')

    # Decoding image
    decoded = (mixed & 15) << 4

    # Displaying decoded image
    plt.figure(figsize=(12, 12))
    plt.imshow(decoded), plt.title("Decoded image")
    plt.axis('off')

    return decoded


f_mixed = "mixed_img.png"
decoder(f_mixed)
