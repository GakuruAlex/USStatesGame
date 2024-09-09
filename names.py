from turtle import Turtle

class Names:

    def write_name(self, location: tuple, user_guess: str):
        turtle = Turtle()
        turtle.penup()
        turtle.hideturtle()
        turtle.color("black")
        turtle.goto(location)
        turtle.write(f"{user_guess.title()}")
