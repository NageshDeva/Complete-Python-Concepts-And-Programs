num=int(input("Enter the value:"))
fact=1
if num<1:
    print("no factorial for less than 1")
else:
    for i in range(1,num+1):
        fact=fact*i
    print("The factorial of the given num is", fact)