def maximumSubarraySum(nums, k) -> int:
    maxSum = float('-inf')
    currSum = 0
    left = 0

    for right in range(len(nums)):
        currSum += nums[right]

        # Check for valid subarrays while maintaining a sliding window
        while left < right and abs(nums[left] - nums[right]) > k:
            currSum -= nums[left]
            left += 1

        # Consider all subarrays ending at 'right', including length 1
        maxSum = max(maxSum, currSum)

    return maxSum

print(maximumSubarraySum([-1, 3, 2, 4, 5], 3))  # Output: 11 (correct)
