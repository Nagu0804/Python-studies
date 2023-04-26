def big_num():
    num=int(input('How many numbers:'))
    i=0
    maxi=0
    low=100000
    while(i<num):
        n=int(input('Enter Number: '))
        if maxi>n:
            maxi=maxi
        elif maxi<n:
            maxi=n
        if low>n:
            low=n
        elif low<n:
            low=low
        i+=1

    print('Biggest Num is:',maxi)
    print('Lowest Num is:',low)
big_num()
