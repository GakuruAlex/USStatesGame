from turtle import Screen,Turtle
from u_s_states import USStates
from names import Names
def main()-> None:
    screen = Screen()
    turtle = Turtle()
    u_s_states = USStates()
    name = Names()
    game_is_on = True

    screen.title("U.S. States Game")
    image = "blank_states_img.gif"
    screen.register_shape(image)
    turtle.shape(image)
    counter = 0
    while game_is_on:
        no_states = len(u_s_states.data)
        user_answer = screen.textinput(title=f"{counter}/{no_states}",prompt="Enter a state: ")
        if u_s_states.check_state(user_answer):
            location = u_s_states.location_of_state(user_answer)
            name.write_name(location=location, user_guess=user_answer)
            counter += 1
        if counter == no_states:
            game_is_on = False


    screen.exitonclick()

if __name__ == "__main__":
    main()