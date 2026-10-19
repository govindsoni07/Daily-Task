n=int(input("Enter a no. to round:  "))
last=n%10
if last<=5:
    n=n-last
else:
    n=n+(10-last)
print("Rounded No. :",n)