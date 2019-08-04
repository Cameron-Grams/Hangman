import subprocess as sp

def clear_display():
    tmp = sp.call("clear", shell=True)

def display_scaffold(scaffold):
    for layer in scaffold:
      current_layer = "".join(layer)
      print(" ", current_layer)

def update_scaffold(scaffold, errors):
    hung_man = [ [' ', ' O', ' '],
                 ['-', ' |', ' -'],
                 [' ', ' ^ ', ' '],
                 [' ', '| |', ' ']
               ]
    if( errors == 1 ):
        scaffold[3][1] = hung_man[0][1]
    if( errors == 2 ):
        scaffold[4][1] = hung_man[1][1]
    if( errors == 3 ):
        scaffold[4][0] = hung_man[1][0]
    if( errors == 4 ):
        scaffold[4][2] = hung_man[1][2]
    if( errors == 5 ):
        scaffold[5][1] = hung_man[2][1]
    if( errors == 6 ):
        scaffold[6][1] = hung_man[3][1]
    return(scaffold)
 

