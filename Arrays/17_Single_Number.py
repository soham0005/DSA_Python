# Single Number - Leetcode


def singleNumber(nums):
    ans = 0
    for ele in nums:
        ans = ans ^ ele
    return ans
print(singleNumber([2,2,1]))
        