def checkSortedAndRotated(nums):
    count = 0
    for i in range(len(nums)):
        if nums[i] > nums[(i+1) % len(nums)]:
            count += 1
        if count > 1:
            return False
    return True


print(checkSortedAndRotated([1,2,3,4,5,3]))