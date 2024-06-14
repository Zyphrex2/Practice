# ParameterProcedures06.py
# This program demonstrates that different data types
# can be passed to the same procedure.  
# The <showStudentInfo> procedure is called 3 times.
# The first two procedure calls are proper.
# The third one has the arguments out of order
# which causes strange output.


def showStudentInfo(name, age, gpa, inState):
   print()
   print("Student Information:")
   print("Name:     ",name)
   print("Age:      ",age)
   print("GPA:      ",gpa)
   print("In-State: ",inState)
   
   

##########
#  MAIN  #
##########

showStudentInfo("John Smith", 22, 2.875, True)
showStudentInfo("Suzy Brown", 29, 3.999, False)
showStudentInfo(1.763, True, "Tom Jones", 27)
