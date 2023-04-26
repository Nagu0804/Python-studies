 #Calculate the sum of all numbers from 1 to a given number
def sum(n):
    sum=0
    for i in range(1,n+1,1):
        sum=sum+i
    print("sum is:",sum)
num=int(input("enter Your Number:"))
sum(num)
