def product_except_self(nums):
    product = 1
    arr = []

    # Forward pass
    for i in range(len(nums)):
        print("Iteration value i is: ",i)

        arr.append(product)
        print("Array Value: ",arr)
        print(product, nums[i])
        product *= nums[i]
        print("Product variable value: ",product)

    product = 1

    # Backward pass
    for j in range(len(nums) - 1, -1, -1):
        print("Backward Pass value of J: ",arr[j],product)

        arr[j] *= product
        product *= nums[j]

    return arr

print(product_except_self([1,2,3,4]))