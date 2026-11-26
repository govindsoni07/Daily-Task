def rotateArray(arr, r):
    n = len(arr)

    if n == 0:
        return arr

    r = r % n

    arr[:] = arr[r:] + arr[:r]

    return arr
print(rotateArray([1,2,3,4,5,6,7],r=3))