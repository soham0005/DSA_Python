from collections import Counter
nums = [1,2,4,3,5]

map = Counter(nums)

max_val = max(map.values())
result = sum([value for key,value in map.items() if value == max_val])

print(result)