# MouseEvents10.py
# This program uses "ranges" to determine
# if the user clicked inside a certain
# rectangular (or square) area of the screen.

from Graphics import *

def displayBoxes():
   setColor("red")
   fillRectangle(100,100,250,250)
   setColor("green")
   fillRectangle(100,300,250,450)
   setColor("blue")
   fillRectangle(100,500,250,650)
     
def locate(x,y):
   clear()
   displayBoxes()
   x,y = traditionalXY(x,y)
   if 100 <= x <= 250 and 100 <= y <= 250:
      setColor("red")
      drawString("You clicked inside the red square.",325,200,"Arial",36,"normal")    
   elif 100 <= x <= 250 and 300 <= y <= 450:
      setColor("green")
      drawString("You clicked inside the green square.",325,400,"Arial",36,"normal")   
   elif 100 <= x <= 250 and 500 <= y <= 650:
      setColor("blue")
      drawString("You clicked inside the blue square.",325,600,"Arial",36,"normal")  
   else:
      setColor("black")
      drawString("You did not click inside any of the squares.",150,80,"Arial",36,"normal")   
        
        
##########
#  MAIN  #
##########

beginGrfx(1300,700)
displayBoxes()
onscreenclick(locate)
endGrfx()
   