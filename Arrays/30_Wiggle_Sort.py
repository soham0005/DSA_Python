
def wiggle_sort(nums):
    ans = []
    
    while len(nums) != 0:
        
        
        ans.append(min(nums))
        nums.remove(min(nums))
        if len(nums)!=0:
            ans.append(max(nums))
            nums.remove(max(nums))
    return ans
print(wiggle_sort([1,3,2,2,3,1]))
        
