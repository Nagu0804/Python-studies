#palindrome
def palin(n):
    result=0
    i=n
    while(n>0):
        num=n%10
        result=num+(result*10)
        n=n//10
               
    if(n==result):
        print('Number is Palindrom')
    else:
        print('Number is not Palindrom')
        
n=int(input('Enter  Number:'))
palin(n)
