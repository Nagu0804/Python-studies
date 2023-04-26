#multiple inheritance
class child1():

    def area_circle(self):
        r=int(input('Enter radius of circle value:'))
        area=3.14*r*r
        print('Area of the circle:',area,'\n')
        child4.continu(self)

    def peri_circle(self):
        r=int(input('Enter radius of circle value:'))
        pm=2*(22/7)*r
        print('Perimeter of circle:',pm,'\n')
        child4.continu(self)
        

class child2():
    def area_rect(self):
        l=int(input('Enter length of rectangle value:'))
        w=int(input('Enter width of rectangle value:'))
        area=l*w
        print('Area of the rectangle is:',area,'\n')
        child4.continu(self)

    def peri_rect(self):
        l=int(input('Enter length of rectangle value:'))
        w=int(input('Enter width of rectangle value:'))
        pm=2*(l+w)
        print('Perimeter of the rectangle is:',pm,'\n')
        child4.continu(self)

class child3():
    def area_triangle(self):
        h=int(input('Enter height of triangle value:'))
        ba=int(input('Enter Base of triangle value:'))
        area=(h*ba)/2
        print('Area  of the triangel:',area,'\n')
        child4.continu(self)
        
    def peri_triangle(self):
        a=int(input('Enter side1 of triangle value:'))
        b=int(input('Enter side2 of triangle value:'))
        c=int(input('Enter side3 of triangle value:'))
        pm=a+b+c
        print('perimeter  of the triangel:',pm,'\n')
        child4.continu(self)

class child4(child1,child2,child3):
    def area_call(self):
        shapes=['1.circle','2.rectangle','3.triangle']
        for i in shapes:
            print(i)

        print('\n')
        s=input('Type shape Name:')
        s=s.lower()
        if(s=='circle'):
            child1.area_circle(self)

        elif(s=='rectangle'):
            child2.area_rect(self)

        elif(s=='triangle'):
            child3.area_triangle(self)

        else:
            print('Entered wrong content!','\n',' Please bellow shapes...')
            child4.area_call(self)
            

    def peri_call(self):
        shapes=['1.circle','2.rectangle','3.triangle']
        for i in shapes:
            print(i)

        print('\n')
        s=input('Type shape Name:')
        s=s.lower()
        if(s=='circle'):
            child1.peri_circle(self)

        elif(s=='rectangle'):
            child2.peri_rect(self)

        elif(s=='triangle'):
            child3.peri_triangle(self)

        else:
            print('Entered wrong content!','\n',' Please bellow shapes...')
            child4.peri_call(self)
        
        
    def a(self):
        e=input('Type area or perimeter:')
        e=e.lower()
        if(e=='area'):
            child4.area_call(self)
            
        elif(e=='perimeter'):
            child4.peri_call(self)

        else:
            print('Entered wrong content!','\n',' Please type Area or Perimeter...')
            child4.a(self)

    def continu(self):
        con=input('Do you want continue(y/n):')
        con=con.lower()
        if (con=='y' or con=='yes'):
            child4.a(self)

        elif(con=='n' or con=='no'):
            print('!...Thank You...!')
        else:
            print('Entered wrong content!')
            print('Try again')
            child4.continu(self)

obj=child4()
obj.a()
#obj.all_methods()

        





    
