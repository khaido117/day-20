from turtle import Turtle, Screen
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
starting_x_position = [(0,0),(-20,0),(-40,0)]

segment = []

for snake_index in starting_x_position:
    new_snake = Turtle(shape="square")
    new_snake.penup()
    new_snake.color("white")
    new_snake.goto(snake_index)
    segment.append(new_snake)
    

game_is_on = True 
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for snake in segment:
        snake.forward(10)
        time.sleep(1)

screen.exitonclick()
