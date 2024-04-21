#perfect number is a positive integer that is equal to the sum of  its positive divisors excluding the number.
# 6--> divisors--> 1, 2, 3, 6(exclude 6) =1+2+3=6 perfect number
num=int(input("Enter the number:"))
result=0
for i in range(1,num):
    if num%i==0:
        result=result+i
if result==num:
    print(num,"is a perfect number")
else:
    print(num,"is not a perfect number")