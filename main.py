import random

class game:
    name = "username"

    @staticmethod
    def get_random():
        return random.choice([1, 2, 3])

    @staticmethod
    def check_selection(choice: int):
        choice_lst = ["stone", "paper", "scissor"]
        if 1 <= choice <= 3:
            return choice_lst[choice-1]
        return "invalid"

    @staticmethod
    def decision_frame(user, system):
        if user == system:
            return "tie"

        if (system == 1 and user == 2) or (system == 2 and user == 3) or (system == 3 and user == 1):
            return "user"

        return "system"

    def greet_user(self):
        print(f"hello {self.name}, let's start!! :)")


class console_frames:
    name = "username"
    user = 0
    system = 0
    choice = 1

    @staticmethod
    def welcome_frame():
        frame_data = (
            "WELCOME TO THE STONE PAPER SCISSOR GAME :)\nYour options are:\n1. stone\n2. paper\n3. scissor"
        )
        print(frame_data)

    def choice_table(self):
        frame_data = f"|NAME : {self.name} |CHOICE : {game.check_selection(self.choice)} |"
        print(f"{'_'*len(frame_data)}\n{frame_data}\n{'-'*len(frame_data)}")

    @staticmethod
    def choice_system_choice(system: int):
        frame_data = f"|NAME : system |CHOICE : {game.check_selection(system)} |"
        print(f"{'_'*len(frame_data)}\n{frame_data}\n{'-'*len(frame_data)}")

    def win_table(self):
        frame_data = f"|{self.name} : {self.user} |SYSTEM : {self.system} |"
        print(f"{'_'*len(frame_data)}\n{frame_data}\n{'-'*len(frame_data)}")


if __name__ == "__main__":
    console_frames.welcome_frame()
    num_play_time = int(input("Enter the number of times you want to play\n>> "))
    user_score = 0
    system_score = 0
    user = input("Enter your name: ")
    game.name = user
    console_frames.name = user
    game().greet_user()

    for i in range(num_play_time):
        try:
            choice = int(input("Choice number (1=stone, 2=paper, 3=scissor)\n>> "))
            if choice not in [1, 2, 3]:
                print("Invalid choice, please select 1, 2, or 3.")
                continue
        except ValueError:
            print("Invalid input, please enter a number 1, 2 or 3.")
            continue

        system_choice = game.get_random()
        cf = console_frames()
        cf.choice = choice
        cf.choice_table()
        console_frames.choice_system_choice(system_choice)

        result = game.decision_frame(user=choice, system=system_choice)
        if result == "user":
            user_score += 1
            print(f"{user} wins this round!")
        elif result == "system":
            system_score += 1
            print("System wins this round!")
        else:
            print("This round is a tie!")

    cf.user = user_score
    cf.system = system_score
    cf.win_table()

    if user_score > system_score:
        print(f"Congratulations {user}, you won the game!")
    elif system_score > user_score:
        print("System won the game, better luck next time!")
    else:
        print("The game is a tie!")
