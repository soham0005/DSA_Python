
def subsequence(i,arr,subarr):
    if i ==  len(arr):
        print(subarr)
        
    else:
        subsequence(i+1,arr,subarr)
        
        subsequence(i+1,arr,subarr+[arr[i]])
        
    return

arr = [1,2,3]
subsequence(0,arr,[])

