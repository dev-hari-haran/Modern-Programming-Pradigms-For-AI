# Hariharan R
# Program: NUMPY OPERATIONS : ARRAY CREATION, VECTORIZATION, BROADCASTING
# Date: 30-01-26
#(f) VECTORIZED STATISTICS AND SORTING

import numpy as np   # Import NumPy	
																																																
rand_int = np.random.randint(1, 21, (3, 4))																									
print("Array:\n", rand_int)																									
																									
print("Mean (overall):", rand_int.mean())																									
print("Mean (axis=0):", rand_int.mean(axis=0))																									
print("Mean (axis=1):", rand_int.mean(axis=1))																									
																									
print("Std (overall):", rand_int.std())																									
print("Std (axis=0):", rand_int.std(axis=0))																									
print("Std (axis=1):", rand_int.std(axis=1))																									
																									
rand_int.sort()   # In-place sorting																									
print("Sorted Array:\n", rand_int)																									
