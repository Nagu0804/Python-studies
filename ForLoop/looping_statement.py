# Looping Statement
def loop():

    for e in range(5):
        for f in range(5, e, -1):
            print(" ", end=" ")
        for g in range(e + 1):
            print('*', end=" ")
        for h in range(e):
            print('*', end=" ")
        print("\n")

    for i in range(5):
        for j in range(i):
            print("@",end=" ")
        for k in range(5, i, -1):
            print('1', end=" ")
        for l in range(4, i, -1):
            print('*', end=" ")
        print("\n")


loop()
