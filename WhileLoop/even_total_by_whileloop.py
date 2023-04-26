def sum(n):
    
    sum=0
    i=2
    while(i<=n):
        sum=sum+i
        
        i=i+2
    print("Total is:",sum)
n=int(input('Enter Number:'))
sum(n)
