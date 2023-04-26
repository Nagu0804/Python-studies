from tkinter import *

root = Tk() 
root.minsize(321, 321)
root.resizable(0,0)
root.title("Calculator")


def click(item):
    global expression
    expression = expression + str(item)
    ip_text.set(expression)

def btn_clear(): 
    global expression 
    expression = "" 
    ip_text.set("")
 
def equal():
    global expression
    result = str(eval(expression))
    ip_text.set(result)
    expression = ""
 
expression = ""
ip_text = StringVar()
 
 
ip_frame = Frame(root, width=321, height=50, bd=1, highlightbackground="black", highlightcolor="black", highlightthickness=2)
ip_frame.pack(side=TOP)
 
 
ip_field = Entry(ip_frame, font=('arial', 18, 'bold'), textvariable=ip_text, width=23, bd=1, justify=RIGHT)
ip_field.grid(row=0, column=0)
ip_field.pack(ipady=10)

frame = Frame(root, width=312, height=272.5, bg="grey")
frame.pack()


clear = Button(frame, text = "C", width = 32, height = 3, bd=1, command = lambda: btn_clear()).grid(row = 0, column = 0, columnspan = 3)
multiply = Button(frame, text = "*", width = 10, height = 3, bd=1, command = lambda: click("*")).grid(row = 0, column = 3)

 
seven = Button(frame, text = "7", width = 10, height = 3, bd=1, command = lambda: click(7)).grid(row = 1, column = 0)
eight = Button(frame, text = "8", width = 10, height = 3, bd=1, command = lambda: click(8)).grid(row = 1, column = 1)
nine = Button(frame, text = "9", width = 10, height = 3, bd=1, command = lambda: click(9)).grid(row = 1, column = 2)
divide = Button(frame, text = "/", width = 10, height = 3, bd=1, command = lambda: click("/")).grid(row = 1, column = 3)
 
four = Button(frame, text = "4", width = 10, height = 3, bd=1, command = lambda: click(4)).grid(row = 2, column = 0)
five = Button(frame, text = "5", width = 10, height = 3, bd=1, command = lambda: click(5)).grid(row = 2, column = 1)
six = Button(frame, text = "6", width = 10, height = 3, bd=1, command = lambda: click(6)).grid(row = 2, column = 2)
minus = Button(frame, text = "-", width = 10, height = 3, bd=1, command = lambda: click("-")).grid(row = 2, column = 3)
one = Button(frame, text = "1", width = 10, height = 3, bd=1, command = lambda: click(1)).grid(row = 3, column = 0)

two = Button(frame, text = "2", width = 10, height = 3, bd=1, command = lambda: click(2)).grid(row = 3, column = 1)
three = Button(frame, text = "3", width = 10, height = 3, bd=1, command = lambda: click(3)).grid(row = 3, column = 2)
plus = Button(frame, text = "+", width = 10, height = 3, bd=1, command = lambda: click("+")).grid(row = 3, column = 3)
 
zero = Button(frame, text = "0", width = 21, height = 3, bd=1, command = lambda: click(0)).grid(row = 4, column = 0, columnspan = 2)
dot = Button(frame, text = ".", width = 10, height = 3, bd=1, command = lambda: click(".")).grid(row = 4, column = 2)
equals = Button(frame, text = "=", width = 10, height = 3, bd=1, command = lambda: equal()).grid(row = 4, column = 3)
 
root.mainloop()
