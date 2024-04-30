
def Subset(i,arr,subarr,output,myset):
  
    if i ==  len(arr):
        if tuple(subarr) not in myset:
            myset.add(tuple(subarr))
            output.append(subarr[:])
        
    else:
        Subset(i+1,arr,subarr,output,myset)
        
        Subset(i+1,arr,subarr+[arr[i]],output,myset)  
    return output

arr = ["1","2","2"]
myset = set()
# print(Subset(0,arr,[],[],myset))



def Subset2(nums):
    nums.sort()
    res = []
    
    def generate(index,ele):
        
        if index == len(nums):
            res.append(ele) if ele not in res else None
            return
        generate(index+1,ele)
        generate(index+1,ele+ [nums[index]])
        
    generate(0,[])
    return res

print(Subset2([1,2,2]))

