# GraphicsLibrary26.py
# This program demonstrates that the <drawString>  
# procedure can have up to a total of 6 arguments.  
# The optional 4th, 5th and 6th arguments specify the 
# "Font Face" (name of the font), the "Font Size" and 
# the "Font Style" which can be <"normal">, <"bold">,
# <"italic"> or <"bold&italic">.


from Graphics import *

beginGrfx(1300,700)

drawString("Default font used by drawString: Arial 10-point normal font",20,40)
drawString("Courier 28-point normal font",20,100,"Courier",28,"normal")  
drawString("Courier 28-point bold font",20,160,"Courier",28,"bold")  
drawString("Times Roman 48-point normal font",20,260,"TimesRoman",48) # "normal" is default
drawString("Times Roman 48-point italic font",20,360,"TimesRoman",48,"italic")
drawString("Arial 68-point normal font",20,500,"Arial",68) 
drawString("Algerian 40-point bold&italic font ",10,600,"Algerian",40,"bold&italic")  
drawString("Arial 24-point normal font substituted for non-existent Qwerty font",20,680,"Qwerty",24) 

endGrfx()
