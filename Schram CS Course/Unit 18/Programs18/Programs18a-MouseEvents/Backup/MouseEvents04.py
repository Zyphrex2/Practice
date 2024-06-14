# MouseEvents04.py
# This program will allow the user to select the computer's 
# operating system and use this information to properly 
# determine the button value of the right/2-finger click 
# and whether or not a middle-click exists.
# NOTE: There is no guarentee that the user will select 
#       the correct operating system.


from Graphics import *


def leftDisplay(x,y):
   global numLeftClicks
   clear()
   numLeftClicks += 1
   drawString("Number of left clicks: "+str(numLeftClicks),100,150,"Arial",28,"normal")
   drawString("Number of middle clicks: "+str(numMiddleClicks),100,250,"Arial",28,"normal")
   drawString("Number of right clicks: "+str(numRightClicks),100,350,"Arial",28,"normal")

def middleDisplay(x,y):
   global numMiddleClicks
   clear()
   numMiddleClicks += 1
   drawString("Number of left clicks: "+str(numLeftClicks),100,150,"Arial",28,"normal")
   drawString("Number of middle clicks: "+str(numMiddleClicks),100,250,"Arial",28,"normal")
   drawString("Number of right clicks: "+str(numRightClicks),100,350,"Arial",28,"normal")

def rightDisplay(x,y):
   global numRightClicks
   clear()
   numRightClicks += 1
   drawString("Number of left clicks: "+str(numLeftClicks),100,150,"Arial",28,"normal")
   drawString("Number of middle clicks: "+str(numMiddleClicks),100,250,"Arial",28,"normal")
   drawString("Number of right clicks: "+str(numRightClicks),100,350,"Arial",28,"normal")



##########
#  MAIN  #
##########

numLeftClicks = 0
numMiddleClicks = 0
numRightClicks = 0
right = 4
middle = 4

os = numinput("Select your OS:",
              "1 = Windows\n2 = Mac")
if os == 1 : # Windows
   middle = 2
   right = 3
if os == 2 : # Mac
   right = 2  
   numMiddleClicks = "N/A"

beginGrfx(800,500)
onscreenclick(leftDisplay,btn=1)  
onscreenclick(middleDisplay,btn=middle)
onscreenclick(rightDisplay,btn=right)
endGrfx()
   