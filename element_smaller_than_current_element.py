n = int(input("enter n value : "))
lst=[]
for i in range(n+1):
    s = int(input("enter s value : "))
    lst.append(s)
max1=int(input("enter max value : "))
lst.sort()
max=lst[0]
i=0
while(lst[i]<max1):
    if lst[i]>max:
        max=lst[i]
    i=i+1
print(lst)
print(max)