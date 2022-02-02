def circle(radius):
    print("The perimeter cirle is",2*3.14*radius)
    print("The area of circle is",3.14*radius*radius)

def square(length):
    print("The perimeter of the square is",4*length)
    print("The area of the sqaure is",length*length)

def rectangle(length,breath):
    print("The perimeter of the rectangle is",2*length*breath)
    print("The area of the rectangle is",length*breath);

circle(int(input("enter the readius of the circle")))
square(int(input("enter the length of the square")))
rectangle(int(input("enter the length of the rectangle")),int(input("enter the breadth of the rectangle")))
