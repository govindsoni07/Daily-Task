
def duplicateZeros(arr):
    n = len(arr)
    result = []

    for num in arr:
        result.append(num)

        if num == 0:
            result.append(0)

    return result[:n]


arr = [1, 0, 2, 3, 0, 4, 5, 0]
print(duplicateZeros(arr))
