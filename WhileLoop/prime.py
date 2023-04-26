#prime or not

n=int(input('Enter Number:'))
i=2
while(i<n):
    if(n%i==0):
        print(n,' is not a prime')
        break
    i+=1
else:
    print(n,' is a prime')
            

