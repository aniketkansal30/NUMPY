import numpy as np

py_list = [1, 2, 3]
np_array = np.array([1, 2, 3])

print("Python list multiplication:", py_list * 2)
print("NumPy array multiplication:", np_array * 2)

# Creating array from scratch
zeros=np.zeros((3,4))
print("zeros array:\n",zeros)
ones=np.ones((3,4))
print("ones array:\n",ones)
full=np.full((3,4),5)
print("full array:\n",full)
random=np.random.random((3,4))
print("random array:\n",random)
sequence=np.arange(0,11,2)
print("sequence array:\n",sequence)

# Vector, matrix, tensor
vector=np.array([1,2,3])
print("Vector:",vector)
matrix=np.array([[1,2,3],
                [4,5,6]])
print("Matrix:",matrix)
tensor=np.array([[[1,2],[3,4],
                [5,6],[7,8]]]) #multi-dimensional array
print("Tensor:",tensor)

# Array Properties
arr=np.array([[1,2,3],[4,5,6]])
print("Shape",arr.shape)
print("Dimension",arr.ndim)
print("Size",arr.size)
print("DType",arr.dtype)

# Array Reshaping
arr=np.arange(12)
print("Original array",arr)
Reshaped=arr.reshape((3,4))
print("\n Reshaped array",Reshaped)
# Transpose
transpose=Reshaped.T
print("\n Transpose array",transpose)