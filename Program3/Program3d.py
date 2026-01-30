# Hariharan R
# Program: NUMPY OPERATIONS : ARRAY CREATION, VECTORIZATION, BROADCASTING
# Date: 30-01-26
#(d) MASTER VECTORIZATION, UFUNCS & BROADCASTING

import numpy as np   # Import NumPy																							
# Random floating-point array between -5 and 5																									
np.random.seed(0)																									
rand_arr = np.random.uniform(-5, 5, (3, 5))																									
print("Original Array:\n", np.round(rand_arr, 3))																									
																									
# Unary ufuncs																									
print("Absolute:\n", np.round(np.abs(rand_arr), 3))																									
print("Square:\n", np.round(np.square(rand_arr), 3))																									
print("Square Root:\n", np.round(np.sqrt(np.abs(rand_arr)), 3))																									
print("Exponential:\n", np.round(np.exp(rand_arr), 3))																									
																									
# Replace values using np.where																									
clipped = np.where(rand_arr < 0, 0, rand_arr)																									
clipped = np.where(clipped > 3, 3, clipped)																									
print("After np.where clipping:\n", np.round(clipped, 3))																									
																									
# Scalar broadcasting																									
print("Add 10:\n", np.round(rand_arr + 10, 3))																								
																									
# Row-wise broadcasting																									
print("Multiply rows:\n", np.round(rand_arr * np.array([1, 2, 3]), 3))																									
																									
# Column-wise broadcasting																									
print("Multiply columns:\n", np.round(rand_arr * np.array([[10], [20], [30]]), 3))																									
																									
