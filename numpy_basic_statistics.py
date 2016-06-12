# BASIC STATISTICS

# DATA ANALYSIS
# _______________
# GET TO KNOW YOUR DATA
# LITTLE DATA -> SIMPLY LOOK AT IT
# BIG DATA -> ???

# NUMPY HAS FRIENDLY STATISTICAL FUNCTIONS SUCH AS:
# _________________________________________________
# np.mean(), np.median(), np.corrcoef() to check for correlations
# np.std() for standard deviation, np.sum(), np.sort()

# NUMPY'S FUNCTIONS ARE MUCH FASTER THAN THE PYTHON EQUIVALENTS

# GENERATING DUMMY/SAMPLE DATA WITH NUMPY
import numpy as np

# GENERATE RANDOM HEIGHTS
height = np.round(np.random.normal(1.75, 0.20, 5000), 2)
# the above samples two random distributions 5000 times
# 1.75 - distribution mean
# 0.20 - distribution standard deviation
# 5000 - number of samples

# GENERATE RANDOM WEIGHTS
weight = np.round(np.random.normal(60.32, 15, 5000), 2)
# the above samples two random distributions 5000 times
# 60.32 - distribution mean
# 15 - distribution standard deviation
# 5000 - number of samples

# COMBINE RANDOM SAMPLES INTO TWO COLUMNS
np_city = np.column_stack((height, weight))


# PRACTICE WITH NUMPY ARRAYS
np_height = np_city[:, 0]  # PULLS OFF COLUMN OF ALL HEIGHTS
print(np.mean(np_height))  # PRINT MEAN HEIGHT
print(np.median(np_height))  # PRINT MEDIAN HEIGHT
print(np.std(np_height))  # PRINT STANDARD DEVIATION OF HEIGHT
print(np.corrcoef(np_city[:, 0], np_city[:, 1]))  # PRINT CORRELATIONS

