#factorial by while loop

def factorial(n):
    f=1
    i=1
    while(i<=n):
        f=f*i
        i+=1

    print(f)
n=int(input('Enter Number:'))
factorial(n)
        
