from random import choice


class RPS:
    symbols = ["rock", "fire", "scissors", "snake", "human", "tree", "wolf", "sponge",
               "paper", "air", "water", "dragon", "devil", "lightning", "gun"]

    def __init__(self):
        self.points = 0
        self.game_options = None
        self.choices = None

    def welcome(self):
        user_name = input("Enter your name: ")
        print(f"Hello, {user_name}")
        file = open("rating.txt", "r+")
        for line in file:
            if user_name in line:
                self.points = int(line.split()[1])
        file.close()

    def options(self):
        user_input = input()
        if user_input == "":
            self.choices = ["rock", "paper", "scissors"]
        else:
            self.choices = list(user_input.split(","))
        print("Okay, let's start")

    def game(self):
        while True:
            user_input = input()
            if user_input == "!exit":
                print("Bye!")
                break
            elif user_input == "!rating":
                print(self.points)
                continue
            else:
                cpu = choice(self.choices)
                if user_input not in self.choices:
                    print("Invalid input!")
                else:
                    offset = (self.choices.index(cpu) - self.choices.index(user_input)) % len(self.choices)
                    if user_input == cpu:
                        print(f"There is a draw {cpu}")
                        self.points += 50
                    elif offset > len(self.choices) // 2:
                        print(f"Well done. Computer chose {cpu} and failed")
                        self.points += 100
                    else:
                        print(f"Sorry, but computer chose {cpu}")


game = RPS()
game.welcome()
game.options()
game.game()
