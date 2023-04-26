#revers by for loop
def reverse(n):
    rev=0
    for i in range(0,len(str(n)) ):
        num=n%10
        rev=(rev*10)+num
        n=n//10
        
    print(rev)
    
num=int(input('Enter number:'))
reverse(num)
