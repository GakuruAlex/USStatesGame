from turtle import Screen,Turtle
from u_s_states import USStates
from names import Names
def main()-> None:
    screen = Screen()
    turtle = Turtle()
    u_s_states = USStates()
    name = Names()
    game_is_on = True

    screen.title("Name the  States Game")
    image = "blank_states_img.gif"
    screen.register_shape(image)
    turtle.shape(image)
    counter = 0
    while game_is_on:

        user_answer = screen.textinput(title=f"{counter}/50 States Correct",prompt="What's another state's name: ")
        if u_s_states.check_state(user_answer):
            location = u_s_states.location_of_state(user_answer)
            name.write_name(location=location, user_guess=user_answer)
            u_s_states.remove_state(user_guess= user_answer)
            counter += 1
        if counter == 50:
            name.end_game()
            game_is_on = False


    screen.exitonclick()

if __name__ == "__main__":
    main()