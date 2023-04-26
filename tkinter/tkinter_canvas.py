from tkinter import *
x=Tk()
x.minsize(600,600)
x.maxsize(1200,1200)
c=Canvas(x,bg='pink',width=200,height=200,cursor='circle',relief=RIDGE)
arc = c.create_arc((5,10,150,200),start = 0,extent = 150, fill= "white")  
c.pack()
x.mainloop()