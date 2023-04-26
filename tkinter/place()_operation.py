from tkinter import *


    
x=Tk()

x.minsize(400,400)


name=Label(x,text="Name",bg="red").place(x=25,y=30)
clas=Label(x,text="Class",bg="red").place(x=25,y=60)
m1=Label(x,text="M1",bg="blue").place(x=25,y=90)
m2=Label(x,text="M2",bg="blue").place(x=25,y=120)
m3=Label(x,text="M3",bg="blue").place(x=25,y=150)
total=Label(x,text="Total",fg="yellow").place(x=85,y=180)
avrg=Label(x,text="Average",fg="grey").place(x=130,y=210)
e1=Entry(x).place(x=85,y=30)
e2=Entry(x).place(x=85,y=60)
e3=Entry(x).place(x=85,y=90)
e4=Entry(x).place(x=85,y=120)
e5=Entry(x).place(x=85,y=150)
e6=Entry(x).place(x=135,y=180)
e7=Entry(x).place(x=185,y=210)
x.mainloop()
