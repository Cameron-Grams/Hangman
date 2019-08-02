import random
import play_game as pg

words = ["obstacle", "onion", "ice cream", "chair"]

target_word = random.choice(words)

word_guessed = ""

# while word_guessed != target_word:
#    pg.play_game(target_word, word_guessed)

pg.play_game(target_word, letters_guessed)

print("in main: ", target_word)
