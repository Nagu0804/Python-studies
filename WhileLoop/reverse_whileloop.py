#reverse num by whileloop
def revers(n):
    result=0
    i=n
    while(n>0):
        num=n%10
        result=num+(result*10)
        n=n//10
        #i+=1
    print(result)

n=int(input('Enter number:'))
revers(n)
