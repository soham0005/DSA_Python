'''
Approach is: using 2 Pointers
one pointer pointing to first ele and second pointer to 1st index;

Loop and check if j's value is equal to i's value; if not equal then place j'value to i+1
else skip


'''

def removeDuplicates(nums):
    i = 0
    for j in range(1,len(nums)):
        if nums[j] != nums[i]:
            nums[i+1] = nums[j]
            i+=1
    return i+1

print(removeDuplicates([1,1,2]))