def fib(n):
    a,b=0,1
    print("The fibonacci series is")
    for i in range(n):
        print(a, end=" ")
        result=a+b
        a,b=b,result

fib(10)