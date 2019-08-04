import play_game as pg
import setup as st
import display as d


target_word, guessed_word, scaffold = st.start_game()

letters_guessed = []
errors = 0

check_word = True
check_errors = True

while check_word and check_errors :

    target_word, guessed_word, letters_guessed, scaffold, errors = pg.play_game(target_word, guessed_word, letters_guessed, scaffold, errors)
 
    check_word = pg.test_word(target_word, guessed_word)
    check_errors = errors < 7

    if( guessed_word == target_word):
        pg.victory( target_word, errors )



print("Game Over!")
