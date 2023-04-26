# Fibanocci by if condition

def fib(num):
    if num <= 1:
        return num
    else:

        return fib(num - 1) + fib(num - 2)

    '''
    fib13(fib12(fib11(fib10(fib9(fib8(fib7(fib6(fib5(fib4(fib3(fib2(fib1(fib0))))+fib12(fib10(fib8(fib6(fib4(fib2(fib0))))))
    '''


num = int(input("Enter Number:"))

for i in range(num):
    print(fib(i))