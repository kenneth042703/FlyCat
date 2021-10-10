import turtle
import os
player1 = 1
player2 = 1
b = 1
wn = turtle.Screen()
wn.title("FlyCat by @Kenneth C. Ritualo")
wn.bgpic('bg.png')
wn.setup(width=1330, height=780)
wn.tracer(10)
wn.addshape('fire2.gif')
wn.addshape('fire.gif')
wn.addshape('cat.gif')
wn.addshape('cat2.gif')
wn.addshape('mcat.gif')
wn.addshape('mcat2.gif')
#Character
character = turtle.Turtle()
character.speed(0)
character.shape('cat.gif')
character.shapesize(stretch_len=2, stretch_wid=2)
character.penup()
character.goto(0, 0)

#Character
character2 = turtle.Turtle()
character2.speed(0)
character2.shape("cat2.gif")
character2.shapesize(stretch_len=2, stretch_wid=2)
character2.penup()
character2.goto(0, 0)


#Obstacle
obstacle = turtle.Turtle()
obstacle.speed(0)
obstacle.shape('fire.gif')
obstacle.shapesize(stretch_len=3, stretch_wid=3)
obstacle.penup()
obstacle.goto(300, 300)
obstacle.dx = 2
obstacle.dy = -2

#Obstacle2
obstacle2 = turtle.Turtle()
obstacle2.speed(0)
obstacle2.shape('fire.gif')
obstacle2.shapesize(stretch_len=3, stretch_wid=3)
obstacle2.penup()
obstacle2.goto(-300, -300)
obstacle2.dx = -1
obstacle2.dy = -2

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("Black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)



def up():
    y = character2.ycor()
    y+=60
    character2.sety(y)

def left():
    x = character2.xcor()
    x+=-60
    character2.shape('mcat2.gif')
    character2.setx(x)


def right():
    x = character2.xcor()
    x+=60
    character2.shape('cat2.gif')
    character2.setx(x)
def down():
    y = character2.ycor()
    y+=-60
    character2.sety(y)

def up2():
    y = character.ycor()
    y+=60
    character.sety(y)

def left2():
    x = character.xcor()
    x+=-60
    character.shape('mcat.gif')
    character.setx(x)

def right2():
    x = character.xcor()
    x+=60
    character.shape('cat.gif')
    character.setx(x)
def down2():
    y = character.ycor()
    y+=-60
    character.sety(y)

wn.listen()
wn.onkeypress(down, "Down")
wn.onkeypress(left, "Left")
wn.onkeypress(up, "Up")
wn.onkeypress(right, "Right")
wn.onkeypress(down2, "s")
wn.onkeypress(left2, "a")
wn.onkeypress(up2, "w")
wn.onkeypress(right2, "d")


while True or b<=10000000:
    wn.update()
    
    obstacle.setx(obstacle.xcor() + obstacle.dx)
    obstacle.sety(obstacle.ycor() - obstacle.dy)
    obstacle2.setx(obstacle2.xcor() + obstacle2.dx)
    obstacle2.sety(obstacle2.ycor() + obstacle2.dy)
    character.sety(character.ycor()+1)
    character2.sety(character2.ycor()+1)
    b+=1
    pen.clear()
    pen.write("Player1: {} || Player2: {}".format(player1, player2), align="center", font=("Courier", 24, "bold"))
    if character.ycor() > 290: 
        character.goto(character.xcor(), -280)
    elif character.ycor() < -290: 
        character.goto(character.xcor(), 280)
    elif character.xcor()> 490:
        character.goto(-480, character.ycor())
    elif character.xcor()<-490:
        character.goto(480, character.ycor())
    if character2.ycor() > 290: 
        character2.goto(character2.xcor(), -280)
    elif character2.ycor() < -290: 
        character2.goto(character2.xcor(), 280)
    elif character2.xcor()> 490:
        character2.goto(-480, character2.ycor())
    elif character2.xcor()<-490:
        character2.goto(480, character2.ycor())
    if obstacle.ycor() > 290:
        obstacle.sety(290)
        obstacle.dy *= -1
    if obstacle.ycor() < -290:
        obstacle.sety(-290)
        obstacle.dy *= -1
    if obstacle.xcor() > 490:
        obstacle.setx(490)
        obstacle.dx *= -1
    if obstacle.xcor() < -490:
        obstacle.setx(-490)
        obstacle.dx *= -1
    if obstacle.xcor() > 0:
        obstacle.shape('fire.gif')
    if obstacle2.xcor() > 0:
        obstacle2.shape('fire.gif')
    if obstacle2.ycor() > 290:
        obstacle2.sety(290)
        obstacle2.dy *= -1
    if obstacle2.ycor() < -290:
        obstacle2.sety(-290)
        obstacle2.dy *= -1
    if obstacle2.xcor() > 490:
        obstacle2.setx(490)
        obstacle2.dx *= -1
    if obstacle2.xcor() < -490:
        obstacle2.setx(-490)
        obstacle2.dx *= -1
    if obstacle2.xcor() < 0:
        obstacle2.shape('fire2.gif')
    if obstacle2.xcor() < 0:
        obstacle2.shape('fire2.gif')
    if  (obstacle.xcor() < character.xcor() +100 and obstacle.xcor() > character.xcor() -100) and(obstacle.ycor() < character.ycor() +100 and obstacle.ycor() > character.ycor() -200):
        character.goto(0, 0)
        b+=100000000
        pen.clear()
        pen = turtle.Turtle()
        pen.speed(0)
        pen.color("Black")
        pen.penup()
        pen.hideturtle()
        pen.goto(0, 260)
        pen.write("Player1: 0 || Player2: 0", align="center", font=("Courier", 24, "normal"))

        player1=0
    if  (obstacle.xcor() < character2.xcor() +100 and obstacle.xcor() > character2.xcor() -100) and(obstacle.ycor() < character2.ycor() +100 and obstacle.ycor() > character2.ycor() -200):
        character2.goto(0, 0)
        b+=100000000
        pen.clear()
        pen = turtle.Turtle()
        pen.speed(0)
        pen.color("Black")
        pen.penup()
        pen.hideturtle()
        pen.goto(0, 260)
        pen.write("Player1: 0 || Player2: 0", align="center", font=("Courier", 24, "normal"))
        player2=0
        
    
    if  (obstacle2.xcor() < character.xcor() +100 and obstacle2.xcor() > character.xcor() -100) and(obstacle2.ycor() < character.ycor() +100 and obstacle2.ycor() > character.ycor() -200):
        character.goto(0, 0)
        b+=100000000
        pen.clear()
        pen = turtle.Turtle()
        pen.speed(0)
        pen.color("Black")
        pen.penup()
        pen.hideturtle()
        pen.goto(0, 260)
        pen.write("Player1: 0 || Player2: 0", align="center", font=("Courier", 24, "normal"))

        player1=0
    if  (obstacle2.xcor() < character2.xcor() +100 and obstacle2.xcor() > character2.xcor() -100) and(obstacle2.ycor() < character2.ycor() +100 and obstacle2.ycor() > character2.ycor() -200):
        character2.goto(0, 0)
        b+=100000000
        pen.clear()
        pen = turtle.Turtle()
        pen.speed(0)
        pen.color("Black")
        pen.penup()
        pen.hideturtle()
        pen.goto(0, 260)
        pen.write("Player1: 0 || Player2: 0", align="center", font=("Courier", 24, "normal"))
        player2=0


    if  character.ycor() ++ 20 or character.xcor() ++ 20 :
        player1+=5 
        player2+=5
    
    if player1 >= 14000:
        b+=1000000000
        wn.clearscreen()
        wn.bgcolor("black")
        pen2 = turtle.Turtle()
        pen2.speed(0)
        pen2.color("white")
        pen2.penup()
        pen2.hideturtle()
        pen2.goto(0, 0)
        pen2.write("PLAYER 1 WINS!!!", align="center", font=("Courier", 24, "normal"))
        pen.clear()
        
    elif player2 >= 14000:
        b+=1000000000
        wn.clearscreen()
        wn.bgcolor("black")
        pen2 = turtle.Turtle()
        pen2.speed(0)
        pen2.color("white")
        pen2.penup()
        pen2.hideturtle()
        pen2.goto(0, 0)
        pen2.write("PLAYER 2 WINS!!!", align="center", font=("Courier", 24, "normal"))
        pen.clear()
    elif player2 >= 13500 and player1 >=13500:
        b+=1000000000
        wn.clearscreen()
        wn.bgcolor("black")
        pen2 = turtle.Turtle()
        pen2.speed(0)
        pen2.color("white")
        pen2.penup()
        pen2.hideturtle()
        pen2.goto(0, 0)
        pen2.write("BOTH OF YOU WINS!!!", align="center", font=("Courier", 24, "normal"))
        pen.clear()