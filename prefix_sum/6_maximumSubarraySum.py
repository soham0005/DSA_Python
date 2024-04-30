def maxSubArray(nums):
        import sys
        sum = 0
        maxSum = -sys.maxsize-1

        for i in range(len(nums)):
            sum += nums[i]

            if sum > maxSum:
                maxSum = sum
            
            if sum < 0:
                sum = 0
        return maxSum
print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))