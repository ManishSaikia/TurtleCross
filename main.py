import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
screen.listen()
score = Scoreboard()
screen.onkey(key='Up', fun=player.move)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # generate random cars and move
    cars.create_car()
    cars.move()

    # Detect car collision
    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()

    # Detect a successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        cars.level_up()
        score.score_up()

screen.exitonclick()