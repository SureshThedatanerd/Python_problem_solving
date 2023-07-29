'''
def power(n,pow):
            if pow!=0:
                return n * power(n,pow-1)
            else:
                return 1 
n=int(input('enter a number : '))
pow=int(input("Enter power : "))
print(power(n,pow))
'''
n=int(input('enter a number : '))
i=int(input("Enter power : "))
def pow(n,i):
    power=n
    for j in range(1,i):
         power = n * power
    return power
print(pow(n,i))



    
