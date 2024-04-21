#Addition of two numbers.
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
sum=a+b
print(f"sum: {a} + {b} = {sum}")

#Division
num1=float(input("Enter a num:"))
num2=float(input("Enter a num:"))
if num2 == 0:
    print("Error: Division by zero is not allowed")
else:
    div= num1/num2
    print(f"Division: {num1} / {num2} = {div}")
