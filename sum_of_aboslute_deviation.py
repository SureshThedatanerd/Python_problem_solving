import numpy as np
a =  np.array([3,2,9,5,1,8,7,6,10])
a.sort()
print(a)
sum=0
if len(a)%2==0:
    mid1 = len(a)//2-1
    mid2 = len(a)//2
    print(mid1,mid2)
    med = (a[mid1]+a[mid2])/2
    print(med)
    for i in range(0,len(a)):
        sum =sum + abs(a[i]-med)
    print(sum)
else:
    sum=0
    med = a[len(a)//2]
    for i in range(0,len(a)):
        sum = sum +abs(a[i]-med)
    print(sum)


        

    


