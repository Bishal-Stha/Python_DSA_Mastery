# Input:  [3, 7, 2, 9, 4]
# Output: 7



def SecondMax(arr: list[int])->int:
    t1, t2 = float("-inf"),  float("-inf")
    for x in arr:
        if x > t1:
            t2 = t1
            t1 = x
        elif x > t2 and x != t1:
            t2 = x

    return t2
    
arr = [3, 7, 2, 9, 4]
arr2 = arr[::-1]
arr3 = [10, 1, 9, 8]

output = SecondMax(arr)
print(output)
print(SecondMax(arr2))
print(SecondMax(arr3))
"""
t1 = 3
t2 = 7
if (t1 < t2) the swap(t1,t2)
now, t1 > t2

i = 0
t1 = 3, t2 = 7 | swap(t1,t2) if t1 < t2

i = 1
t1 = 7, t2 = 3 | 

"""