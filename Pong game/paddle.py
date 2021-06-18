from turtle import Turtle

MOVE = 20

class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(1, 5)
        self.right(90)
        self.goto(x,y)

    def up(self):
        self.bk(MOVE)

    def down(self):
        self.fd(MOVE)