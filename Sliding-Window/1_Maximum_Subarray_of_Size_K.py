# GFG
'''
Approach:
1) Generate a window Sum
2) Assign it to max Sum
3) Run a Loop and add next element to window sum and subtract previous value
4) Compare with maxSum

'''

def maximum_Subarray(arr,k):
    window_sum = sum(arr[:k])
    maxSum = window_sum
    n = len(arr)
    for i in range(n-k):
        window_sum = window_sum - arr[i] + arr[i+k]
        maxSum = max(maxSum,window_sum)
    return maxSum

print(maximum_Subarray([100,200,300,400],3))