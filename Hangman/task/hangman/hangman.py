import random

hidden_words = ("python", "java", "swift", "javascript")
free_symbol = "-"
hidden_word = random.choice(hidden_words)
hint = hidden_word[:3] + free_symbol * (len(hidden_word) - 3)

print("H A N G M A N")

input_word = input(f"Guess the word {hint}: ")
print("You survived!" if input_word == hidden_word else "You lost!")
