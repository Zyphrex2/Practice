# Lab07Bst.py
# "Selection With Graphics"
# This is the student, starting version of Lab 07B.



from Graphics import *

beginGrfx(1300,700)

# Substitute your own name here.
drawHeading("David Bardan","7B")
     
shapeNum = numinput("Shape Selection", "1 = Line \n2 = Rectangle \n3 = Circle \n4 = Oval \n5 = Regular Octagon \n6 = Star \n7 = Burst")
colorNum = numinput("Color Selection", "1 = Red \n2 = Orange \n3 = Yellow \n4 = Green \n5 = Blue \n6 = Purple \n7 = Brown")
width(numinput("Width Selection", "Enter 1-100"))
if shapeNum != 1 and shapeNum != 7: isFilled = textinput("Want the shape filled?", "Enter Y for 'Yes' and N for 'No'.")

if colorNum == 1:
    setColor("red")
elif colorNum == 2:
    setColor("orange")
elif colorNum == 3:
    setColor("yellow")
elif colorNum == 4:
    setColor("green")
elif colorNum == 5:
    setColor("blue")
elif colorNum == 6:
    setColor("purple")
elif colorNum == 7:
    setColor("brown")
else:
    drawString("Error... Please enter a number from 1 - 7.", 200, 300,"Times New Roman", 40)

if shapeNum == 1:
    drawLine(200,350,1100,350)
elif shapeNum == 2:
    if isFilled == "Y": fillRectangle(200,200,1100,500)
    else: drawRectangle(200,200,1100,500)
elif shapeNum == 3:
    if isFilled == "Y": fillCircle(650,350,100)
    else: drawCircle(650,350,100)
elif shapeNum == 4:
    if isFilled == "Y": fillOval(650,350,200,100)
    else: drawOval(650,350,200,100)
elif shapeNum == 5:
    if isFilled == "Y": fillRegularPolygon(650,350,200,8)
    else: drawRegularPolygon(650,350,200,8)
elif shapeNum == 6:
    if isFilled == "Y": fillStar(650,350,200,5)
    else: drawStar(650,350,200,5)
elif shapeNum == 7:
    drawBurst(650,350,200,20)
else:
    drawString("Error... Please enter a number from 1 - 7.", 200, 300,"Times New Roman", 40)


        
endGrfx() 
  