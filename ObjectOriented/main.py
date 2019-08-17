from  Game import Game
import start as st
import words as w

play_game = False

target_word = st.get_word( w.words )

hangman = Game( target_word )

like_to_play = input("Would you like to play Hangman?")
like_to_play = like_to_play.upper()

if like_to_play == ("YES" or "Y"):
    play_game = True

while play_game: 
    hangman.guess()
    hangman.show_word()
    play_game = hangman.correct_word()
