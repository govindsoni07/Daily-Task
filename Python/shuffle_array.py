def shuffle(nums, n):
    result = []

    for i in range(n):
        result.append(nums[i])
        result.append(nums[i + n])
    return result

print(shuffle([1,2,3,4,4,3,2,1],4))