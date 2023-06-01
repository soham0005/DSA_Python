arr = [1,19,3,4,5,36]
# arr.clear()
print(arr)


# Swapping the elements of the array
[arr[0],arr[1]] = [arr[1],arr[0]]
print(arr)


# Max item
print(max(arr))

# max item in range 0:4
print(max(arr[:4]))

# Reversing the array
print(arr[::-1])

# Reversing the array using two pointers approach
def reverseArray(arr):
    start = 0
    end = len(arr) - 1
    
    while start < end:
        [arr[start],arr[end]] = [arr[end],arr[start]]
        start +=1 
        end -= 1
        
    print("Reversed Array is :",arr)
    
reverseArray([1,2,3,4,5,6,67,7,8]) 