import random


hidden_words = ("python", "java", "swift", "javascript")
FREE_SYMBOL = "-"
hidden_word = random.choice(hidden_words)
uncovered_letters = set()
MAX_ATTEMPTS = 8

msg_start = "H A N G M A N"
msg_input = "Input a letter: "
mgs_false = "That letter doesn't appear in the word."
msg_end = "Thanks for playing!"


def hide_word(word, letters):
    result = ""
    for ch in word:
        result += ch if ch in letters else FREE_SYMBOL
    return result


def go():
    print(msg_start)
    attempts = MAX_ATTEMPTS

    while attempts > 0:
        print("\n" + hide_word(hidden_word, uncovered_letters))
        letter = input(msg_input)

        if letter not in hidden_word:
            print(mgs_false)

        uncovered_letters.add(letter)
        attempts -= 1

    print("\n" + msg_end)


if __name__ == "__main__":
    go()
