from turtle import *
width(7)
speed(20)
# უნდა გავაკეთოთ 4 კვადრატი, მათ შორის დაშორება უნდა იყოს 100 პიქსელი. (ეს უნდა გაკეთდეს ფუნქიების საშუალებით, ანუ გიგაჩადურად)
def draw_square():
    for i in range(4):
     forward(150)
     left(90)

draw_square()
def change_directions(x, y):
   penup()
   goto(x, y)
   pendown()

change_directions(-250,0)

draw_square()

change_directions(-250, -250)


draw_square()

change_directions(0, -250)

draw_square()
   
exitonclick()
    
