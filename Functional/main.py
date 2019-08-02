import play_game as pg
import setup as st

target_word, guessed_word = st.start_game()

letters_guessed = []

# while word_guessed != target_word:
#    pg.play_game(target_word, word_guessed)


for guess in range(4):
    target_word, guessed_word, letters_guessed = pg.play_game(target_word, guessed_word, letters_guessed)

print("in main: ", target_word)
