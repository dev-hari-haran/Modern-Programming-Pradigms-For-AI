# Hariharan R
# Program: NUMPY OPERATIONS : ARRAY CREATION, VECTORIZATION, BROADCASTING
# Date: 30-01-26
#(b) Array creation with Zeros,ones,Empty
import numpy as np   # Import NumPy																																																		
																									
# 1D array of zeros																									
zeros_arr = np.zeros(10)																									
print("Zeros Array:", zeros_arr)																									
																									
# 2D array of ones with integer type																									
ones_arr = np.ones((3, 4), dtype=int)																									
print("Ones Array:\n", ones_arr)																									
																									
# Empty 3D array (may contain garbage values)																									
empty_arr = np.empty((2, 3, 2))																									
print("Empty Array:\n", empty_arr)																									
