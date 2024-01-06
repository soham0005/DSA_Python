# Sequentially Search the element by comparing the value of target with the element of array

def linearSearch(arr,target):
    for i in range(len(arr)):
        if arr[i] ==target:
            return [True,i]
    return False

print(linearSearch([1,2,3,4,5],3))