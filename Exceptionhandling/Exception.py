"""
2 types of errors:
1) syntax errors:
    The errors which occur because of invalid syntax are called syntax errors.
2) Runtime errors
    Also Known as Exceptions.
    while executing the program if something goes wrong bcoz of end user input or
    logic or memory problems etc run time errors

"""
#Exception
'''An unwanted or unexpected event that disturbs flow of program is called exception.'''

'''The code which may raise exception is called risky code & we have to take risky code inside try block.
The handling code we have to take inside except block.
try:
    risky code
except:
    handling code
'''
try:                    # here we have written the error situation the try block wont raise any error & the code handled in except block.
    a=10
    b=0
    c=a/b
except:
    print("Division by 0 is not possible.")

#same with user input
a1 = int(input("Enter any value:"))
b1 = int(input("Enter any value:"))
try:
    c1 = a1 / b1
except ZeroDivisionError:
    print("division is not possible by 0")



'''within the try block if anywhere exception raised then rest of the try block wont be executed even though we handled that exception
if any statement which is not a part of try block raises an exception then it is always abnormal termination.'''

#try with multiple except blocks:
try:
    x=int(input("Enter first number:"))
    y=int(input("enter second number:"))
    print(x/y)
except ZeroDivisionError:
    print("cant divide by zero")
except ValueError:
    print("please provide int value only")




try:
    x1=int(input("Enter first number:"))
    y1=int(input("enter second number:"))
    print(x1/y1)
except ZeroDivisionError:
    print("ZeroDivisionError")
except ValueError:
    print("ValueError")
except ArithmeticError:
    print("Arithmetic Error")