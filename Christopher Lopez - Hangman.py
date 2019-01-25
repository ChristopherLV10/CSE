import random
hangman_words = ["Grapefruit", "Pineapple", "Blueberries", "Apples", "Mango", "Strawberries", "Lemons", "Watermelon",
                 "Oranges"]
letters_guessed = []
guesses = 8
playing = True
answer = random.choice(hangman_words)
letters_in_answer = list(answer)
hidden_word = list("*" * len(answer))


while guesses > 0 and playing:
    if letters_in_answer == hidden_word:
        print("You got it! It is", answer)
        playing = False
        guesses = 0
        continue

    print(letters_guessed)
    print(hidden_word)
    letter = input("Enter a letter:")
    letters_guessed.append(letter)
    for i in range(len(letters_in_answer)):
        if letters_in_answer[i] == letter:
            hidden_word.pop(i)
            hidden_word.insert(i, letter)
    if letter not in answer:
        guesses = guesses - 1
        print("Wrong")
        print("Guesses Left:", guesses)
