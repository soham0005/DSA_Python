

def rotatedBinarySearch(arr,key,start,end):
    
    if(start > end):
        return -1
    
    mid = start  + (end - start) // 2
    
    if key == arr[mid]:
        return mid
    
    if(arr[mid] >= arr[start]):
        if key >= arr[start] and key <= arr[mid]:
           return rotatedBinarySearch(arr,key,start,end-1)
        else:
            return rotatedBinarySearch(arr,key,mid+1,end)
    
    if key >= arr[mid] and key <= arr[end]:
        return rotatedBinarySearch(arr,key,mid+1,end)
    
    return rotatedBinarySearch(arr,key,start,mid-1)

arr = [5,6,7,8,9,1,2,3]
print(rotatedBinarySearch(arr,10,0,len(arr)-1))