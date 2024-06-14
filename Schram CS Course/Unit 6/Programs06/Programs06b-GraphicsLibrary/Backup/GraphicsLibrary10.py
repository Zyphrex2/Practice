# GraphicsLibrary10.py
# This program demonstrates the <drawArc> procedure of the 
# <Graphics> library.  An "arc" is a piece of an "oval".
# Like ovals, arcs are drawn from their center (x,y) with 
# a horizontal radius (hr) and a vertical radius (vr).  
# Arcs also require a starting and stopping degree value.  
# This is done with <drawArc(x,y,hr,vr,start,stop)>.


from Graphics import *

beginGrfx(1000,650)

drawArc(500,325,400,300,0,360)	# complete oval
drawArc(500,400,200,50,90,270)  	# bottom half of an oval
drawArc(500,400,200,100,90,270)
drawArc(350,200,80,20,270,90)   	# top half of an oval
drawArc(650,200,80,20,270,90)         
drawArc(123,325,100,100,180,0)  	# left half of an oval
drawArc(878,325,100,100,0,180)  	# right half of an oval
drawArc(490,325,10,20,270,360)  	# top-left 1/4 of an oval
drawArc(510,325,10,20,0,90)     	# top-right 1/4 of an oval
drawArc(70,325,20,30,180,90)    	# 3/4 of an oval
drawArc(930,325,20,30,270,180)  	# different 3/4 of an oval
drawPoint(350,200)
drawPoint(650,200)

endGrfx()
