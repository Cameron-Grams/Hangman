import subprocess as sp

tmp = sp.call("clear", shell=True)

scaffold = [ [' ', ' O', ' '],
             ['-', ' |', ' -'],
             [' ', ' ^ ', ' '],
             [' ', '| |', ' ']]

for layer in scaffold:
  current_layer = "".join(layer)
  print(current_layer)
