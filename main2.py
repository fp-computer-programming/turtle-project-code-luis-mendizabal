

import turtle
import time
import random
# window Settings
window = turtle.Screen()
window.setup(width= 600,height= 600)
window.title("Snake Game")
window.bgcolor('green')
window.tracer()

#this will be the number of segments the turtle/snake will have
segments = []

#score
score = 0
highscore = 0

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
food.speed(0)
food.shape('circle')
food.color("Red")
food.penup()
food.goto(0,100)

#score board
pen = turtle.Turtle()
pen.penup()
pen.speed(0)
pen.hideturtle()
pen.goto(0, 262)
pen.shape('square')
pen.color('white')
pen.write("Score: 0 High Score: 0", align= 'center', font= ("Times New Roman", 24, 'normal'))

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
    #updates dictionaries
    window.update()

    # checks for collisions with the border
    if mainturtle.xcor()> -290 or mainturtle.xcor()<-290 or mainturtle.ycor()> 290 or mainturtle.ycor()< -290:
        #delays time, so it takes one second to be able to play the game again
        time.sleep(1)
        mainturtle.goto(0, 0)
        # prevents turtle from moving until key from above is pressed
        mainturtle.direction = 'stop'

    # makes the turtle segments go outside the the playable grid
    #if coordinates were within the grid then there would be a grey box at that specific coordinate
    # for every segment, each will go to that one coordinate
    for segment in segments:
        segment.goto(1000,1000)
    #clears the segments 
    segments.clear()

    # score gets reset to 0
    score = 0

    #latency or delay if it is closer to zero then there is close to no delay so the trurtle moves faster
    delay = 0.1

    #clears score board and writing
    pen.clear()
    # score and high score are updated
    pen.write("Score: {0} High Score: {1}".format(score, highscore), align='center', font= ('Times New Roman', 24, 'normal'))

    # checks for snake and food collision
    # distance function calculates the distance of one object that has moved
    if mainturtle.distance(food) < 20:
        # move food to a different locstion
        #start with x coordinate
        x = random.randint(-285, 285)
        #now randomize y coordinate withing playing grid
        y= random.randint(-285, 285)
        # both will combine to be a coordinate (x, y)
        food.goto(x, y)

        # now we have to add a segment when the turtle collides with the food
        # we have to make a new turtule
        new_segment = turtle.Turtle()
        new_segment.color('grey')
        new_segment.shape('square')
        new_segment.speed(0)
        segments.append(new_segment)

        # shorten delay to not make it seem long
        delay -= .001

        # when they collide the score has to increase. It will increase by 5
        score += 5

        # if score surpasses high score then high score has to equal score
        if score > highscore:
            highscore = score

        pen.clear()
        pen.write("Score: {0} High Score: {1}".format(score, highscore), align= 'Center', Font= ("Times New Roman", 24, "normal"))

        move()   


window.mainloop()