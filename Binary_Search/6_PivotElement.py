# Pivot Elemet - Largest Element in Sorted and Rotated Array:-
# [6,7,1,2,3,4,5]
def PivotElement(nums):
    start = 0
    end = len(nums) - 1
    
    while start <= end:
        mid = (start + (end - start) // 2)
        
        if mid<end and nums[mid] > nums[mid+1]:
            return nums[mid]
        elif mid<end and nums[mid-1] > nums[mid]:
            return mid-1
        elif nums[start] > nums[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1

print(PivotElement([6,7,8,9,19,1,2,3,4,5]))
            