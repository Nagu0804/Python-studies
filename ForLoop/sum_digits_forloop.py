# sum of digits forloop
def sum_digits(n):
    sum=0
    for i in range(1,n):
        sum=sum+(n%10)
        n=n//10
    print(sum)

num=int(input('Enter number:'))
sum_digits(num)
