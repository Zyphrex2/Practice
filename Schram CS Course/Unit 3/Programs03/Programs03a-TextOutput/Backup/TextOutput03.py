# TextOutput03.py
# By default, the <print> command "ends" by going to
# the next line -- as if it pressed the <enter> key.
# However, you can change what happens at the <end>
# of a <print> command.  This allows multiple outputs
# to be on the same line.  In the particular example,
# the <end> values are spaces, so the first 3 outputs
# are all on the same line, separated by spaces.
# Note that "Line4" is displayed on its own line.
# This is because "Line3" was displayed with a normal
# <print> command without an <end>.


print("Line1",end = " ")
print("Line2",end = " ")
print("Line3")
print("Line4")

