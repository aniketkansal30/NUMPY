import numpy as np
import matplotlib.pyplot as plt
arr1=np.array([[1,2,3],[4,5,6]])
np.save('array1.npy',arr1)
loaded_arr1=np.load('array1.npy')
print(loaded_arr1)

try:
    logo=np.load('numpy-logo.npy')
    plt.figure(figsize=(10,5))
    plt.subplot(121)
    plt.imshow(logo)
    plt.title("Numpy Logo")
    plt.grid(False)
    plt.show()
    dark_logo=1-logo
    plt.subplot(122)
    plt.imshow(dark_logo)
    plt.title("Numpy Dark Logo")
    plt.grid(False)
    plt.show()
except FileNotFoundError:
    print("numpy logo file not found")