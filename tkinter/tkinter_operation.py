from tkinter import *
x=Tk()
x.minsize(width=200,height=300)
x.maxsize(width=600,height=750)
name=Label(x,text="Name").grid(row=0,column=0)
e1=Entry(x,text="Name").grid(row=0,column=1)
nbutton=Button(x,text="Next").grid(row=1,column=0)
email=Label(x,text="Email").grid(row=4,column=0)
e2=Entry(x,text="email").grid(row=4,column=1)
nbutton1=Button(x,text="Ok").grid(row=6,column=0)

x.mainloop()
