n = int(input("enter a number : "))
def fib(n):
    if n<=1:
        return n
    return fib(n-2)+fib(n-1)
print(fib(n))
'''
for i in range(0,n+1):
    print(fib(i))'''

