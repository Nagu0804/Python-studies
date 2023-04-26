#fibanocci series for loop

def fib(n):
    f=0
    s=1
    total=0
    for i in range(0,n):
        print(f)
        total=f+s
        f=s
        s=total
num=int(input('Enter numbee of numbers:'))
fib(num)
