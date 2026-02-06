# Hariharan R
# Program: NUMPY OPERATIONS : ARRAY CREATION, VECTORIZATION, BROADCASTING
# Date: 30-01-26
#(g) VECTORIZED RANDOM WALK SIMULATION			

import numpy as np   # Import NumPy																																												
																									
# Generate random steps (+1 or -1)																									
steps = np.random.choice([1, -1], size=(5, 10))																									
																									
# Cumulative sum gives positions																									
positions = np.cumsum(steps, axis=1)	

print ("Steps Taken:\n",steps)																																																	
print("Positions (Cummative Sum):\n", positions)																									
print("Maximum position:", positions.max())																									
print("Minimum position:", positions.min())																									
