import subprocess as sp

def clear_display():
    tmp = sp.call("clear", shell=True)

def display_scaffold(scaffold):
    for layer in scaffold:
      current_layer = "".join(layer)
      print(current_layer)
