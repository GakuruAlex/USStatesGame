from turtle import Screen,Turtle

def main()-> None:
    screen = Screen()
    turtle = Turtle()
    screen.title("U.S. States Game")
    image = "blank_states_img.gif"
    screen.addshape(image)
    turtle.shape(image)
    
    screen.exitonclick()

if __name__ == "__main__":
    main()