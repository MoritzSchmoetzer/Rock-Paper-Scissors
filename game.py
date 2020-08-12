from random import choice


class RPS:
    beats = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
    choices = ["rock", "paper", "scissors"]

    def game(self, user_choice):
        cpu = choice(self.choices)
        if user_choice not in self.choices:
            print("Invalid input!")
            pass
        else:
            if user_choice == cpu:
                print(f"There is a draw {cpu}")
            elif self.beats[user_choice] == cpu:
                print(f"Well done. Computer chose {cpu} and failed")
            else:
                print(f"Sorry, but computer chose {cpu}")


game = RPS()
while True:
    user_input = input()
    if user_input == "!exit":
        print("Bye!")
        break
    game.game(user_input)
