import turtle
import os
wn =turtle.Screen()
wn.title("Pong By Tanish Bhatia")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0


# paddle A 
paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

#paddle B
paddle_b=turtle.Turtle()
paddle_b.speed()
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)


# ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")

ball.penup()
ball.goto(0,0)
ball.dx=2
ball.dy=2
# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

#functions....
def paddle_a_up():
    y=paddle_a.ycor()
    y=y+20
    paddle_a.sety(y)

#keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up,"q")

def paddle_a_down():
    y=paddle_a.ycor()
    y=y-20
    paddle_a.sety(y)
wn.listen()
wn.onkeypress(paddle_a_down,"a")    



def paddle_b_up():
    y=paddle_b.ycor()
    y=y+20
    paddle_b.sety(y)

#keyboard binding
wn.listen()
wn.onkeypress(paddle_b_up,"p")



def paddle_b_down():
    y=paddle_b.ycor()
    y=y-20
    paddle_b.sety(y)

#keyboard binding
wn.listen()
wn.onkeypress(paddle_b_down,"l")
#game loop......



while True:
    wn.update()
    
    
    
    #move the ball
    
    ball.setx(ball.xcor()+(ball.dx)/10)
    ball.sety(ball.ycor()+(ball.dy)/10)  
        # Border checking

    # Top and bottom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")
    
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")

    # Left and right
    if ball.xcor() > 350:
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    elif ball.xcor() < -350:
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    # Paddle and ball collisions
    if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.dx *= -1 
        os.system("afplay bounce.wav&")
    
    elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1
        os.system("afplay bounce.wav&")