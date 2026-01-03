import numpy as np
###
val = np.array([1,2,4,8,16],float)
print(val)

val = np.linspace(1,25,5)
print(val)

arr = np.arange(10,20,2)
print(arr)

ln = np.logspace(10,20,2)
print(ln)

zeroz = np.zeros(10)
onez = np.ones(5)
print(zeroz)
print(onez)

###
# Multidimensional Array
mulDArr0 = np.array(1)
print("0D array:\n",mulDArr0)

mulDArr1 = np.array([1,2,3,4,5])
print("1D array:\n",mulDArr1)

mulDArr2 = np.array([[1,2,3],[4,5,6]])
print("2D array:\n",mulDArr2)

mulDArr3 = np.array([
    [
        [1,2],
        [3,4]
    ],
    [
        [5,6],
        [7,8]
    ]
])
print("3D array:\n",mulDArr3)
