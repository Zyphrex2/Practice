# Lab18Ast.py
# "Simple Paint Program"
# This is the student, starting version of Lab 18A.


from Graphics import *


def drawMenu(): # This procedure is complete.  Do not alter it!
   reset()
   drawHeading("John Smith","18A")
   setColor("red")
   fillRectangle(0,600,100,700)
   setColor("orange")
   fillRectangle(100,600,200,700)   
   setColor("yellow")
   fillRectangle(200,600,300,700)
   setColor("green")
   fillRectangle(300,600,400,700)   
   setColor("blue")
   fillRectangle(400,600,500,700)   
   setColor("purple")
   fillRectangle(500,600,600,700) 
   setColor("black")
   fillRectangle(600,600,700,700)   
   drawRectangle(700,600,800,700)   # pen up
   drawString("Pen",708,653,"Arial Narrow",24,"normal")
   drawString("Up",708,693,"Arial Narrow",24,"normal")
   drawRectangle(800,600,900,700)   #pen down
   drawString("Pen",808,653,"Arial Narrow",24,"normal")
   drawString("Down",808,693,"Arial Narrow",24,"normal")
   drawRectangle(900,600,1000,700)  # thin    
   drawLine(950,620,950,680) 
   drawRectangle(1000,600,1100,700) # medium
   fillRectangle(1045,620,1055,680) 
   drawRectangle(1100,600,1200,700) # thick
   fillRectangle(1138,620,1162,680) 
   drawRectangle(1200,600,1300,700) # reset
   drawString("Reset",1208,673,"Arial Narrow",24,"normal")
   update()
   penup()
   goto(0,25)
   showturtle()
   speed(1)
   pendown()


def settings(x,y):
   if inside(x,y,0,600,100,700):
      setColor("red") 
   #
   # Several elif commands need to be inserted here.
   #   
   elif inside(x,y,1200,600,1300,700): # Reset
      drawMenu() 

   update()                              
     

def moveUp():
   setheading(90)
   forward(100)   
   update() 
    
      
      
##########
#  MAIN  #
##########

beginGrfx(1300,700)
drawMenu()
listen()
onscreenclick(settings,btn=1)
onkey(moveUp,"Up")



update()
done()
