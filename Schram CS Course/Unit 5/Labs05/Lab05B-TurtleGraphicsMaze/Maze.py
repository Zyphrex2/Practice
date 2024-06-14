# Maze.py
# This file contains the necessary subroutines
# to generate the maze used by Lab05Bst.py
# Several of these subroutines were copied
# from Mr. Schram's <Graphics> library.
# No changes should me made to this file.
# Students really have no need to load 
# this file in the first place. 



from turtle import *
from math import *
from random import *


# Translates the x-coordinate from Traditional Graphics to Turtle Graphics.
def getX(x): 
   centerX = window_width() / 2 
   return int(x - centerX + 1)


# Translates the y-coordinate from Traditional Graphics to Turtle Graphics.
def getY(y):
   centerY = window_height() / 2 
   return int(centerY - y - 1)
   

# Translates the x-coordinate from Turtle Graphics to Traditional Graphics.
def actualX(x): 
   centerX = window_width() / 2 
   return int(x + centerX - 1)


# Translates the y-coordinate from Turtle Graphics to Traditional Graphics.
# Note: Technically, this function is identical to <getY>.
def actualY(y):
   centerY = window_height() / 2 
   return int(centerY - y - 1) 
   
   
# Translates the (x,y)-coordinate from Traditional Graphics to Turtle Graphics.
def turtleXY(x,y):
   return getX(x), getY(y)    
   
   
# Translates the (x,y)-coordinate from Turtle Graphics to Traditional Graphics.
def traditionalXY(x,y):
   return actualX(x), actualY(y)      


   
# Draws a line from (x1,y1) to (x2,y2)   
def drawLine(x1,y1,x2,y2):
   x1 = getX(x1)
   y1 = getY(y1)
   x2 = getX(x2)
   y2 = getY(y2)
   penup()
   goto(x1,y1)
   pendown()
   goto(x2,y2) 
   
      

# Displays text on the graphics screen at the (x,y)
# position with the <face>, <font> and <style> if specified.
# If not specified, the default font is used.  
def drawString(output,x,y,face="Arial",size=10,style="normal"):
   if style.lower() == "plain":
      style = "normal"  
   if style.lower() in ["bold&italic","bold+italic","both"]:
      style = ("bold","italic")      
   penup()
   setpos(getX(x),getY(y))
   write(output,font=(face,size,style)) 

  
# Draws a regular polygon with <numSides> sides that
# is inscribed in a circle with center (centerX,centerY)
# and radius (r).
def drawRegularPolygon(centerX,centerY,r,numSides):
   rotate = pi / 2
   if numSides < 2:
      numSides = 2
   if numSides % 2 == 0:
	   rotate = rotate + pi / numSides
   radian = 0
   count = 0
   step = 2 * pi / numSides
   halfSides = numSides // 2
   xStart = cos(radian - rotate) * r + centerX 
   yStart = sin(radian - rotate) * r + centerY
   x1 = xStart
   y1 = yStart
   while radian <= 2 * pi:
      radian = radian + step
      x2 = cos(radian - rotate) * r + centerX
      y2 = sin(radian - rotate) * r + centerY
      count = count + 1
      if numSides % 2 == 1:
         if count == halfSides:
            yTemp = y2
         elif count == halfSides+1: 
            y2 = yTemp   
      elif numSides % 4 == 0:
         if count == numSides // 2:
            yTemp1 = y2  
         elif count == numSides // 2 + 1:
            y2 = yTemp1       
         if count == 1:
            yTemp2 = y2  
         elif count == numSides:
            y2 = yTemp2      
      elif numSides % 4 == 2:                      
         if count == numSides // 2:
            yTemp1 = y2  
         elif count == numSides // 2 + 1:
            y2 = yTemp1       
         if count == 1:
            yTemp2 = y2  
         elif count == numSides:
            y2 = yTemp2                    
      drawLine(x1,y1,x2,y2)
      x1 = x2
      y1 = y2        
   drawLine(x2,y2,xStart,yStart)  
   

def fillOctagon(centerX,centerY,r):   
   begin_fill()
   drawRegularPolygon(centerX,centerY,r,8)
   end_fill()
   #update()
         

def drawMaze():
   tracer(0,0)
   hideturtle()
   seed(1038)
   color("darkgreen")
   for x in range(25,1276,50):
      for y in range(25,676,50):
         if not (x==y==25 or (x == 1275 and y == 675) or randint(1,5) >= 4) or (x == 1125 and y == 575) or (x == 1275 and y == 325) or (x == 1075 and y == 375) or (y == 525 and x in [575,625,775,1075]) or (y == 475 and x in [875,925]):
            fillOctagon(x,y,26)  
   color("black")          
   drawString("Start",5,19)   
   drawString("Finish",1250,701)       
   penup()
   goto(turtleXY(25,25))           
   width(3)
   color("red")
   pendown()
   showturtle()   
   tracer(1,10)  
   