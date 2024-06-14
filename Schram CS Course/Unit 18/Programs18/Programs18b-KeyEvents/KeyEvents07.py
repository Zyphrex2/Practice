# KeyEvents07.py
# This program attempts to used the "space bar"
# to make the computer display "Hello".  It may
# seem to work at first, until you realize that
# typing ANY key will make the computer display 
# "Hello".


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
onkeypress(display," ")
endGrfx()
   