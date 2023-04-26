#condition Statements

def mark_check():
    if (num>50 and num<60):
        print("You are Pass")
    elif(num>60 and num<90):
        print("You got Average Mark")
    elif(num>90 and num<99):
        print("You got Good Marks")
    elif(num==100):
        print("You got First Mark")
    else:
        print("You are Fail")

num=int(input("Enter Your Mark(xxx/100):"))
mark_check()
