a=int(input("Enter the a value:"))
b=int(input("Enter the b value:"))
for i in range(a,b+1):
    num_digit=len(str(i))
    temp=i
    sum=0
    while temp!=0:
        digit=temp%10
        sum += digit ** num_digit
        temp=temp//10
    if sum==i:
        print(i)
