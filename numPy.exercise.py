# array = list(range(10, 51))
# print(array)


import numpy as np

array = np.arange(10, 51)
print(array)



array = np.arange(10, 51)

max_value = np.max(array)
min_value = np.min(array)

print("Max:", max_value)
print("Min:", min_value)

print(array * 3)