# Input:  [3, 7, 2, 9, 4]
# Output: 9

def Max_Val(arr: list[int])->int:
    temp = arr[0]
    for x in arr:
        if x > temp:
            temp = x
    return temp

arr = [3,7,2,9,4]
output = Max_Val(arr)
print(output)

## Time Complexity: O(n)
## Space Complexity O(1)