class Game( object ):
    def __init__( self, target_word ):
        self.target_word = target_word.upper()
        self.guessed_word = "_" * len( target_word )
        self.attempted_guesses = []
        self.target_array = list(self.target_word)
        self.guess_array = list( self.guessed_word )
        self.errors = 0

    def show_game_status( self ):
        print( f"So far you have guessed: { self.guessed_word }" ) 
        print( f"And attempted: { '-'.join( self.attempted_guesses ) }" )

    def correct_word ( self ):
        return( self.target_word == self.guessed_word )

    def you_lose( self ):
        print( f"You lose with { self.errors } incorrect guesses." )
        print( f"You failed to guess { self.target_word }." )
 
    def victory( self ):
        print( f"Congratulations! You guessed { self.guessed_word } with only { self.errors } errors." )
    
    def guess( self ):
        guessed_letter = ( input( "Guess a letter: " ) ).upper()

        if guessed_letter in self.attempted_guesses:
            print( f"You have already guessed { guessed_letter }" )
            return self.errors
        self.attempted_guesses.append( guessed_letter )

        if not guessed_letter in self.target_word:
            self.errors += 1
        for letter_index in range( len( self.target_word ) ):
            if self.target_word[ letter_index ] == guessed_letter:
                self.guess_array[ letter_index ] = guessed_letter
        self.guessed_word = "".join( self.guess_array )

        if self.errors == 6:
            self.you_lose()
        return self.errors
