# Properties of nd arrays
import numpy as np
a=np.array([10,20,30])
b=np.array([
    [10,20,30],
    [40,30,50]
])
c=np.array([
    [
        [10,20,30,40],
        [30,20,40,50],
        [10,20.90,30,40]
    ],
    [
        [10,30,40,50],
        [20,40,10,30],
        [50,60,80,90]
    ]
])

#1.ndim
print(">>>>>>The Dimentions<<<<<<<")
print(a.ndim)
print(b.ndim)
print(c.ndim)

#2.shape
print(">>>>>>>Size of Dimentions<<<<<<<")
print(a.shape)
print(b.shape)
print(c.shape)

#3.size
print(">>>>>>>>>Number of Elements<<<<<<<<")
print(a.size)
print(b.size)
print(c.size)

#4.dtype
print(">>>>>>>>>>Datatype of Elements<<<<<<<<<<<")
print(a.dtype)
print(b.dtype)
print(c.dtype)

#5.nbytes
print(">>>>>>>>>Storage<<<<<<<<<")
print(a.nbytes)
print(b.nbytes)
print(c.nbytes)

#6.itemsize
print(">>>>>>>>>>Memory<<<<<<<<<")
print(a.itemsize)
print(b.itemsize)
print(c.itemsize)
