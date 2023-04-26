from tkinter import *  
from functools import partial  
   
   
def add(label_result, n1, n2):  
    num1=(n1.get())  
    num2=(n2.get())  
    result=int(num1)+int(num2)  
    label_result.config(text="Result = %d" % result)  
    return
def sub(label_result, n1, n2):  
    num1=(n1.get())  
    num2=(n2.get())  
    result1=int(num1)-int(num2)  
    label_result.config(text="Result = %d" % result1)  
    return
def multi(label_result, n1, n2):  
    num1=(n1.get())  
    num2=(n2.get())  
    result1=int(num1)*int(num2)  
    label_result.config(text="Result = %d" % result1)  
    return
def divi(label_result, n1, n2):  
    num1=(n1.get())  
    num2=(n2.get())  
    result1=int(num1)/int(num2)  
    label_result.config(text="Result = %d" % result1)  
    return
   
x=Tk()  
x.geometry('400x200+100+200')  
  
x.title('Simple Calculator')  
   
number1=StringVar()  
number2=StringVar()  
  
labelNum1=Label(x, text="A").grid(row=1, column=0)  
  
labelNum2=Label(x, text="B").grid(row=2, column=0)  
  
labelResult=Label(x)  
  
labelResult.grid(row=7, column=2)  
  
entryNum1=Entry(x, textvariable=number1).grid(row=1, column=2)  
  
entryNum2=Entry(x, textvariable=number2).grid(row=2, column=2)  
  
add=partial(add, labelResult, number1, number2)
sub=partial(sub, labelResult, number1, number2)
multi=partial(multi, labelResult, number1, number2)
divi=partial(divi, labelResult, number1, number2)
  
button = Button(x, text="Addition", command=add).grid(row=3, column=0)  
button1 = Button(x, text="Subtraction", command=sub).grid(row=3, column=1)
button2 = Button(x, text="Multiplication", command=multi).grid(row=3, column=2)
button3 = Button(x, text="Division", command=divi).grid(row=3, column=3)
x.mainloop()  
