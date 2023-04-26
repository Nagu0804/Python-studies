from tkinter import *

x = Tk()

x.geometry("200x200")

check1 = IntVar()

check2 = IntVar()

check3 = IntVar()

l1=Label(x,text='Which langues do you known:')

chkbtn1 = Checkbutton(x, text="C", variable=check1, onvalue=1, offvalue=0, height=2, width=10,justify=LEFT)

chkbtn2 = Checkbutton(x, text="C++", variable=check2, onvalue=1, offvalue=0, height=2, width=10,justify=LEFT)

chkbtn3 = Checkbutton(x, text="Java", variable=check3, onvalue=1, offvalue=0, height=2, width=10,justify=LEFT)

l1.grid(row=1,columnspan=3)

chkbtn1.grid(row=2,column=1)

chkbtn2.grid(row=4,column=1)

chkbtn3.grid(row=6,column=1)

x.mainloop()