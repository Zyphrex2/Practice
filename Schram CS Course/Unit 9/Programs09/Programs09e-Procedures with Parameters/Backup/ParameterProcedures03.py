# ParameterProcedures03.py
# This program demonstrates passing 2 arguments to a 
# procedure.  Procedure <showRectangleArea> is called twice.  
# In this case reversing the sequence of the arguments 
# is not a problem.


def showRectangleArea(L,W):
   area = L * W
   print()
   print("The rectangle area is",area)
   


##########
#  MAIN  #
##########

length = 100
width = 50
showRectangleArea(length,width)
showRectangleArea(width,length)
 