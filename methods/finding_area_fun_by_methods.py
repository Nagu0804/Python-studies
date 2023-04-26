#with parameters & return value
def area_triangle(h,b):
    area=(h*b)/2
    return (area)

#with parameters & without return value
def area_rect(l,w):
    area=l*w
    print('Area of the rectangle is:',area,'\n')

#without parameters & return value
def area_square():
    a=int(input('Enter the side value of square:'))

    area=a*a
    return (area)

#without parameters & without return value
def area_circle():
    r=int(input('Enter radius of circle:'))
    
    area=3.14*r*r
    print('Area of the circle:',area,'\n')

h=int(input('Enter height of triangle:'))
b=int(input('Enter base of triangle:'))
x=area_triangle(h,b)
print('area of the triangle is:',x,'\n')

l=int(input('Enter height of rectangular:'))
w=int(input('Enter base of rectangular:'))
area_rect(l,w)

x=area_square()
print('Area of the square is:',x,'\n')

area_circle()
