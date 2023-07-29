n=int(input("Enter a number : "))
sum=0
temp=n
while(temp!=0):
    rem=temp%10
    sum=sum+rem
    temp=temp//10
if n%sum==0:
    print("Harshad number")
else:
    print("Not a harshad number")


