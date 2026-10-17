def sumOfSeries(n, a, d):
    total = 0

    for i in range(n):
        total = total + a
        a = a + d

    return total

s=sumOfSeries(5,1,3)
print(s)