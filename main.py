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
screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.car_create()
    car.move()
    for new_car in car.all_car:
        if player.distance(new_car) < 50:
            game_is_on = False
            score.update_scoreboard()


screen.exitonclick()
