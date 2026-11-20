def deleteAllOccurrences(arr: List[int], X: int) -> List[int]:
    count=0
    for i in range(len(arr)-1,-1,-1):
        if arr[i] == X:
            arr.remove(arr[i])
            count+=1
    return arr[:]+count*[0]

print(deleteAllOccurrences([10, 20, 10, 30, 10, 40],10))
