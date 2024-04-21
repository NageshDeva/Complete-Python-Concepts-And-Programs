n=int(input("Enter any number:"))
num_str=str(n)
num_digits=len(num_str)
temp=n
sum=0
while n!=0:
    digit=n%10
    sum += digit**num_digits
    n=n//10
if sum==temp:
    print("it is a armstrong number")
else:
    print("it is not a armstrong number")
     