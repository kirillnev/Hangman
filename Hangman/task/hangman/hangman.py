import random


hidden_words = ("python", "java", "swift", "javascript")
FREE_SYMBOL = "-"
hidden_word = random.choice(hidden_words)
uncovered_letters = set()
MAX_ATTEMPTS = 8

msg_start = "H A N G M A N"
msg_input = "Input a letter: "
msg_false = "That letter doesn't appear in the word."
msg_repeat = "No improvements."
msg_win = "You guessed the word!\nYou survived!"
msg_end = "You lost!"


def hide_word(word, letters):
    result = ""
    for ch in word:
        result += ch if ch in letters else FREE_SYMBOL
    return result


def is_guess(word):
    return FREE_SYMBOL not in word



def go():
    print(msg_start)
    attempts = MAX_ATTEMPTS
    is_win = False
    while attempts > 0 and not is_win:
        print("\n" + hide_word(hidden_word, uncovered_letters))
        letter = input(msg_input)

        if letter in uncovered_letters:
            print(msg_repeat)
            attempts -= 1
        if letter not in hidden_word:
            print(msg_false)
            attempts -= 1

        uncovered_letters.add(letter)
        if is_guess(hide_word(hidden_word, uncovered_letters)):
            is_win = True

    if is_win:
        print("\n" + hidden_word)
        print(msg_win)
    else:
        print("\n" + msg_end)


if __name__ == "__main__":
    go()
