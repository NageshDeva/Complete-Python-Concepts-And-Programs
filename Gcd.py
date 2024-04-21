def compute_GCD(a,b):
    if b==0:
        return a
    else:
        return compute_GCD(b, a%b)
    
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
print(compute_GCD(num1,num2))