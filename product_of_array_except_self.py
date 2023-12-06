'''
Brute Force Approach

def product_except_self(nums):
    n = len(nums)
    result = [0] * n

    for i in range(n):
        product = 1
        for j in range(n):
            if i != j:
                product *= nums[j]
        result[i] = product

    return result

# Example usage:
nums1 = [1, 2, 3, 4]
print(product_except_self(nums1))  # Output: [24, 12, 8, 6]

nums2 = [-1, 1, 0, -3, 3]
print(product_except_self(nums2))  # Output: [0, 0, 9, 0, 0]

'''








def product_of_array_except_self(arr):
    arr_length=len(arr)
    result=[1]*arr_length

    left_product=1
    for index in range(arr_length):
        result[index]*=left_product
        left_product*=arr[index]
    
    right_product=1

    for index in range(arr_length-1,-1,-1):
        result[index]*=right_product
        right_product*=arr[index]

    return result 


if __name__=="__main__":
    print(product_of_array_except_self([1,2,3,4]))




