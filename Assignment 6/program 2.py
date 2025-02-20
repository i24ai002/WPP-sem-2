import random

class Rock_Paper_Scissors:
    def __init__(self, rounds):
        self.rounds = rounds
        self.user_wins = 0
        self.comp_wins = 0

    def play_round(self):
        choices = {-1: "Rock", 0: "Paper", 1: "Scissors"}
        user_choice = int(input("Enter -1 (Rock), 0 (Paper), or 1 (Scissors): "))
        while user_choice not in choices:
            print("Invalid choice. Try again.")
            user_choice = int(input("Enter -1 (Rock), 0 (Paper), or 1 (Scissors): "))

        comp_choice = random.choice([-1, 0, 1])

        print(f"You chose {choices[user_choice]}, Computer chose {choices[comp_choice]}.")

        if user_choice == comp_choice:
            print("It's a draw!")
        elif (user_choice == -1 and comp_choice == 1) or (user_choice == 1 and comp_choice == 0) or (user_choice == 0 and comp_choice == -1):
            print("You win this round!")
            self.user_wins += 1
        else:
            print("Computer wins this round!")
            self.comp_wins += 1

    def play_game(self):
        for i in range(self.rounds):
            self.play_round()

        print(f"\nFinal Score - You: {self.user_wins}, Computer: {self.comp_wins}")
        if self.user_wins > self.comp_wins:
            print("You won the game!!")
        elif self.user_wins < self.comp_wins:
            print("Computer won the game!!")
        else:
            print("It's a tie!")


rounds = int(input("Enter total rounds: "))
game = Rock_Paper_Scissors(rounds)
game.play_game()


    