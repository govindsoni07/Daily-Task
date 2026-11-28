def frequencyArray(arr):
    freq = [0] * 101

    for num in arr:
        index = num - 900
        freq[index] += 1

    return freq

print(frequencyArray([999,999,999,999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999]))