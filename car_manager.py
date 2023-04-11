from turtle import Turtle
import random
import time


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.goto(x=300, y=random.randint(-250, 250))
            new_car.seth(180)
            new_car.speed = STARTING_MOVE_DISTANCE
            self.all_cars.append(new_car)


    def move_car(self):
        for car in self.all_cars:
            car.forward(car.speed)

    def increase_car_move_speed(self):
        for car in self.all_cars:
            car.speed += MOVE_INCREMENT



