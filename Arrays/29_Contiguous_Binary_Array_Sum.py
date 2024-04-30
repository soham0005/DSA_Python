def findMaxLength(nums):
    max_len = 0
    count = 0
    count_dict = {0: -1}  
    for i in range(len(nums)):
        if nums[i] == 0:
            count += 1
        else:
            count -= 1

        if count in count_dict:  
            max_len = max(max_len, i - count_dict[count])
        else:
            count_dict[count] = i  
    return max_len

nums = [0,1,0]
print(findMaxLength(nums))  
