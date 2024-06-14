from Graphics import *

def background():
    color("tan")
    fillRectangle(0, 0, 1300, 700)
    pass

def tank():
    color("black")
    width(5)
    drawRectangle(200, 125, 1100, 700)

def water():
    color("cyan")
    fillRectangle(202, 127, 1098, 698)

def plant():
    color("green")
    width(30)
    def individualPlant(x, height):
        counter = 0
        for k in range(height):
            drawArc(x, (700 - counter * 60), 30, 30, 180, 0)
            counter += 1
            drawArc(x, (700 - counter * 60), 30, 30, 0, 180)
            counter += 1
    individualPlant(960, 4)
    individualPlant(860, 3)
    individualPlant(1055, 2)

def fish():
    color("red")
    fillOval(500, 400, 100, 50)
    fillPolygon([600,400,650,350,650,450])
    color("black")
    fillCircle(425, 390, 5)
    pass

def bubbles():
    width(1)
    color("white")
    def drawBubble(x, y, size):
        drawCircle(x, y, size)
        fillOval(x + (size/3), y - (size/3), size*0.5, size*0.25)
    drawBubble(360, 350, 30)
    drawBubble(400, 275, 25)
    drawBubble(380, 205, 20)

def drawFloor():
    color("tan")
    fillRectangle(200,700,1100,660)
    color("gray")
    fillPolygon([300,660,310,640,330,635,340,660])