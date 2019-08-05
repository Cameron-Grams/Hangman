class Game( object ):
    def __init__( self, target_word ):
        self.target_word = target_word
        self.guessed_word = "_" * len( target_word )
        self.errors = 0

    def show_word(self):
        print( self.target_word )
        print( self.guessed_word )
        self.correct_word()

    def correct_word ( self ):
        print( self.target_word == self.guessed_word )
        return( self.target_word == self.guessed_word )