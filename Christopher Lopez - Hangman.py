import random
hangman_words = ["Grapefruit", "Pineapple", "Blueberries", "Apples", "Mango", "Strawberries", "Lemons", "Watermelon",
                 "Oranges"]
letters_guessed = []
guesses = 8
playing = True
answer = random.choice(hangman_words)
solved = False

while guesses > 0 and playing:
    print(letters_guessed)
    for i in range(len(hangman_words)):
        if hangman_words[i] == "letter":
            hangman_words.pop(i)
            hangman_words.insert(i, "*")
            print(answer)

    letter = input("Enter a letter:")
    letters_guessed.append(letter)
    if letter not in answer:
        guesses = guesses - 1
        print("Wrong")
        print("Guesses Left:", guesses)
    else:
        print(answer)

