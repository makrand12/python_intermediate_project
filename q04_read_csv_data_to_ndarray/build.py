# %load q04_read_csv_data_to_ndarray/build.py
# Default Imports
import numpy as np
path = './data/ipl_matches_small.csv'

# Enter code here
def read_csv_data_to_ndarray(path, dtype = np.float):
    array = np.genfromtxt(path, dtype=dtype, delimiter=',', skip_header=1)
    return array
read_csv_data_to_ndarray(path)


