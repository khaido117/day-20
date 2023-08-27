from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.exitonclick()

screen.listen()
screen.onkey(f, "Up")

tim.heading(90)
tim.forward(90)

