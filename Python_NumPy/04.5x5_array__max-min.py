# Crea una matriz de 5x5 y calcula el valor maximo y minimo.

import numpy as np

x = np.random.rand((5,5))
print("Original Array:")
print(x) 

xmin, xmax = x.min(), x.max()
print("Minimum and Maximum Values:")
print(xmin, xmax)