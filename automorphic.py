n=int(input("Enter a number : "))
res=n**2
l1=list(map(int,str(n)))
l2=[]
for i in range(len(str(n))):
    rem=res%10
    l2.append(rem)
    res=res//10
if l1==l2[::-1]:
    print("automorphic number")
else:
    print(" not an automorphic number")
   
    


