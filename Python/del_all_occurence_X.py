arr=[10,20,10,30,10,40]
X=10
for i in range(len(arr)-1,-1,-1):
    if arr[i]==X:
        arr.pop(i)
        arr.append(0)
print(arr)