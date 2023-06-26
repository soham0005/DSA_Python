# Leetcode - 2729

def isFascinating(n):
    res = str(n) + str(2*n) + str(3*n)
    print(res)
    ans = set(res)
    
    return len(ans) == 9 == len(res) and '0' not in ans
    
    
    
print(isFascinating(192)) 