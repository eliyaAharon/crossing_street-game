from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.hideturtle()
        self.goto(-260, 250)
        self.display()

    def display(self):
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def level_up(self):
        self.clear()
        self.level += 1
        self.display()

    def game_over(self):
        self.color("red")
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
