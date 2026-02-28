# Hariharan R
# Program: NUMPY OPERATIONS : ARRAY CREATION, VECTORIZATION, BROADCASTING
# Date: 30-01-26
#(e) BROADCASTING WITH DIFFERENT SHAPES																									

import numpy as np   # Import NumPy																										
																									
arr1 = np.ones((4, 3))																									
arr2 = np.array([1, 2, 3])																									
																									
print("Add across rows:\n", arr1 + arr2)																									
																									
arr3 = np.array([[10], [20], [30], [40]])																									
print("Add across columns:\n", arr1 + arr3)																									
