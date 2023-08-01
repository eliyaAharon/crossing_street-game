from turtle import Turtle
from random import randint, choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        super().__init__()
        self.cars = []
        self.random_time = 1
        self.add_car()
        self.speed = MOVE_INCREMENT

    def add_car(self):

        if self.random_time == 1:
            new_car = Turtle()
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.goto(280, randint(-250, 250))
            new_car.shape("square")
            new_car.color(choice(COLORS))
            self.cars.append(new_car)
        self.random_time = randint(1, 7)

    def move_cars(self):
        for car in self.cars:
            car.goto(car.xcor() - self.speed, car.ycor())

    def increment_speed(self):
        self.speed += 2
