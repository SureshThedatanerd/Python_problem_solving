
def fib(n):
      if n<=1:
            return n
      else:
            return fib(n-1)+fib(n-2)

lst=["A",'B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
str = input("enter a string : ")
lst1=list(str)
sum=0
for i in range(len(lst1)):
    k=lst1[i].upper()

    for j in range(0,len(lst)):
            if k==lst[j]:
                  sum=sum+fib(j)
print(sum)
                   

    

