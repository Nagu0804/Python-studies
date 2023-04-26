#palindrome
def palin(n):
    result=0
    i=n
    while(n>0):
        num=n%10
        result=num+(result*10)
        n=n//10
        #i+=1
    if i==result:
        print('Number is Paliindrom')
    else:
        print('Number is not Palindrome')

n=int(input('Enter number:'))
palin(n)
