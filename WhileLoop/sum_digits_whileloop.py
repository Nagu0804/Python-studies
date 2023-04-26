#Find the sum of digits
def sum_digits(n):
    total=0
    i=0
    while(n>0):
        num=n%10
        total=total+num
        n=n//10
        i+=1
    print('Sum of Digits is ',total)
n=int(input('Enter Number:'))
sum_digits(n)
        
        
        
