import numpy as np

x = np.random.rand(10, 4)
print("Original array: ")
print(x)

y= x[:5, :]
print("First 5 rows of the above array:")
print(y)