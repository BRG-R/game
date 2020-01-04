# You can play the game with arrow keys and space

import turtle
import random
import math
from random import randint
#The screen setup
wn = turtle.Screen()
wn.bgcolor("gray")

#Drawing borders

border = turtle.Turtle()
border.penup()
border.setposition(-350,-350)
border.color("white")
border.pendown()
border.hideturtle()
border.pensize(3)
border.speed(800)
for side in range(4):
    border.forward(700)
    border.left(90)
border.penup()
border.setpos(-280,350)
border.pendown()
border.write("SURVIVE AS LONG AS YOU CAN, USE ARROW KEYS AND SPACE", font=("Arial",11,"bold"))
border.hideturtle()
border.penup()
border.setpos(-130,370)
border.color("yellow")
border.write("ESCAPING FROM THE DRUNK BALLS", font=("Calibri",13,"bold"))
#Creating player turtle

player = turtle.Turtle()

player.color("blue")
player.shape("turtle")
player.penup()
player.speed(0)
#Setting speed variable.
speed = 0





#Defined functions

def uzaklik(x1,x2,y1,y2):
    a = y2- y1
    b = x2 -x1
    return math.sqrt(a*a + b*b)
    
def turnleft():
    player.left(30)
    
def turnright():
    player.right(30)
    
def speedboost():
    global speed
    if speed < 20:
        speed += 2

def speedbrake():
    global speed
    if speed>0:
        speed -= 2
        
def stop():
    global speed
    speed = 0
    

def boundaries(player):
    if player.xcor() < -350:
        player.hideturtle()
        player.speed(1200)
        player.setposition(350,player.ycor())
        player.speed(0)
        player.showturtle()
    elif player.xcor() > 350:
        player.hideturtle()
        player.speed(1200)
        player.setposition(-350,player.ycor())
        player.speed(0)
        player.showturtle()
    if player.ycor() < -350:
        player.hideturtle()
        player.speed(1200)
        player.setposition(player.xcor(),350)
        player.speed(0)
        player.showturtle()
    elif player.ycor() > 350:
        player.hideturtle()
        player.speed(1200)
        player.setposition(player.xcor(),-350)
        player.speed(0)
        player.showturtle()

#Setting keyboard bindings.

turtle.listen()
turtle.onkeypress(turnleft, "Left")
turtle.onkeypress(turnright, "Right")
turtle.onkeypress(speedboost, "Up")
turtle.onkeypress(speedbrake, "Down")
turtle.onkey(stop, "space")

#setting enemies

#enemy1
enemy1 = turtle.Turtle()
enemy1.shape("circle")
enemy1.shapesize(3)
enemy1.color("black")
enemy1.penup()
enemy1.speed(1000)
enemy1.setposition(randint(-300,300),randint(-300,300))
enemy1.speed(0)
#enemy2(ifyouwant)
enemy2 = turtle.Turtle()
enemy2.shape("circle")
enemy2.shapesize(3)
enemy2.color("dark red")
enemy2.penup()
enemy2.speed(1000)
enemy2.setposition(randint(-300,300),randint(-300,300))
enemy2.speed(0)



# case count and defines

case = 0
enemy_speed= 5

def case(x):
    global enemy_speed

    
while True:
    player.forward(speed)
    enemy1.forward(10)
    enemy2.forward(10)
    case = randint(0,5)
    if case ==0:
        enemy1.forward(enemy_speed)
        enemy2.left(enemy_speed)
    elif case == 1:
        enemy1.left(randint(0,95))
        enemy2.right(enemy_speed)
    elif case == 2:
        enemy1.right(randint(0,95))
        enemy2.forward(enemy_speed*10)
    elif case == 3:
        enemy1.forward(enemy_speed * 10)
        enemy2.forward(enemy_speed*3)
    elif case == 4:
        enemy1.forward(enemy_speed * 3)
        enemy2.forward(enemy_speed)
    elif case == 5:
        enemy1.left(randint(0,90))
        enemy2.right(randint(0,90))
    #Boundaries
    
    boundaries(player)
    boundaries(enemy1)
    boundaries(enemy2)
    
    #gameend
    
    if uzaklik(player.xcor(),enemy1.xcor(),player.ycor(),enemy1.ycor()) < 40:
        end = turtle.Turtle()
        end.penup()
        end.ht()
        end.speed(802)
        end.color("white")
        end.setpos(-200,0)
        end.write("YOU LOSE!", font=("Arial",50,"bold"))
        break
    if uzaklik(player.xcor(),enemy2.xcor(),player.ycor(),enemy2.ycor()) < 40:
        end = turtle.Turtle()
        end.penup()
        end.ht()
        end.speed(802)
        end.color("white")
        end.setpos(-200,0)
        end.write("YOU LOSE!", font=("Arial",50,"bold"))
        break
