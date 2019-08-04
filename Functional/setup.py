import random

words = ["obstacle", "onion", "ice cream", "chair"]
target_word = random.choice(words)

scaffold = [
        ["-----", "-----", "-----"],
        [ " ", " ", " " ],
        ["--", "\u00AC"," "],
        [ " ", " ", " " ],
        [ " ", " ", " " ],
        [ " ", " ", " " ],
        [ " ", " ", " " ],
        [ " ", " ", " " ],
        ["-----", "-----", "-----"]
        ]

def start_game():
    guessed_word = "_" * len(target_word)
    return(target_word, guessed_word, scaffold)


