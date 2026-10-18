a=int(input("Enter a no. : "))

last=a%10

if last<=5:
    a=a-last
else:
    a=a+(10-last)
print(a)