import random
hangman_words = ["Grapefruit", "Pineapple", "Blueberries", "Apples", "Mango", "Strawberries", "Lemons", "Watermelon",
                 "Oranges"]
word = []
guesses = 8
playing = True
random.choice(hangman_words)
input("Enter a letter:")
while guesses > 0 and playing:
    if input == random.choice:
        word. append(input)
    else:
        guesses = guesses - 1
        input("Enter a letter:")
print(guesses)