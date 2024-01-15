import numpy as np

# Advantages of using Numpy arrays
one_dimensional_arr = np.array([10, 12])
print(one_dimensional_arr)

# How to create Numpy arrays
a = np.array([1, 2, 3])
print(a)

# Create an array with 3 integers, starting from the default integer 0.
b = np.arange(3)
print(b)

# Create an array that starts from the integer 1, ends at 20, incremented by 3.
c = np.arange(1, 20, 3)
print(c)

lin_spaced_arr = np.linspace(0, 100, 5)
print(lin_spaced_arr)

lin_spaced_arr_int = np.linspace(0, 100, 5, dtype=int)
print(lin_spaced_arr_int)

c_int = np.arange(1, 20, 3, dtype=int)
print(c_int)

b_float = np.arange(3, dtype=float)
print(b_float)

char_arr = np.array(['Welcome to Math for ML!'])
print(char_arr)
print(char_arr.dtype) # Prints the data type of the array