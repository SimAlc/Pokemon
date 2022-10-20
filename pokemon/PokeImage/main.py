# Importing libraries that might be required during the game
import turtle
import random

# Color list that can be used later for flags
colors = ['red', 'blue', 'green', 'purple', 'yellow', 'orange', 'black']
score = 0

# Creating player turtle that will be controlled by the user, using Turtle() class

wn=turtle.Screen()
wn.addshape('MyBulb.gif')
wn.addshape('EnemyBulb.gif')
player = turtle.Turtle()
player.speed(0)
player.shape('MyBulb.gif')
player.color('red')
player.shapesize(10)
player.penup()

# Creating the flags that the player need to capture and need to be respawned

flag = turtle.Turtle()
flag.speed(0)
flag.shape('EnemyBulb.gif')
flag.color(random.choice(colors))
flag.shapesize(5)
flag.penup()


# Function for the control keys, so python knows what to when any  button is pressed

# function to move up
def up():
    player.setheading(90)
    player.forward(10)

# function to move down
def down():
    player.setheading(270)
    player.forward(10)

# function to move left
def left():
    player.setheading(180)
    player.forward(10)

# function to move right
def right():
    player.setheading(0)
    player.forward(10)

# We will be creating events when user presses a key. In a way taking input.
turtle.listen()
# Connecting the function made earlier with the keys on the keyword.
turtle.onkey(up, 'Up')
turtle.onkey(down, 'Down')
turtle.onkey(left, 'Left')
turtle.onkey(right, 'Right')

# It keeps the game running and look for user input until the user the presses the 'x' button
turtle.mainloop()




