class Game( object ):
    def __init__( self, target_word ):
        self.target_word = target_word.upper()
        self.guessed_word = "_" * len( target_word )

        self.target_array = list(self.target_word)
        self.guess_array = []
        self.errors = 0

    def show_word(self):
        print( self.target_word )
        print( self.guessed_word )
        self.correct_word()

    def correct_word ( self ):
        print( self.target_word == self.guessed_word )
        return( self.target_word == self.guessed_word )
    
    def guess( self ):
        guessed_letter = ( input( "Guess a letter: " ) ).upper()
        if not guessed_letter in self.target_word:
            self.errors += 1
        for letter_index in len( target_word ):
            if target_word[ letter_index ] == guessed_letter:
                guess_array[ letter_index ] = guessed_letter

