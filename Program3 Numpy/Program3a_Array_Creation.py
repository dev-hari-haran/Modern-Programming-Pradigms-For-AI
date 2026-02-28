# Hariharan R
# Program: NUMPY OPERATIONS : ARRAY CREATION, VECTORIZATION, BROADCASTING
# Date: 30-01-26
# #(a) Basic array from the List																								
																									
import numpy as np   # Import NumPy																									
																																													
# Create 1D array from list																									
arr1 = np.array([3, 14, 4, 2, 3])																									
print("1D Array:", arr1)																									
																									
# Create 2D array from nested lists																									
arr2 = np.array([[1, 2, 3], [4, 5, 6]])																									
print("2D Array:\n", arr2)																									
																									
# Print properties																									
print("Shape:", arr2.shape)																									
print("Dimensions:", arr2.ndim)																									
print("Data type:", arr2.dtype)																									
																									
