import pandas as pd

class USStates:
    def __init__(self):
        self.data = {}
        self.states()

    def states(self):
        """_Read and process the state csv _
        """
        states_data =pd.read_csv("50_states.csv")
        states_names = states_data.state
        states_x = states_data.x
        states_y = states_data.y

        for i, state_name in enumerate(states_names):
            self.data[state_name]= (int(states_x[i]), int(states_y[i]))

    def check_state(self, user_guess: str) -> bool:
        """_Check if user input is one of the states_

        Args:
            user_guess (str): _user input_

        Returns:
            bool: _True if user input is in states else False_
        """
        return user_guess.title() in self.data.keys()
    def location_of_state(self, user_guess: str) -> tuple:
        """_Given a state return the location of the state_

        Args:
            user_guess (str): _The state user guessed_

        Returns:
            tuple: _location of state_
        """
        return self.data[user_guess.title()]

    def remove_state(self, user_guess: str) -> None:
        del self.data[user_guess.title()]
    def states_to_learn(self):
        unnamed_states =pd.DataFrame({"States": list(self.data.keys())}, index= range(1, len(self.data) + 1))
        unnamed_states.to_csv("./states_to_learn.csv")
