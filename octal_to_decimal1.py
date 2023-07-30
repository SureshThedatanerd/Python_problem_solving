def pow(val,i):
    if i==0:
        return 1
    else:
        return val*pow(val,i-1)
n=int(input("Enter n value : "))
temp=n
res=0
i=0
while temp!=0:
    val=8
    rem=temp%10
    res=res+rem*pow(8,i)
    i=i+1
    temp=temp//10
print(res)
