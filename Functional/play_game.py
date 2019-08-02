import display

def play_game(target_word, guessed_word, letters_guessed):
    print( f"Current guessed word is: {guessed_word}" )
    guessed_list = list(guessed_word)
    current_guess = input("Guess a letter of the word: ")
    # guard against guessing a second time
    if current_guess in letters_guessed:
        print( f"You have already guessed {current_guess}. Try something else.")

        return(target_word, guessed_word, letters_guessed)


    for i in range( len( target_word ) ):
        if (target_word[i] == current_guess):
            guessed_list[i] = current_guess
    letters_guessed.append(current_guess)

    guessed_word = "".join(guessed_list)


    print("returning main play_game, letters guessed: ", letters_guessed, " guessed word: ", guessed_word )
    return(target_word, guessed_word, letters_guessed)




