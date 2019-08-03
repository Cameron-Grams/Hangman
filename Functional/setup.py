import random

words = ["obstacle", "onion", "ice cream", "chair"]
target_word = random.choice(words)

scaffold = [
        ["-----", "-----", "-----"],
        ["-", "\u00AC"," "],
        [ " ", " ", " " ],
        [ " ", " ", " " ],
        [ " ", " ", " " ],
        ["-----", "-----", "-----"]
        ]

def start_game():
    word_guessed = "_" * len(target_word)
    return(target_word, word_guessed, scaffold)


