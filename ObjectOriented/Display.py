import subprocess as sp

class Display( object ):
    def __init__( self ):
        self.scaffold = [
                ["-----", "-----", "-----"],
                [ " ", " ", " " ],
                ["--", "\u00AC"," "],
                [ " ", " ", " " ],
                [ " ", " ", " " ],
                [ " ", " ", " " ],
                [ " ", " ", " " ],
                [ " ", " ", " " ],
                ["-----", "-----", "-----"]
                ]


    def clear_display( self ):
        tmp = sp.call("clear", shell=True)

    def display_scaffold( self ):
        for layer in self.scaffold:
          current_layer = "".join(layer)
          print(" ", current_layer)

    def update_scaffold( self, errors ):
        hung_man = [ [' ', ' O', ' '],
                     ['-', ' |', ' -'],
                     [' ', ' ^ ', ' '],
                     [' ', '| |', ' ']
                   ]
        if( errors == 1 ):
            self.scaffold[3][1] = hung_man[0][1]
        if( errors == 2 ):
            self.scaffold[4][1] = hung_man[1][1]
        if( errors == 3 ):
            self.scaffold[4][0] = hung_man[1][0]
        if( errors == 4 ):
            self.scaffold[4][2] = hung_man[1][2]
        if( errors == 5 ):
            self.scaffold[5][1] = hung_man[2][1]
        if( errors == 6 ):
            self.scaffold[6][1] = hung_man[3][1]
        self.clear_display()
        self.display_scaffold()

