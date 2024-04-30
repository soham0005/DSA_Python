# Recursive Solution
def knapsack(weight,inputdata,w,n):
    if n == 0 or w == 0:
        return 0
    
    if weight[n-1] > w:
        return knapsack(weight,inputdata,w,n-1)
    
    else:
        return max(inputdata[n-1] + knapsack(weight,inputdata,w - weight[n-1],n-1), knapsack(weight,inputdata,w,n-1))



# DP Memoized Version
def knapsack(weight, inputdata, w, n):
    if n == 0 or w == 0:
        return 0
    
    if dp[n][w] != -1:
        return dp[n][w]
    
    if weight[n-1] > w:
        dp[n][w] = knapsack(weight, inputdata, w, n-1)
        return dp[n][w]
    else:
        dp[n][w] = max(inputdata[n-1] + knapsack(weight, inputdata, w - weight[n-1], n-1), knapsack(weight, inputdata, w, n-1))
        return dp[n][w]
    

#  Top Down Approach

def knapsack_top_down(weight,val,result,n,dp):
    
    for i in range(n+1):
        for w in range(result+1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weight[i-1] <= w:
                dp[i][w] = max(val[i-1] + dp[i-1][w-weight[i-1]],dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][result]


result = 6
weights = [1, 2, 3]
values = [10, 15, 40]
n = len(weights)

# Initialize dp table with zeros
dp = [[0 for _ in range(result + 1)] for _ in range(n + 1)]

ans = knapsack_top_down(weights, values, result, n, dp)
print(ans)