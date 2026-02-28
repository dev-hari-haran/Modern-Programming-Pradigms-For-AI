
# Hariharan R
# Program: NUMPY OPERATIONS : ARRAY CREATION, VECTORIZATION, BROADCASTING
# Date: 30-01-26
#(h) IMPORTANT MATHEMATICAL OPERATIONS		
import numpy as np   # Import NumPy	
																																																																								
np.random.seed(0)																									
data = np.random.uniform(-10, 10, (4, 6))																									
print("Original Data:\n", np.round(data, 3))																									
																									
# Unary functions																									
print("abs:\n", np.round(np.abs(data), 3))																									
print("sqrt:\n", np.round(np.sqrt(np.abs(data)), 3))																									
print("square:\n", np.round(np.square(data), 3))																									
print("exp:\n", np.round(np.exp(data), 3))																									
print("log:\n", np.round(np.log(np.abs(data) + 1), 3))																									
print("log10:\n", np.round(np.log10(np.abs(data) + 1), 3))																									
print("sign:\n", np.sign(data))																								
																									
# Trigonometric																									
print("sin:\n", np.round(np.sin(data), 3))																									
print("cos:\n", np.round(np.cos(data), 3))																									
print("tan:\n", np.round(np.tan(data), 3))																									
																									
# Hyperbolic																									
print("sinh:\n", np.round(np.sinh(data), 3))																									
print("cosh:\n", np.round(np.cosh(data), 3))																									
print("tanh:\n", np.round(np.tanh(data), 3))																									
																									
# Rounding																									
print("ceil:\n", np.ceil(data))																									
print("floor:\n", np.floor(data))																									
print("rint:\n", np.rint(data))																									
print("trunc:\n", np.trunc(data))																									
																									
# Binary operations																									
print("add:\n", data + 2)																									
print("subtract:\n", data - 2)																									
print("multiply:\n", data * 2)																									
print("divide:\n", data / 2)																									
print("power:\n", data ** 2)																									
print("mod:\n", np.mod(data, 2))																									
print("maximum:\n", np.maximum(data, 5))																									
print("minimum:\n", np.minimum(data, -5))																									
																									
# Statistics																									
print("sum:", data.sum())																									
print("prod:", data.prod())																									
print("cumsum:\n", np.cumsum(data))																									
print("cumprod:\n", np.cumprod(data))																									
																									
# Comparisons																									
print("greater than 0:\n", data > 0)																									
print("less than 0:\n", data < 0)																									
print("equal to 0:\n", data == 0)																									
print("not equal to 0:\n", data != 0)																									
																									
