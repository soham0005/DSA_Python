# Leetcode - 1528

def shuffleString(s,indices):
    map = {}
    res = ""
    for i in range(0,len(s)):
        map[indices[i]] = s[i]
    
    for i in range(0,len(s)):
        res += map[i]
    print(res)
        
shuffleString("abc",[0,1,2])
    
    
