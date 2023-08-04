import numpy as np
arr = np.array([3,2,5,1,9,8,7,6,10])
arr.sort()
l1=[]
l2=[]
if len(arr)%2==0:
    mid = len(arr)//2
    for i in range(0,mid):
        l1.append(arr[i])
    for j in range(len(arr)-1,mid-1,-1):
            l2.append(arr[j])
    print(l1+l2)
else:
    mid=(len(arr)//2)+1
    for i in range(0,mid):
        l1.append(arr[i])
    for j in range(len(arr)-1,mid-1,-1):
            l2.append(arr[j])
    print(l1+l2)
