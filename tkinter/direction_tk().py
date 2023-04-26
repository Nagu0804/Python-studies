from tkinter import *
x=Tk()
x.minsize(width=200,height=300)
x.maxsize(width=600,height=750)

south=Button(x,text="south",fg="yellow").pack(side=BOTTOM )
north=Button(x,text="north", fg="green").pack(side=TOP)
west=Button(x,text="west" ,fg="blue").pack(side=LEFT)
east=Button(x,text="east",fg="black").pack(side=RIGHT)

x.mainloop()
