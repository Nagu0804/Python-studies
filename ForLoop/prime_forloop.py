#Prime or not prime
def prime(n):

    for i in range(2,n):
        if n%i==0:
            print('It is a not prime')
            break
    else:
        print('It is a prime')
        
num=int(input('Enter number:'))
prime(num)
