#!/usr/bin/env python
# encoding: utf-8
"""
render.py
Created by Tao Gao on Dec 12, 2015
This is the graphics engine for rendering images given paramatres
"""
#TODO: find a python graphics engine for syntehzing images!!!

import os
import numpy as np

curr_dir = os.getcwd() #get the current working directory

# class graphics_engine():
#     def __init__(self, openv_draw):
#         self.draw = opencv_draw
#
#     def __call__(self, paramaters):
#         return self.draw(image)
#
# engien = graphics_engine(paramater)
# engien(image)


def draw(paramaters, engine, save=False, show=False, path=None):
    """
    input:
        paramaters: a vector of graphcis paramaters
        engine: a graphic engien that can synthesize an image given paramaters
    return:
        r_image: a rendered image
    """

def synthesize_training_images(prior_distribution,
                               engine,
                               num_images=10000,
                               path=curr_dir,
                               prefix="training_image"):
    for i in range(num_images):
        paramater = sample_from_prior_distribution()
        #TODO: implement this sampling function
        image_name = os.path.join(path, "_".join(prefix, str(i), ".png"))
        draw(paramater,engine,save=True, path=image_name)


def main():
    pass

if __name__ == '__main__':
    main()

