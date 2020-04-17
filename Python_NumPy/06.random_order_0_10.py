#Ordena aleatoriamente numeros entre 0-10
import numpy as np

x = np.arange(10)
np.random.shuffle(x)
print(x)
print("Same result using permutation():")
print(np.random.permutation(10))