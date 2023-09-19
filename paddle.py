from turtle import Turtle


class Paddle(Turtle):
    #creating a paddle 
    def __init__(self, position):
        # call superclass
        super().__init__()#The super() builtin returns a proxy object (temporary object of the superclass) that allows us to access methods of the base class.
        self.shape("square")
        self.color("#BDC3C7")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

#methods inside our class
#moving the paddle
    def go_up(self):
        y_position = self.ycor() + 20
        self.goto(self.xcor(), y_position)

    def go_down(self):
        y_position = self.ycor() - 20
        self.goto(self.xcor(), y_position)