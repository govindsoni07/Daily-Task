nums=[1,3,2,1,2,1,1,2,2,4,5]
freq={}
for i in nums:
    if i not in freq:
        freq[i]=0
    freq[i]+=1
print(freq)
