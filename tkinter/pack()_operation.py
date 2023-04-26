from tkinter import *
x=Tk()
x.minsize(200,400)
x.maxsize(400,800)

t=Button(x,text='TOP',bg='blue').pack(side=TOP)

r=Button(x,text='RIGHT',bg='brown').pack(side=RIGHT)

b=Button(x,text='BOTTOM').pack(side=BOTTOM)

l=Button(x,text='LEFT',bg='black',fg='white').pack(side=LEFT)

x.mainloop()
