def areAnagrams(n1, n2):
    n1 = str(n1)
    n2 = str(n2)

    if sorted(n1) == sorted(n2):
        return True

    return False
print(areAnagrams(1221,1212))
