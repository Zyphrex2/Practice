# MouseEvents12.py
# The only difference between this program and the previous program is that 
# in this one the calls to procedure <displayBoxes> have been commented out.
# Note that even though the boxes are not displayed, you can still click on 
# them... or at least, you can click on the area they occupied.

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
   #displayBoxes()
   if inside(x,y,100,100,250,250):
      setColor("red")
      drawString("You clicked inside the red square.",325,200,"Arial",36,"normal")   
   elif inside(x,y,100,300,250,450):
      setColor("green")
      drawString("You clicked inside the green square.",325,400,"Arial",36,"normal")   
   elif inside(x,y,100,500,250,650):
      setColor("blue")
      drawString("You clicked inside the blue square.",325,600,"Arial",36,"normal")   
   else:
      setColor("black")
      drawString("You did not click inside any of the squares.",150,80,"Arial",36,"normal")   
        
         
##########
#  MAIN  #
##########

beginGrfx(1300,700)
#displayBoxes()
onscreenclick(locate)
endGrfx()
   