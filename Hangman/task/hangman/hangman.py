import random
import string


hidden_words = ("python", "java", "swift", "javascript")
FREE_SYMBOL = "-"
hidden_word = random.choice(hidden_words)
uncovered_letters = set()
suggested_letters = set()

MAX_ATTEMPTS = 8
msg = {
    "start": "H A N G M A N",
    "input": "Input a letter: ",
    "false": "That letter doesn't appear in the word.",
    "repeat": "You've already guessed this letter.",
    "long": "Please, input a single letter.",
    "invalid": "Please, enter a lowercase letter from the English alphabet.",
    "win": "You guessed the word {}!\nYou survived!",
    "unsolved": "Please, enter a lowercase letter from the English alphabet.",
    "end": "You lost!"
}


def hide_word(word, letters):
    result = ""
    for ch in word:
        result += ch if ch in letters else FREE_SYMBOL
    return result


def is_guess(word):
    return FREE_SYMBOL not in word


def go():
    print(msg["start"])
    attempts = MAX_ATTEMPTS
    is_win = False
    while attempts > 0 and not is_win:
        print("\n" + hide_word(hidden_word, uncovered_letters))
        letter = input(msg["input"])

        if len(letter) != 1:
            print(msg["long"])
        elif letter not in string.ascii_lowercase:
            print(msg["invalid"])
        elif letter in suggested_letters:
            print(msg["repeat"])
            attempts -= 1
        elif letter not in hidden_word:
            print(msg["false"])
            attempts -= 1
            suggested_letters.add(letter)
        else:
            uncovered_letters.add(letter)
            suggested_letters.add(letter)

        if is_guess(hide_word(hidden_word, uncovered_letters)):
            is_win = True

    if is_win:
        print("\n" + hidden_word)
        print(msg["win"].format(hidden_word))
    else:
        print("\n" + msg["end"])


if __name__ == "__main__":
    go()
