# MouseEvents08.py
# This program draws a small red  
# square at every click location.


from Graphics import *


def display(x,y):
   x,y = traditionalXY(x,y)
   fillRectangle(x-7,y-7,x+7,y+7)
   update()



##########
#  MAIN  #
##########

beginGrfx(1300,700)
setColor("red")
onscreenclick(display)
endGrfx()
   