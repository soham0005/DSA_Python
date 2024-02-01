output = []
def Subset(arr,index,ans):
    
    if index == len(arr):
        # print(ans)
        output.append(ans)
        return
        
    else:
        Subset(arr,index+1,ans+[arr[index]])
        Subset(arr,index+1,ans)
    
    return output
print(Subset([1,2,3],0,[]))
    