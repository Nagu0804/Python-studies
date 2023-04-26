def unit_calci(n):
    
    if n<=100:
        print('Your unit charge is Zero','\n','(100 units free in TN)')

    elif n>101 and n<501:
        unit=n-100
        charge=unit*8
        print('Your unit is',n,'Amount to paid is',charge,'rs')

    elif n>=501 and n<1001:
        unit=n-500
        
        charge=(400*8)+(unit*10)
        print('Your unit is',n,'Amount to paid is',charge,'rs')

    elif n>=1001 and n<2001:
        unit=n-1000
        charge=400*8+500*10+unit*15
        print('Your unit is',n,'Amount to paid is',charge,'rs')

    elif n>=2001 and n<5001:
        unit=n-2000
        charge=400*8+500*10+1000*15+unit*20
        print('Your unit is',n,'Amount to paid is',charge,'rs')

    elif n>=5001 and n<10001:
        unit=n-5000
        charge=400*8+500*10+1000*15+3000*20+unit*25
        print('Your unit is',n,'Amount to paid is',charge,'rs')

    elif n>=10001 and n<20001:
        unit=n-10000
        charge=400*8+500*10+1000*15+3000*20+5000*25+unit*50
        print('Your unit is',n,'Amount to paid is',charge,'rs')

    elif n>20000:
        unit=n-20000
        charge=400*8+500*10+1000*15+3000*20+5000*25+10000*50+unit*75
        print('Your unit is',n,'Amount to paid is',charge,'rs')

n=int(input('Enter units in (numbers):'))
unit_calci(n)
