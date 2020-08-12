from random import choice


class RPS:
    cpu = choice(["rock", "paper", "scissors"])
    beats = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

    def game(self, user_choice):
        if user_choice == self.cpu:
            print(f"There is a draw {self.cpu}")
        elif self.beats[user_choice] == self.cpu:
            print(f"Well done. Computer chose {self.cpu} and failed")
        else:
            print(f"Sorry, but computer chose {self.cpu}")


game = RPS()
game.game(input())
