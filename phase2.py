# Numpy array operations
import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9])
print("Basic Slicing",arr[2:7])
print("With Step",arr[1:8:2])
print("Negative Indexing",arr[-3])
arr_2d=np.array([[[1,2,3],
                  [4,5,6],
                  [7,8,9]]])
print("Specific Element",arr_2d[0,1,2])
print("Entire Row",arr_2d[0,1])
print("Entire Column",arr_2d[0,:,1])

# SORTING
unsorted=np.array([1,2,35,8,2,4,69,7,6])
print("Sorted Array",np.sort(unsorted))
arr_2d_unsorted=np.array([[3,1],[1,2],[2,3]])
print("Sorted 2D array by column",np.sort(arr_2d_unsorted,axis=0))

# FILTER
numbers=np.array([i for i in range(1,11)])
print("Original Numbers:",numbers)
even_numbers=numbers[numbers%2==0]
print("Even Numbers:",even_numbers)
mask=numbers>5
print("Filter with mask",numbers[mask])
indices=([0,2,4])
print(numbers[indices])
condition_array=np.where(numbers>5,numbers*4,numbers)
print(condition_array)

# Adding and Removing Data
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
Combined=np.concatenate((arr1,arr2))
print(Combined)

# Array Compatibility
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
print("Array Compatibility",arr1.shape==arr2.shape)

# Adding row by vstack
original=np.array([[1,2],[3,4]])
new_row=np.array([5,6])
with_new_row=np.vstack((original,new_row))
print(with_new_row)

# Adding column by hstack
original=np.array([[1,2],[3,4]])
new_column=np.array([[5],[6]])
with_new_column=np.hstack((original,new_column))
print(with_new_column)