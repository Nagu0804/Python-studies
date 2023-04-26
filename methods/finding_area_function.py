# area of different shapes using function

#print('To find the area of shape')

def find():
    find=input('Do you  find the area of shape(Yes/No):')
    find=find.lower()
        
    if find=='yes':
        name()
    else:
        print('Thank you for visit!')

def continu():
    find=input('Do you  want to continue(Yes/No):')
    find=find.lower()
        
    if find=='yes':
        name()
    else:
        print('Thank you for visit!')
    
def name():
    print(' 1.Square','\n','2.Rectangle','\n','3.Triangle','\n','4.Circle')
    name1=input('Type the Name of the shape:')
    name1=name1.lower()

    if name1=='square' or name1=='1':
        area_square()
    elif name1=='rectangle' or name1=='2':
        area_rect()

    elif name1=='triangle' or name1=='3':
        area_triangle()
    elif name1=='circle' or name1=='4':
        area_circle()
    
def area_triangle():
    h=int(input('Enter height of triangle:'))
    b=int(input('Enter base of triangle:'))
    area=(h*b)/2
    print('area of the triangle is:',area,'\n')
    continu()
    

def area_rect():
    l=int(input('Enter height of rectangular:'))
    w=int(input('Enter base of rectangular:'))
    area=l*w
    print('Area of the rectangle is:',area,'\n')
    continu()

def area_square():
    a=int(input('Enter the side value of square:'))

    area=a*a
    print('Area of the square is:',area,'\n')
    continu()


def area_circle():
    r=int(input('Enter radius of circle:'))
    
    area=3.14*r*r
    print('Area of the circle:',area,'\n')
    continu()


 
find()
