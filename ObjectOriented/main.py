from  Game import Game
import start as st
import words as w

target_word = st.get_word( w.words )

hangman = Game( target_word )

hangman.show_word()

hangman.correct_word()
