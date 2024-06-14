# RepetitionWithGraphics08.py
# This program demonstrates several ovals.  
# All of the ovals have the same center and vertical  
# radius.  The horizontal radius keeps growing.
# NOTE: There may be a little delay in the display
# of the output.


from Graphics import *

beginGrfx(1300,700)

x = 650
y = 350
hr = 50
vr = 150

for k in range(30):
   drawOval(x,y,hr,vr)
   hr += 20
   
endGrfx()   