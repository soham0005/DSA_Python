# Leetcode Question - 2460

'''
Brute Force: use extra space and count the total zeroes and modify the array according to condtition and then append zeroes upptill count at the end

Optimized Solution:
Apply the operation to modify the array.
Use two pointers j = 0, i from starting,
swap when j is zero and i is not zero and increment j

if j is not zero then increment 


'''
# def applyOperations(nums):
#     temp = []
#     count = 0
    
#     for i in range(len(nums) - 1):
#         if nums[i] == nums[i+1]:
#             nums[i] = nums[i] * 2
#             nums[i+1] = 0
#     for i in nums:
#         if i != 0:
#             temp.append(i)
#         else:
#             count+=1
#     return temp+[0]*count  
        
# Optimized Solution  
def applyOperations(nums):    
    for i in range(len(nums) - 1):
        if nums[i] == nums[i+1]:
            nums[i] = nums[i] * 2
            nums[i+1] = 0
    j = 0
    for i in range(len(nums)):
        if nums[j] == 0 and nums[i] != 0:
            [nums[i],nums[j]] = [nums[j],nums[i]]
            j+=1
        elif nums[j]!=0:
            j+=1
    return nums  

    
print(applyOperations([1,2,2,1,1,0]))