# author: LM (AMDG) 3/29/22
from tkinter import mainloop
import turtle
backgroundcolor = input("What color do you want the background to be?(not red) ")
turtlecolor = input("What color do you want the turtle to be?(not red) ")
# window Settings
window = turtle.Screen()
window.setup(600,600)
window.title("Snake Game")
window.bgcolor(backgroundcolor)
window.tracer(0)

# Turtle Setup
mainturtle = turtle.Turtle()
mainturtle.speed(0)
mainturtle.shape("square")
mainturtle.color(turtlecolor)
mainturtle.penup()
# sets position of turtle
mainturtle.goto(0, 100)

# set the scores equal to zero but will change throughout the game
highscore = 0
currentscore = 0

# snake food
apple = turtle.Turtle()
apple.shape("circle")
apple.color("red")
apple.penup()
apple.goto(1, 100)
apple.speed(0)

# pen function
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
#pen.hideturtle()
pen.penup()
# moves the writing to the top of the page
pen.goto(0,260)
pen.write("Score: 0   Highest Score: 0", align= 'center', font=('Times New Roman', 20, 'normal'))

# functions of the game
def go_up():
    mainturtle.
    while True:
        if 


window.mainloop()
