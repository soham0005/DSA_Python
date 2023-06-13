# Sinking Sort or Exchange Sort.
# Adjacent Elements are compared and Swapped
# After Every Iteration, Max Element is placed in its position

def bubble_sort(arr):
    
    for i in range(0,len(arr)):
        swapped = False
        for j in range(1,len(arr)- 1):
            if arr[j] < arr[j-1]:
                [arr[j],arr[j-1]] = [arr[j-1],arr[j]]
                swapped = True
                
        if(not swapped):
            break
    return arr

print(bubble_sort([1,3,2,4,5,2,10]))