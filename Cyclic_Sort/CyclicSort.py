# Use Cyclic Sort when Range from 1 to N is mentioned in the question

def cyclic_Sort(arr):
    i = 0
    
    while i < len(arr):
        correct = arr[i] - 1
        
        if arr[i] != arr[correct]:
            [arr[i],arr[correct]] = [arr[correct],arr[i]]
        else:
            i = i + 1
    return arr
    

print(cyclic_Sort([1,3,5,6,2,4]))