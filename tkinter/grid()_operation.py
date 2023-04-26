#grid_operation
from tkinter import *
x=Tk()
x.minsize(width=400,height=500)
x.maxsize(width=800,height=1000)
name=Label(x,text='Name',fg='red')
name.grid(row=1,column=0)
n=Text(x,width=50,height=2).grid(row=1,column=1)
print('\n')

sub1=Label(x,text='Tamil',fg='red')
sub1.grid(row=2,column=1)
s1=Text(x,width=50,height=2).grid(rowspan=2,columnspan=4)
print('\n')
'''
sub2=Label(x,text='English',fg='red')
sub2.grid(row=4,column=0)
s2=Text(x,width=50,height=2).grid(row=4,column=1)

sub3=Label(x,text='Maths',fg='red')
sub3.grid(row=6,column=0)
s3=Text(x,width=50,height=2).grid(row=6,column=1)

sub4=Label(x,text='Science',fg='red')
sub4.grid(row=8,column=0)
s4=Text(x,width=50,height=2).grid(row=8,column=1)

total=Label(x,text='Total',fg='red')
total.grid(row=10,column=0)
s5=Text(x,width=50,height=2).grid(row=10,column=1)

avrg=Label(x,text='Average',fg='red')
avrg.grid(row=12,column=0)
t=Text(x,width=50,height=2).grid(row=12,column=1)'''

x.mainloop()
