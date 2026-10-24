from turtle import Turtle
import random

SCREEN_SIDE_LENGTH = 600

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len= 0.5, stretch_wid= 0.5)
        self.color("blue")
        self.penup()
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x_position = random.randint(-SCREEN_SIDE_LENGTH//2 + 30, SCREEN_SIDE_LENGTH//2 - 30)
        random_y_position = random.randint(-SCREEN_SIDE_LENGTH//2 + 30, SCREEN_SIDE_LENGTH//2 - 30)
        self.goto(random_x_position, random_y_position)
