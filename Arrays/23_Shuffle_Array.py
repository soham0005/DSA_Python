# Leetcode - 1470 Shuffle the Array

def ShuffleArray(nums,n):
    
    while n < len(nums):
        temp = []
        for i in range(n):
            temp.append(nums[i])
            temp.append(nums[i+n])
        return temp