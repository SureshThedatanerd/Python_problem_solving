

'''str=input("Enter a string : ")
str1=' '
for i in str:
    str1=i+str1
print(str1)'''


n=int(input("enter  n value : "))
str=' '
lst=[]
temp=n
while(temp!=0):
    rem=temp%2
    lst.append(rem)
    temp=temp//2
print(lst[::-1])