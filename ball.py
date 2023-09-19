#making our ball
from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("#BDC3C7")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1 #it means that the ball will change from 10 to -10 which will reverse its direction(-1 * 10 = -10) 

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()#reversing the balls direction when the right or left side isnt touched by the paddle