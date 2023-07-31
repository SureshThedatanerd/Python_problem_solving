lst=[]
n=int(input("enter n value : "))
k=int(input("enter k value : "))
for j in range(n):
        s=input("enter a string : ")
        lst.append(s)
print(lst)
lst1=[]
for i in lst:
        if i not in lst1:
                lst1.append(i)
        else:
                lst1.remove(i)
print(lst1[k-1])
        
                
