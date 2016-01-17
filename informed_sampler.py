#!/usr/bin/env python
# encoding: utf-8
"""
informed_sampler.py
Created by Tao Gao on Dec 12, 2015
implementing the mcmc sampler with both global "informed proposal distribution"
and local gaussian distribution.
"""

import numpy as np
import pylab as pl

def informed_sampler(image, proposal_distribution, prior_distribution,
                    *mcmc_paramaters):
    """
    input:
        image: np.array (m*n*3)
        proposal_distribution: the distribution from k_classifier
        prior_distribution: the prior distribution of graphics paramaters
        mamc_paramaters: other paramaters for mcmc sampling
    output:
        distribution: paramatic as kernal density?? (a function))
    """
    pass


def main():
    pass

if __name__ == '__main__':
    main()

