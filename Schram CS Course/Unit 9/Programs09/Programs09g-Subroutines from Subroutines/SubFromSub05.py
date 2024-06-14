# SubFromSub05.py
# This program demonstrates that a function can also be 
# created from another function. In this case, the <gcf> 
# function is used to create the <lcm> function. 
# Example: LCM(A,B) = A * B / GCF(A,B)
# This program also demonstrates that you can call a 
# function if you know what it does and what parameters 
# it requires, but you do not necessarily need to know 
# how it works. This program also demonstrates how you 
# can break up a very long command and make it "wrap" 
# to the next line by using a backslash (\).


def gcf(a,b):
   while True:
      rem = a % b
      if rem == 0:
         return b
      else:
         a,b = b,rem
            

def lcm(a,b):
   return a * b // gcf(a,b)



##########
#  MAIN  #
##########

print()
num1 = eval(input("Enter 1st number  -->  "))
num2 = eval(input("Enter 2nd number  -->  "))
print()
print("The Greatest Common Factor of",num1, \
"and",num2,"is",gcf(num1,num2))
print()
print("The Least Common Multiple of",num1, \
"and",num2,"is",lcm(num1,num2))
 