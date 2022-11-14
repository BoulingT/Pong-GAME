from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.turtlesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(position)

    def up(self):
        y_position = self.ycor()
        self.goto(y=y_position + 20, x=self.xcor())

    def down(self):
        y_position = self.ycor()
        self.goto(y=y_position - 20, x=self.xcor())





