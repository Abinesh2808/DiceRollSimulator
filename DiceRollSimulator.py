#Scerario: Two Users will roll the dice, who will reach a total count of 25 will win this game

from random import *
class Dice:
    def __init__(self):
        self.user_a_count = 0
        self.user_b_count = 0

    def result(self):
        if self.user_a_count >= 25:
            return "User A won the game"
        elif self.user_b_count >= 25:
            return "User B won the game"
    def user_a(self):
        while True:
            ip1 = input("User A, Enter Y to roll the dice: ")
            if ip1.lower() == "y":
                a = randint(1,6)
                self.user_a_count += a
                print(f"A got {a}, and total is {self.user_a_count}")
                break
            else:
                print("Enter a valid input")

    def user_b(self):
        while True:
            ip2 = input("User B, Enter Y to roll the dice: ")
            if ip2.lower() == "y":
                b = randint(1,6)
                self.user_b_count += b
                print(f"B got {b}, and total is {self.user_b_count}")
                break
            else:
                print("Enter a valid input")
    def play(self):
        while True:
            self.user_a()
            if self.user_a_count >= 25:
                print(self.result())
                break
            self.user_b()
            if self.user_b_count >= 25:
                print(self.result())
                break

obj = Dice()
obj.play()
