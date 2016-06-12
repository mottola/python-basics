# IMPORT NUMPY
import numpy as np

# NUMPY !!!!! -- NUMERIC PYTHON
# NUMPY IS VERY USEFUL FOR ARRAYS AND DATA

# RECAP OF LISTS
# ______________
# POWERFUL
# COLLECTION OF VALUES
# HOLD DIFFERENT DATA TYPES
# CHANGE, ADD, REMOVE

# HOWEVER, FOR DATA SCIENCE:
# __________________________
# NEED MATHEMATICAL OPERATIONS OVER COLLECTIONS
# NEED SPEED!
# THIS IS A PROBLEM WITH LISTS

# NUMPY IS OUR SOLUTION
# ______________________
# CAN PERFORM CALCULATIONS OVER ENTIRE ARRAYS
# EASY AND FAST
# USE pip3 install numpy


height = [1.73, 1.68, 1.71, 1.89, 1.79]
weight = [65.4, 59.2, 63.6, 88.4, 68.7]

# USE NUMPY TO CHANGE HEIGHT LIST INTO ARRAY
np_height = np.array(height)
print(np_height)

# USE NUMPY TO CHANGE WEIGHT LIST INTO ARRAY
np_weight = np.array(weight)
print(np_weight)

# NOW I CAN PERFORM MATHEMATICAL OPERATIONS TO THE ARRAY
bmi = np_weight / np_height ** 2
print(bmi)

# NUMPY ARRAYS CAN CONTAIN ONLY ONE TYPE
# IF YOU PUT SEVERAL TYPES, TYPE COERCION WILL OCCUR

# NUMPY COMES WITH INS OWN METHODS

# BE CAREFUL, NUMPY METHODS DIFFER FROM THAT OF LISTS
# FOR EXAMPLE:
python_list = [1, 2, 3]

numpy_array = np.array([1, 2, 3])

print(python_list + python_list)  # CONCATENATES THE LISTS [1, 2, 3, 1, 2, 3]
print(numpy_array + numpy_array)  # COMBINES ARRAY INDICES [2, 4, 6]

print(bmi[1])  # PRINTS BMI AT INDEX 1

print(bmi > 23)  # PRINTS THE ARRAY WITH BOOLEAN CHECKS FOR CONDITION AT EACH INDEX
