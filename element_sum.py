n = int(input("Enter a number :"))
a = [1,7,9,8,0,6,2,9]
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[i]+a[j]==n:
            print(a[i],a[j])