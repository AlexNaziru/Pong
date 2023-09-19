from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("#BDC3C7")
        self.penup()
        self.hideturtle()#only write score
        self.left_score = 0
        self.right_score = 0
        self.update_score()

    #update score 
    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.left_score, align="center", font=("Courier", 80, "normal"))#the score 
        #right side score
        self.goto(100, 200)
        self.write(self.right_score, align="center", font=("Courier", 80, "normal"))


    #score point
    def left_point(self):
        self.left_score +=1
        self.update_score()

    def right_point(self):
        self.right_score +=1
        self.update_score()