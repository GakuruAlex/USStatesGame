from turtle import Turtle
FONT = ("Arial", 24, "normal")
class Names:
    def __init__(self):
        self.turtle = Turtle()
        self.turtle.penup()
        self.turtle.hideturtle()
        self.turtle.color("black")

    def write_name(self, location: tuple, user_guess: str):
        """_Create a turtle and move it to given location, writing its name _

        Args:
            location (tuple): _Location of the state_
            user_guess (str): _Name of state given by user_
        """
        
        self.turtle.goto(location)
        self.turtle.write(f"{user_guess.title()}")

