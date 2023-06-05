# Two Sum - Leetcode

def twoSum(nums,target):
    map = {}
    for i in range(len(nums)):
        ele = target - nums[i]
        
        if ele not in map:
            map[nums[i]] = i 
        else:
            return [map[ele],i]
print(twoSum([2,7,15,11],9))