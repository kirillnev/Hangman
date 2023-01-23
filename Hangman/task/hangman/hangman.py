import random

hidden_words = ("python", "java", "swift", "javascript")
hidden_word = hidden_words[random.randint(0, len(hidden_words) - 1)]

print("H A N G M A N")

input_word = input("Guess the word: ")
print("You survived!" if input_word == hidden_word else "You lost!")
