#!/usr/bin/env python
# encoding: utf-8
"""
informed_sampler.py
Created by Tao Gao on Dec 12, 2015
"""

import numpy as np
import pylab as pl
import k_means as km
import informed_sampler as sp
import render as rd



def image_reconstruction(image, prior_distribution):
    """
    input:
        image: np.array (m*n*3)
        prior_distribution: the prior distribution of graphics paramaters
        (maybe a multi-var gaussian??)
    output:
        r_image:the reconstructed image;
        graphics_paramaters(numpy row vector): a vector of grahics paramaters
        that can synthesize the image by a graphics rendering process.
    """
    proposal_distribution = k_means_classification(image)
    g_paramaters = informed_sampler(image,
                                    proposal_distribution,
                                    prior_distribution,
                                    *mcmc_paramaters)
    r_image = render(g_paramaters) #TODO: a graphics function for rendering image;
    return r_iamge, g_paramaters

def main():
    pass

if __name__ == '__main__':
    main()

