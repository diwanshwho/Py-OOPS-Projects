## This Geometry Game is good to have a starting knowledge of how Object-Oriented Progamming Works.

''' This Program takes lower and upper points for a imaginary rectangle and check if the input provided
    by the user lie inside the rectangle or not.'''

from turtle import Turtle, done
from random import randint


## Class to take x & y co-ordinates from the user input
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    ## Method to check if the point lies within Rectangle or not.
    def falls_in_rec(self, rect):  
        if rect.lowleft.x < self.x < rect.upright.x \
        and rect.lowleft.y < self.y < rect.upright.y:
            
            return True
        
        else: 
            return False

## Class to generate Rectangle and calculate its area.
class Rectangle:


    def __init__(self, lowleft, upright):
        self.lowleft = lowleft
        self.upright = upright

    def area(self):
        return (self.upright.x - self.lowleft.x) * (self.upright.y - self.lowleft.y)


## Class to create graphical interface of the rectangle 
class GUIRect(Rectangle):

    def make(self, screen):

        screen.penup()
        screen.goto(rect.lowleft.x,rect.lowleft.y)
        screen.pendown()
        screen.forward(rect.upright.x - rect.lowleft.x)
        screen.left(90)
        screen.forward(rect.upright.y - rect.lowleft.y)
        screen.left(90)
        screen.forward(rect.upright.x - rect.lowleft.x)
        screen.left(90)
        screen.forward(rect.upright.y - rect.lowleft.y)

## Class to mark the point on the graphical canvas. 
class GUIPoint(Point):

    def make(self, screen):

        screen.penup()
        screen.goto(self.x,self.y)
        screen.pendown()
        screen.dot(5, 'red')

rect = GUIRect(Point(randint(0,100),randint(0,100)),Point(randint(100,200),randint(100,200)))
user = GUIPoint(int(input("Enter X: ")),int(input("Enter Y:  ")))

print("Your Point is within Rectangle: ",user.falls_in_rec(rect))

print(f"\nRectangle co-ordinates are: ({rect.lowleft.x},{rect.lowleft.y}) \
      & ({rect.upright.x},{rect.upright.y})")

userarea = int(input("Can you guess the area:  "))
print("You missed the correct area by:  ",rect.area() - userarea)

tur = Turtle()
rect.make(tur)  
user.make(tur)
done()
