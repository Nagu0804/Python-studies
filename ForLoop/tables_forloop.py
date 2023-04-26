#tables by for loop
def table(n):
    multi=0
    for i in range(1,21):
        multi=i*n
        print(n,' x',i,' =',multi)
       

n=int(input('Enter multipy number:'))
table(n)
