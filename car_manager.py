import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_car = []
        self.move_speed = STARTING_MOVE_DISTANCE

    def car_create(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(280, random.randint(-240, 240))
            new_car.setheading(180)
            new_car.shapesize(1, 2)
            self.all_car.append(new_car)

    def move(self):
        for new_car in self.all_car:
            new_car.fd(self.move_speed)

    def speed_increase(self):
        self.move_speed += MOVE_INCREMENT
