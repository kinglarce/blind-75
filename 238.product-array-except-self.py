# https://leetcode.com/problems/product-of-array-except-self/
# Input: [1,2,3,4]
# Output [24,12,8,6]

# using running pointer - t: o(n), s: o(1)
def product_array_except_self(nums):
    result = [1] * (len(nums))
    left = 0
    right = 1
    result[left] = nums[left]
    while left < len(nums):
        right_value = nums[right]
        if right != left:
            result[left] = result[left] * right_value
        right += 1
        if right >= len(nums):
            left += 1
            right = 0
    return result

def product_array_except_self(nums):
    result = [1] * (len(nums))
    prefix = 1
    for i in range(len(nums)):
        result[i] = prefix
        prefix = prefix * nums[i]
    postfix = 1
    for i in range(len(nums)-1, -1, -1):
        result[i] = result[i] * postfix
        postfix = postfix * nums[i]

    return result

print(product_array_except_self([1,2,3,4])) # Expect [24,12,8,6]
print(product_array_except_self([-1,1,0,-3,3])) # Expect [0,0,9,0,0]

