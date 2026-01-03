import array

from numpy import integer, ones

Integers = array.array('I',[1,2,3,4,5])
for i in range(0,len(Integers)):
    print(Integers[i],end=" ")
print("\n")

Floats = array.array('d',[1.4,2.44, 5.35,2,5.4,9,4.9])
for d in Floats:
    print(d,end=", ")

copyArray = array.array(Integers.typecode, [x for x in Integers])
print("\nPrinting contents of Copy Array:")
for c in copyArray:
    print(c, end=" ")

print(" ")
copyArray.pop(2)
for c in copyArray:
    print(c, end=" ")

copyArray.pop() # if index is not given, it applies Stack ADT.
print(copyArray)
copyArray.remove(1)
print(copyArray)


### Slicing
# f = Float[start index: end index]
i = Integers[1:4] # start include hunxa ending ko index include hudaina.
print(i)

y = Integers[1:-2] #
print(y)

rev = Integers[::-1] # reverses the string.
print(rev)

### 
arr = array.array('i',[])
# num = int(input("Enter total no of values: "))
# for i in range(num):
#     arr.append(int(input("enter next input: ")))

# print(arr)

### search in element.
arr = array.array('i',[10,15,20,25,30,35,40,45,50])
idx = arr.index(25)
print(idx)

# if not in array.
# print(arr.index(55))

