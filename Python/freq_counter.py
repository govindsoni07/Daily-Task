def countFrequency(n):
    freq = [0] * 10

    for i in str(n):
        freq[int(i)] += 1

    return freq
print(countFrequency(1223))