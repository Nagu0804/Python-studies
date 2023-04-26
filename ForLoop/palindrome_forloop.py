#Palindrome by using for loop
def palin(n):
    rev=0
    i=n
    for i in range(0,len(str(n))):
        num=n%10
        rev=(rev*10)+num
        n=n//10
        
    if i ==rev:
        print('Number is palindrome')
    else:
        print('Number is not Palindrome')
    
num=(input('Enter number:'))
palin(num)
