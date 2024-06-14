# GraphicsLibrary11.py
# This program may seem almost identical to the
# previous program which drew the smiley face.  
# In reality, it demonstrates what happens when
# arguments are put in the wrong order.  The 
# program does execute without any errors, but 
# the results are not what you expect.
# This is another example of a Logic Error.


from Graphics import *

beginGrfx(1000,650)

drawArc(325,500,400,300,0,360)
drawArc(500,400,50,200,90,270)
drawArc(400,500,200,100,270,90)
drawArc(200,350,20,80,270,90)
drawArc(650,200,80,20,90,270)
drawArc(123,325,100,100,0,180)
drawArc(878,325,100,100,180,0)
drawArc(490,325,10,20,270,360)
drawArc(325,510,10,20,90,0)
drawArc(325,70,20,30,90,270)
drawArc(930,325,30,20,270,180)
drawPoint(200,350)
drawPoint(650,200)

endGrfx()
