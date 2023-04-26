def big_num():
    n=int (input('How many number: '))
    i=0
    total=0
    while(i<n):
        num=int(input('Enter Number: '))
        total=total+num
        i+=1

    print('\n')
    print('Total is:',total)
big_num()
