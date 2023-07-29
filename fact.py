def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)

n = int(input("Enter a number : "))
temp=n
res=0
while(temp!=0):
    rem=temp%10
    res=res+fact(rem)
    temp=temp//10
if res==n:
    print("Given number is a strong number")
else:
    print("given number is not a strong number")
