# Prefix Sum from given ranges inclusive

def prefix_Sum(nums,left,right):
    
    ans = 0
 
    
    for i in range(left,right+1):
        ans += nums[i]
        
    return ans
print(prefix_Sum([2,7,3,5,6,3,9,-8,4,2],4,8))