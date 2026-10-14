n1=int(input("Enter a 1st no. : "))
n2=int(input("Enter a 2nd no. : "))
lcm=max(n1,n2)
while True:
    if lcm%n1==0 and lcm%n2==0:
        break
    lcm+=max(n1,n2)
print("LCM : ",lcm)