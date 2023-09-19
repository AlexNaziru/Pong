from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Scoreboard
import time


screen = Screen()
screen.bgcolor("#34495E")#background color
screen.setup(width=800, height=600)
screen.title("Pong")#name of the screen
screen.tracer(0)#This function is used to turn turtle animation off and set a delay for update drawings

#paddle object
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

#ball object
ball = Ball()
#scroe object
score = Scoreboard()



screen.listen()#this is like an event listener in JS
#right paddle
screen.onkey(right_paddle.go_up, "Up")#up arrow key
screen.onkey(right_paddle.go_down, "Down")#down arrow key
#left paddle
screen.onkey(left_paddle.go_up, "w")#up W key
screen.onkey(left_paddle.go_down, "s")#down S key


game_is_on = True#this is so that the tracer will update with what i have put afte tracer() and appear on my screen
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #collision detection with the upper and down side of the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        #ball needs to bounce
        ball.bounce_y()
    #detecting collision on the right paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:#distance is a built in function of turtle
        ball.bounce_x()

    #detecting when the right paddle missed
    if ball.xcor() > 380:#right paddle is set at 350 pixels 
        ball.reset_position()#method in ball class
        score.left_point()

    #detecting the left paddle missed
    if ball.xcor() < -380:
        ball.reset_position()
        score.right_point()



screen.exitonclick()#if we do not put this function it will flash and exit 