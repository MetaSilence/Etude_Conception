# -*- coding: utf-8 -*-
"""
Created on Fri Oct 31 11:23:53 2025

@author: nicol
"""

import numpy as np
import matplotlib.pyplot as plt

n_eau = 1.33
n_cell = 3.5
wav = np.arange(2, 22.01, 0.01)
nanoaxis = np.arange(200, 2201, 1)
irrad = (6.61e5 / (wav ** 5 * (np.exp(2484/(wav * 10 ** 2))-1)))

plt.plot(wav, irrad)

Gamma = (n_eau-n_cell)/(n_eau+n_cell)

T = 1 - Gamma**2

value = np.trapz(T*irrad, wav)

print(value)



