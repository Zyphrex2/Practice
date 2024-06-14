# KeyEvents08.py
# This program corrects the issue of the previous
# program by using the string literal key symbol
# "space" instead of " ".


from Graphics import *


def display():  
   clear()
   setRandomColor()
   drawString("Hello",100,150,"Arial",28,"bold")
   update()  
   
   
   
##########
#  MAIN  #
##########


beginGrfx(800,500)
listen()
onkeypress(display,"space")
endGrfx()
   