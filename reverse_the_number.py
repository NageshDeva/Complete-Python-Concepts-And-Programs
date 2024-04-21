n = int(input("Enter any number: "))
reverse = 0
while n != 0:
    digit = n % 10
    reverse = (reverse * 10) + digit
    n //= 10
print("The reversed number is:", reverse)