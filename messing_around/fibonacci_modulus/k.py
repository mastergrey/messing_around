import turtle
my_window = turtle.Screen()
my_pen=turtle.Turtle()
a=[2,3,5,7,11,13,17,19,23,31,37,41,43,47]
for i in a:
    if(i%2==0):
        my_pen.forward(100)
        my_pen.right(90)
    else:
        my_pen.forward(100)
        my_pen.left(90)
