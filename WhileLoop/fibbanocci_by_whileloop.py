#Fibanocci series
def fib(n):
    f=0
    s=1
    total=0
    i=0
    while(i<n):
        print(f)
        total=f+s
        f=s
        s=total
        i+=1
n=int(input('Enter Number:'))
fib(n)
