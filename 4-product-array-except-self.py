# Approaches: 
# 1. if not o(n), then use 2 loops to multiply each other except self and place it to another array
# 2. using left index, right index and a result placeholder for placing the product of all value on a specific index.
# left as base and right is runner where right check if right is not same as left index then multiply the value of 
# currently result placeholder to the right value then move left index if right reach end and right index returns back 
# to beginning or zero index. - t: o(n), s: o(1)
# 3. using dynamic programming, make sure result placholder is in place and then make two passes, 
# one pass is for prefix, which you assign the prefix value to current index then multiple the current value to the prefix
# second pass is for postfix which you go reverse, which you multiply the current postfix to the last index then update the 
# postfix by multiplying the current value which is running in reverse to the postfix value. - t: o(n), s: o(1)


# Problem:
# Given an integet array `nums`, return an array `answer` such that `answer[i]` is equal to the product
# of all the elements of numbers except `nums[i]`.
# The product of any prefix or suffix of `nums` is *guaranteed* to fit in the 32-bit interger.
# You must write an algorithm that runs in `o(n)` time and without using the division operation.

list1 = [1,2,3,4]
# input [1,2,3,4]
# output [24,12,8,6]

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

