# Left Rotate  array by 1
'''
Approach:- Store the first element is temp
           Start from index 1 to n-1 and simple swap to previous place.
           
           After swapping just change the value of temp and n-1

'''


def leftRotate(nums):
    temp = nums[0]
    print(nums[len(nums)-1])
    for i in range(1,len(nums)):
        [nums[i],nums[i-1]] = [nums[i-1],nums[i]]
    nums[len(nums) - 1] = temp
    return nums

def rightRotate(nums):
    n = len(nums)
    temp = nums[n - 1]
    
    for i in range(n-1,0,-1):
        nums[i] = nums[i-1]
    nums[0] = temp
    return nums 
    
print(rightRotate([1,2,3,4,5]))