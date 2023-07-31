def pow(val,i):
    if i==0:
        return 1
    else:
        return val*pow(val,i-1)
n=int(input("Enter n value : "))
l1=[0]*20
temp=n
count=1
res=0
j=0
i=0
while(temp!=0):
    val=2
    rem=temp%10
    res=res+rem*pow(val,i)
    temp=temp//10
    i=i+1
    l1[j]=res
    if count%3==0:
        res=0
        i=0
        j=j+1
    count=count+1
for k in range(j,-1,-1):
        print(l1[k],end='')

    



        
