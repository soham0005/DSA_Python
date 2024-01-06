

def modifiedLinearSearch(target,arr,index):
    finalList = []
    
    if(index == len(arr)):
        return finalList
    
    
    #List created for function scope only
    if(arr[index] == target):
        finalList.append(index)
    
    callList = []
    callList = modifiedLinearSearch(target,arr,index+1)
    finalList.extend(callList)
    
    return finalList

arr = [1,2,3,4,4,5,6,7,10,12,13,13]
print(modifiedLinearSearch(13,arr,0))