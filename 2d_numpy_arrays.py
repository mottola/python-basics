# 2D Numpy Arrays

import numpy as np

np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])

np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])

type(np_height)
np.ndarray  # ndarray = N-dimensional array

type(np_weight)
np.ndarray

# CREATE A 2D ARRAY
np_2d = np.array([[1.73, 1.68, 1.71, 1.89, 1.79],
                  [65.4, 59.2, 63.6, 88.4, 68.7]])

print(np_2d)

print(np_2d.shape)  # SHOWS ARRAY SHAPE IN THE FORM (ROWS, COLUMNS)

# REMEMBER, THE ARRAYS CAN ONLY BE OF ONE TYPE, IF YOU ADD A NUMBER AS A STRING
# PYTHON WILL COERCE THE REST OF THE DATA INTO STRINGS AS WELL

# SUBSETTING
print(np_2d[0, 2])  # PRINTS DATA AT (ROW[0], COLUMN[2])

print(np_2d[:, 1:3])  # ALL ROWS, BUT ONLY COLUMNS[1-3]

print(np_2d[1, :])  # ALL COLUMNS IN ROW 1


