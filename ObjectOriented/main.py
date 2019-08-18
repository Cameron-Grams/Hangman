from  Game import Game
import start as st
import words as w

play_game = False

target_word = st.get_word( w.words )

hangman = Game( target_word )

like_to_play = input("Would you like to play Hangman?")
like_to_play = like_to_play.upper()

print( f"entered like to play: {like_to_play}" )

if ( like_to_play == "Y" ) or ( like_to_play == "YES" ):
    play_game = True

while play_game: 
    hangman.guess()
    hangman.show_word()
    if hangman.correct_word():
        play_game = False
