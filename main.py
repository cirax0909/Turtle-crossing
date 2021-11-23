import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
player = Player()
car = CarManager()
score = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.car_create()
    car.move()
    screen.listen()
    screen.onkey(player.move, "Up")

    for new_car in car.all_car:
        if new_car.distance(player) < 20:
            game_is_on = False
            score.update_scoreboard()

    if player.ycor() > 300:
        player = Player()
        score.update_level()
        car.speed_increase()

screen.exitonclick()
