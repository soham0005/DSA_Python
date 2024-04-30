def maxSubArray(nums,k):
        sum = 0
        count = 0

        for i in range(len(nums)):
            sum += nums[i]

            if sum % k == 0:
                count +=1
        return count
print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4],5))