n=int(input("Enter number of strings : "))
lst=[]
lst1=[]
for i in range(0,n):
    s=input("enter words : ")
    lst.append(s)
for j in range(0,len(lst)):
   if lst[j] not in lst1:
       lst1.append(lst[j])
print("unique _words : ",len(lst1))
for k in range(0,len(lst1)):
    count=0
    for x in range(0,len(lst)):
        if lst1[k] == lst[x]:
            count=count+1
    print(count)

