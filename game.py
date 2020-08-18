from random import choice


class RPS:
    beats = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
    choices = ["rock", "paper", "scissors"]

    def __init__(self):
        self.points = 0

    def welcome(self):
        user_name = input("Enter your name: ")
        print(f"Hello, {user_name}")
        file = open("rating.txt", "r+")
        for line in file:
            if user_name in line:
                self.points = int(line.split()[1])
        file.close()

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
                    if user_input == cpu:
                        print(f"There is a draw {cpu}")
                        self.points += 50
                    elif self.beats[user_input] == cpu:
                        print(f"Well done. Computer chose {cpu} and failed")
                        self.points += 100
                    else:
                        print(f"Sorry, but computer chose {cpu}")


game = RPS()
game.welcome()
game.game()
