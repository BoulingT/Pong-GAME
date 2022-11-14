import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

RIGHT_PADDLE = (350, 0)
LEFT_PADDLE = (-350, 0)
#Creating screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

#Creating score settings
score = Scoreboard()

#Creating the right paddle
r_paddle = Paddle(RIGHT_PADDLE)
l_paddle = Paddle(LEFT_PADDLE)

#Ball settings
ball = Ball()

#Control settings
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "z")
screen.onkey(l_paddle.down, "s")




#Game
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.ball_movement()
    #Detect if ball out of the field
    if ball.xcor() > 400:
        ball.home()
        score.l_point()
        ball.bounce_x()
    #left player
    if ball.xcor() < -400:
        ball.home()
        score.r_point()
        ball.bounce_x()
    #Detect collision with wall
    if ball.ycor() > 275 or ball.ycor() < -275:
        ball.bounce_y()
    #Detect collision with paddles
    if (ball.distance(r_paddle) < 50 and ball.xcor()) > 330 or (ball.distance(l_paddle) < 50 and ball.xcor() < -330):
        ball.bounce_x()





screen.exitonclick()

#RAQUETTE CONTROL
#SECOND RAQUETTE
#BALL MOVEMENT
#BALL COLLISION AND BOUNCE WITH WALL
#BALL COLLISION WITH PADDLE
#SCORING POINT
#SCORE

