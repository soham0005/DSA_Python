def permutate(nums):
    ans = []
    index = 0
    
    solve(nums,ans,index)
    return ans
    


def solve(nums,ans,index):
    
    if index >= len(nums):
        if nums[:] not in ans:
            ans.append(nums[:])
        return
    
    for j in range(index,len(nums)):
        nums[index],nums[j] = nums[j],nums[index]
        solve(nums,ans,index+1)
        nums[index],nums[j] = nums[j],nums[index]

print(permutate([1,2,3]))