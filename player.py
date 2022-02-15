from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 15
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.left(90)
        self.go_to_start()

    def go_to_start(self):
        self.goto(0, -200)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def is_at_finish(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True

