
import turtle
# window Settings
window = turtle.Screen()
window.setup(width= 600,height= 600)
window.title("Snake Game")
window.bgcolor('green')
window.tracer()


# Turtle Setup
mainturtle = turtle.Turtle()
mainturtle.speed(0)
mainturtle.shape("square")
mainturtle.color("black")
mainturtle.penup()
mainturtle.goto(0, 100)
mainturtle.direction= "stop"

# food
food = turtle.Turtle()
food.shape('circle')
food.color("Red")
food.penup()
food.goto(0,100)

# sets direction of turtle. Thhis will be used when using keys
def move_up():
    if mainturtle.direction != 'down':
        mainturtle.direction == "up"
def move_down():
    if mainturtle.direction != 'up':
        mainturtle.direction == 'down'
def move_left():
    if mainturtle.direction != 'right':
        mainturtle.direction == 'left'
def move_right():
    if mainturtle.direction != 'left':
        mainturtle.direction == 'right'

def move():
    if mainturtle.direction == "up":
        y= mainturtle.ycor()
        mainturtle.sety(y+20)
    if mainturtle.direction == 'down':
        y= mainturtle.ycor()
        mainturtle.sety(y-20)
    if mainturtle.direction == "right":
        x= mainturtle.xcor()
        mainturtle.setx(x+20)
    if mainturtle.direction == 'left':
        x= mainturtle.xcor()
        mainturtle.setx(x-20)

# makin the computer listen for key presses
window.listen()
window.onkeypress(move_up, 'Up')
window.onkeypress(move_down, 'Down')
window.onkeypress(move_left, "Left")
window.onkeypress(move_right, "Right")

# main loop
while True:
    #updates dictionarie
    window.update()

    # checks for collisions with the border
    if mainturtle.xcor()> -290 or mainturtle.xcor()<-290 or mainturtle.ycor()> 290 or mainturtle.ycor()< -290:
        mainturtle.goto(0, 100)
        mainturtle.direction = 'stop'
    
    


window.mainloop()