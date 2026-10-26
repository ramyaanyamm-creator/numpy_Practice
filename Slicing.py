#Slicing
import numpy as np
arr=np.array([10,20,30,40,50,60])
print(arr[0:5:2])
print(arr[:3])
print(arr[2:])
print(arr[::-1])
print(arr[::2])
#slicing in 2D
a=np.array([
    [10,20,30,40],
    [20,40,60,80],
    [10,30,50,70]
])
print(a[1:3,1:3])
print(a[1:3,1:3])
