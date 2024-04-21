n=int(input("Enter any value:"))
a=0
b=1
print("The Fibonacci series is:")
for i in range(n):
    print(a, end="")
    result=a+b
    a,b=b,result
