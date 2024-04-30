'''
Approach: in each iteration, one element is picked and placed in its appropriate position
Start from index 1 and consider element at index 0 as sorted part of array.

'''

def insertion_sort(nums):
    for i in range(1,len(nums)):
        temp = nums[i]
        j = i - 1
        
        while j>=0 and nums[j] > temp:
            nums[j+1] = nums[j]
            j -=1
        nums[j+1] = temp 
    return nums

print(insertion_sort([10,2,1,4,5,3,7]))