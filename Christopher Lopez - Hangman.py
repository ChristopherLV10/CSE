import random
hangman_words = ["Grapefruit", "Pineapple", "Blueberries", "Apples", "Mango", "Strawberries", "Lemons", "Watermelon",
                 "Oranges"]

guesses = 8
playing = True
random.choice(hangman_words)
print(random.choice(hangman_words))
input("Enter a letter:")
if input == random.choice:
    
else:
    guesses = guesses - 1
