class myClass:
    a=int(input('Enter the side value of square:'))




    def peri_square(self):
        pm=4*self.a
        return pm
    
    def area_square(self):
        #a=int(input('Enter the side value of square:'))
        area=self.a*self.a
        return area
  

    def area_circle(self):
        r=int(input('Enter radius of circle:'))
        area=3.14*r*r
        pm=2*(22/7)*r
        print('Area of the circle:',area)
        print('Perimeter of circle:',pm,'\n')
        

    def area_triangle(self,h,b):
        area=(h*b)/2
        return (area)
    
    def peri_triangle(self,a,b,c):
        pm=a+b+c
        return pm

    def area_rect(self,l,w):
        area=l*w
        pm=2*(l+w)
        print('Area of the rectangle is:',area)
        print('Perimeter of the rectangle is:',pm,'\n')
obj=myClass()
x=obj.area_square()
print('Area  of the square:',x)
y=obj.peri_square()
print('Perimeter  of the square:',y,'\n')

obj.area_circle()

h=int(input('Enter height of triangle:'))
i=int(input('Enter base of triangle:'))
z=obj.area_triangle(h,i)
print('Area  of the triangel:',z,'\n')

a=int(input('Enter side1 of triangle:'))
b=int(input('Enter side2 of triangle:'))
c=int(input('Enter base of triangle:'))
w=obj.peri_triangle(a,b,c)
print('perimeter  of the triangel:',w,'\n')

l=int(input('Enter length of Rectangle:'))
k=int(input('Enter width of Rectangle:'))
obj.area_rect(l,k)
