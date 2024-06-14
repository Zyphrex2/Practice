# GraphicsLibrary18.py
# This program demonstrates 32 of the colors 
# that are available in Python.  For a complete
# list of all 140 colors, visit this website:
# https://www.w3schools.com/colors/colors_names.asp
# This program also demonstrates <fillCircle>.
# It also shows that you can put 2 Python 
# commands on the same line if you end the 
# first with a semicolon <;>


from Graphics import *

beginGrfx(1300,700)

radius = 100
      
setColor("red");          fillCircle(125,125,radius) 
setColor("orange");       fillCircle(275,125,radius)      
setColor("yellow");       fillCircle(425,125,radius) 
setColor("green");        fillCircle(575,125,radius) 
setColor("blue");         fillCircle(725,125,radius) 
setColor("purple");       fillCircle(875,125,radius) 
setColor("gray");         fillCircle(1025,125,radius) 
setColor("coral");        fillCircle(1175,125,radius) 

setColor("dark red");     fillCircle(125,275,radius) 
setColor("dark orange");  fillCircle(275,275,radius)      
setColor("gold");         fillCircle(425,275,radius) 
setColor("dark green");   fillCircle(575,275,radius) 
setColor("dark blue");    fillCircle(725,275,radius) 
setColor("magenta");      fillCircle(875,275,radius) 
setColor("dark gray");    fillCircle(1025,275,radius) 
setColor("beige");        fillCircle(1175,275,radius) 

setColor("pink");         fillCircle(125,425,radius) 
setColor("lavender");     fillCircle(275,425,radius)      
setColor("khaki");        fillCircle(425,425,radius) 
setColor("light green");  fillCircle(575,425,radius) 
setColor("light blue");   fillCircle(725,425,radius) 
setColor("tan");          fillCircle(875,425,radius) 
setColor("light gray");   fillCircle(1025,425,radius) 
setColor("turquoise");    fillCircle(1175,425,radius) 

setColor("brown");        fillCircle(125,575,radius) 
setColor("chartreuse");   fillCircle(275,575,radius)      
setColor("sky blue");     fillCircle(425,575,radius) 
setColor("spring green"); fillCircle(575,575,radius) 
setColor("steel blue");   fillCircle(725,575,radius) 
setColor("cyan");         fillCircle(875,575,radius) 
setColor("black");        fillCircle(1025,575,radius) 
setColor("misty rose");   fillCircle(1175,575,radius)

endGrfx()
