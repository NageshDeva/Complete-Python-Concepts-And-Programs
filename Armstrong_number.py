n=int(input("Enter any number:"))
temp=n
sum=0
while n!=0:
    digit=n%10
    sum=sum + (digit*digit*digit)
    n=n//10
if temp==sum:
    print("it is a armstrong number")
else:
    print("it is not an armstrong number")