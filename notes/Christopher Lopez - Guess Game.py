import random
answer = random.randint(1, 10)

print("Guess Game!")
print()


playing = True
guesses_left = 5


while guesses_left > 0 and playing:
    Guess = int(input("Guess a number 1-10:"))
    if Guess > answer:
        print("Lower")
        guesses_left -= 1

    elif Guess < answer:
        print("Higher")
        guesses_left -= 1
    else:
        playing = False
        print("YOU WIN!!!!! YAY!!!!!!")
