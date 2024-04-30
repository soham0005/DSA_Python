# Check if Array is Sorted or not - GFG Question

def isSortedOrNot(nums):
    for i in  range(1,len(nums)-1):
        if nums[i] >= nums[i-1]:
            pass
        else:
            return 0
    return 1

print(isSortedOrNot([10,20,30,40]))