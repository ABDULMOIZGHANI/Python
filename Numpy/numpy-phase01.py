import numpy as np

# array = np.array([1,2,3,4,5])

# zeros array
zeros = np.zeros((2, 2))
print(zeros)

# unit matrices
ones = np.ones(6)
print(ones)

# Same number matrices
same = np.full((3, 3), 6)
print(same, "\n")

# Random matrices
random = np.random.random((2, 3))
print(random, "\n")

# Start End Steps ethod in array
arange = np.arange(0, 10, 2)  # Out Put ---> [0 2 4 6 8]
print(arange, "\n")

# Vectore Matrix Tensor
# vector is a !D matrix
vector = np.array([1, 2, 3, 4, 5])
print(vector, "\n")

# Matrix is a 2D matrix array
matrix = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(matrix, "\n")

# tensor is a multidimensional array (TPU) tensor processing unit
tensor = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(tensor, "\n")

# ARRAY PROPERTIES

arr = np.array([[1, 2], [3, 4]])

print("shape of array :", arr.shape)
print("Dimension of array :", arr.ndim)
print("Total no. of elements :", arr.size)
print("Data type :", arr.dtype)

# ARRAY RESHAPING
array_reshape = np.arange(12)
print("\n", array_reshape)

# reshaping the array
reshape = array_reshape.reshape((3, 4))
reshape2 = array_reshape.reshape((4, 3))
print("\n", reshape)
print("\n", reshape2)

# how to change the multidimensinal array into 1D
flat = reshape.flatten()
print("\n", flat)

ravel = reshape.ravel()
print(ravel) # ---> Copy of real array

# Transpose tthe array
transpose = reshape.T
print("\n", transpose)