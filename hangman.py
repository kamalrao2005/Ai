import random
words = ["python", "computer", "programming", "hangman"]
word = random.choice(words)
guessed_word = ["_"] * len(word)
guessed_letters = []
attempts = 6
print("Welcome to Hangman Game!")
while attempts > 0 and "_" in guessed_word:
    print("\nWord:", " ".join(guessed_word))
    print("Guessed Letters:", guessed_letters)
    print("Attempts Left:", attempts)

    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue
    guessed_letters.append(guess)
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
        print("Correct guess!")
    else:
        attempts -= 1
        print("Wrong guess!")
if "_" not in guessed_word:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over! The word was:", word)
