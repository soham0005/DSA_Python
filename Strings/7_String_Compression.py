# chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
chars = ["a","a","b","b","b","c","c","c"]

from collections import Counter

result = Counter(chars)
ans = []
for char in chars:
    count = result[char]
    if char not in ans:
            
        if count == 1:
            ans.append(char)
        else:
            ans.append(char)
            ans.append(count)

    
print(ans)