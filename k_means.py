#!/usr/bin/env python
# encoding: utf-8
"""
k_means.py
Created by Tao Gao on Dec 12, 2015
implementating the functions associated with k_means classification
(1) training:
    taking a large amount of synthesized image and do unsupervised classification
(2) classification:
    taking a new image, output its classification and associated class paramaters
"""

import numpy as np

def k_means_training(images, num_class):
    """
    input:
        images: a list of synthesized images (from render)
    output:
        class_dict: a dictionary of class paramaters.
           key: class index
           value: distribution function
           example: distribution = class_dict[class_index]
    """
    pass

def k_means_classification(k_classifier, image):
    """
    input:
        image: np.array (m*n*3)
    output:
        distribution: paramatic as kernal density?? (a function))
    """
    return k_classifier(image)
    #TODO: figure out what is the right representation of the "distribution" ?

def main():
    pass

if __name__ == '__main__':
    main()

