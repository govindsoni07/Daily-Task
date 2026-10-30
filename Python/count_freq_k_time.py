def countFreq(n: int, k: int) -> list[int]:
    freq={}
    for digit in str(n):
        if digit in freq:
            freq[digit]+=1
        else:
            freq[digit]=1

    result=[]
    for digit in freq:
        if freq[digit]>=k:
            result.append(int(digit))
    return sorted(result)

print(countFreq(112233,2))
