def insertElement(arr, X, P):
    return arr[:P] + [X] + arr[P:-1]

print(insertElement(arr=[10, 20, 30, 40, 50],X=99,P=2))

