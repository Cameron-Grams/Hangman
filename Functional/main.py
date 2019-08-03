import play_game as pg
import setup as st
import display as d


target_word, guessed_word, scaffold = st.start_game()

letters_guessed = []
errors = 0

# while not pg.test_word(target_word == guessed_word):
#    target_word, guessed_word, letters_guessed = pg.play_game(target_word, guessed_word, letters_guessed)


for guess in range(4):

    target_word, guessed_word, letters_guessed, scaffold, errors = pg.play_game(target_word, guessed_word, letters_guessed, scaffold, errors)
    d.display_scaffold(scaffold)
#    d.clear_display()

