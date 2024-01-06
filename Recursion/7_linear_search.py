def linearSearch(arr,key,index):
    # if arr[index] == key:
    #     return True
    
    # return index < len(arr) - 1 and linearSearch(arr,key,index+1)
    
    if index == len(arr):
        return False

    return key == arr[index] or linearSearch(arr,key,index+1)

print(linearSearch([1,9,3,4,2],12,0))