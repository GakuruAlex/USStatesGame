from turtle import Turtle

class Names:

    def write_name(self, location: tuple, user_guess: str):
        """_Create a turtle and move it to given location, writing its name _

        Args:
            location (tuple): _Location of the state_
            user_guess (str): _Name of state given by user_
        """
        turtle = Turtle()
        turtle.penup()
        turtle.hideturtle()
        turtle.color("black")
        turtle.goto(location)
        turtle.write(f"{user_guess.title()}")
