#Palindrome by using for loop
def palin(n):
    rev=0
    for i in range(0,len(str(n)) ):
        num=n%10
        rev=(rev*10)+num
        n=n//10
        
    if n==rev:
        print('Number is palindrome')
    else:
        print('Number is not Palindrome')
    
num=int(input('Enter number:'))
palin(num)
