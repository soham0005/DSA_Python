# def findNumbers(nums):
#     count = 0
#     for ele in nums:
#         if(even(ele)):
#             count += 1
#     return count

# def even(num):
#     numberOfDigits = countDigits(num)
#     return numberOfDigits % 2 == 0


# def countDigits(num):
#     count = 0
#     while(num > 0):
#         count += 1
#         num = num // 10
#     return count



# print(findNumbers([12,345,2,6,7896]))

class Solution(object):
    def even(self,num):
        digitCount = self.countDigit(num)
        return digitCount % 2 == 0

    def countDigit(self,num):
        count = 0
        while num > 0:
            count += 1
            num = num // 10
        return count
        
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for ele in nums:
            if(self.even(ele)):
                count += 1
        return count

sol = Solution()
print(sol.findNumbers([12,345,2,6,7896]))