import turtle
from turtle import Turtle
import random
FONT = ("Courier", 16, "normal")

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.0001, stretch_wid=0.0001)
        # self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
        self.update_point()

    def update_point(self):
        self.clear()
        self.write(f"#", font=FONT)


