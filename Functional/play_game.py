import display as d

def test_word(target_word, guessed_word):
    return( not target_word == guessed_word )

def play_game(target_word, guessed_word, letters_guessed, scaffold, errors):
    d.clear_display()
    d.display_scaffold(scaffold)

    
    print( f"Current guessed word is: {guessed_word}" )
    print( f"Attempted letters: {'-'.join(letters_guessed)}" )
    guessed_list = list(guessed_word)
    target_list = list(target_word)

    current_guess = input("Guess a letter of the word: ")

    # guard against guessing a second time
    if current_guess in letters_guessed:
        print( f"You have already guessed {current_guess}. Try something else.")
        return(target_word, guessed_word, letters_guessed, scaffold, errors)

    if( not current_guess in target_list ):
        errors += 1
        scaffold = d.update_scaffold(scaffold, errors)

    for i in range( len( target_word ) ):
        if (target_word[i] == current_guess):
            guessed_list[i] = current_guess

    if( errors >= 7):
        you_lose()


    letters_guessed.append(current_guess)

    guessed_word = "".join(guessed_list)

    return(target_word, guessed_word, letters_guessed, scaffold, errors)

def you_lose():
    print("Too Many guesses! Sorry, you lose...")

def victory( target_word, errors ):
    print( f"Congratulations! You guessed {target_word} with only {errors} incorrect guesses!")
