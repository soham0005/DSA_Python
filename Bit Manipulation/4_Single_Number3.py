def singleNumber(nums) -> int:
    count = 0
    res = []

    for ele in nums:
        if ele not in res:
            res.append(ele)
            count += 1
        elif ele in res and count == 1:
            res.append(ele)
            count += 1
        else:
            count = 0
    
    print(res)
singleNumber([0,1,0,1,0,1,99])