import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
screen.listen()
screen.onkey(player.move, "Up")

car = CarManager()

score = Scoreboard()
game_is_on = True


while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_cars()

    for each_car in car.cars:
        if each_car.distance(player) < 20:
            game_is_on = False
            score.game_over()

    if player.is_at_finish():
        player.go_to_start()
        car.speed_increase()
        score.new_level()






screen.exitonclick()