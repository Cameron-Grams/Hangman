def test_word(target_word, guessed_word):
    return( target_word == guessed_word)

def update_scaffold(scaffold, errors):
    hung_man = [ [' ', ' O', ' '],
                 ['-', ' |', ' -'],
                 [' ', ' ^ ', ' '],
                 [' ', '| |', ' ']
               ]
    


def play_game(target_word, guessed_word, letters_guessed, scaffold, errors):
    
    print( f"Current guessed word is: {guessed_word}" )
    print( f"Attempted letters: {'-'.join(letters_guessed)}" )
    guessed_list = list(guessed_word)
    current_guess = input("Guess a letter of the word: ")
    # guard against guessing a second time
    if current_guess in letters_guessed:
        print( f"You have already guessed {current_guess}. Try something else.")

        return(target_word, guessed_word, letters_guessed, errors)


    for i in range( len( target_word ) ):
        if (target_word[i] == current_guess):
            guessed_list[i] = current_guess
        else:
            errors += 1
            update_scaffold(scaffold, errors)
    letters_guessed.append(current_guess)

    guessed_word = "".join(guessed_list)

    return(target_word, guessed_word, letters_guessed, scaffold, errors)




