# author: LM (AMDG) 3/29/22
from tkinter import mainloop
import turtle
backgroundcolor = input("What color do you want the background to be? ")
# window Settings
window = turtle.Screen()
window.setup(600,600)
window.title("Snake Game")
window.bgcolor(backgroundcolor)

# Turtle Setup
turtlecolor = input("What color do you want the turtle to be? ")
mainturtle = turtle.Turtle()
mainturtle.speed(0)

window.mainloop()
