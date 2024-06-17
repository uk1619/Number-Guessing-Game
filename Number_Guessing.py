import random

answer = random.randrange(1,101)
chance = 0

while chance < 5:
    guess = int(input("Guess a number between 1 and 100: "))

    if guess == answer:
        print("You Won!")
        break
    if guess < answer:
        print("Go higher")
    if guess > answer:
        print("Go lower")

    chance += 1

    if chance == 5:
        print("You lost! The number was", answer)