import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# screem settings.
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
screen.onkey(player.move, "Up")
cars = CarManager()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.add_car()
    cars.move_cars()
    # check collision between the player and cars.
    for car in cars.cars:
        if player.distance(car) < 22:
            game_is_on = False
            scoreboard.game_over()
    # check success of the player.
    if player.ycor() > 280:
        player.restart_car_position()
        cars.increment_speed()
        scoreboard.level_up()

screen.exitonclick()
