# Lab05Ast.py
# "Turtle Graphics Shapes"
# This is the student, starting version of Lab 05A.


from turtle import * 
from time import sleep

setup(1300,700)

##################################      
#  Thick Initials  -  50 Points  #
#================================#
#  In order to receive credit,   #
#  these must be YOUR initials.  #  
##################################

speed(0)
width(15)
penup()
left(180)
forward(300)
right(90)
forward(150)
pendown()
right(180)
forward(300)
left(90)
a=0
while a<=9:
    forward(52.5)
    left(20)
    a+=1
left(70)
penup()
forward(300)
left(90)
forward(300)
left(90)
pendown()
forward(300)
right(90)
a=0
b=0
while b<2:
    while a<=9:
        forward(26.25)
        right(20)
        a+=1
    left(200)
    b+=1
    a=0


sleep(1)
reset()

##############
#  Pentagon  #
##############
speed(0)
a=0
while a<5:
    forward(100)
    left(72)
    a+=1


sleep(1)
reset()

####################
#  Double Diamond  #
####################
speed(0)
right(45)
a=0
b=0
while b<2:
    while a<4:
        forward(100)
        left(90)
        a+=1
    right(180)
    b+=1
    a=0



sleep(1)
reset()

##################
#  8 Point Star  #
##################
speed(0)
a=0
while a < 8:
    forward(200)
    right(135)
    a+=1



sleep(1)
reset()

######################
#  SOS in Morse Code #
######################
speed(0)
width(20)
penup()
right(180)
forward(250)

pendown()
right(180)
forward(10)
penup()
forward(30)
pendown()
forward(10)
penup()
forward(30)
pendown()
forward(10)
penup()
forward(30)
pendown()
forward(50)
penup()
forward(30)
pendown()
forward(50)
penup()
forward(30)
pendown()
forward(50)
penup()
forward(30)
pendown()
forward(10)
penup()
forward(30)
pendown()
forward(10)
penup()
forward(30)
pendown()
forward(10)
penup()
forward(30)

sleep(1)
reset()

#######################
#  Box in Box in Box  #
#######################

speed(0)
penup()
left(90)
forward(100)
left(90)
forward(100)
right(180)
pendown()
forward(200)
right(90)
forward(200)
right(90)
forward(200)
right(90)
forward(200)
right(90)
penup()
forward(40)
right(90)
forward(40)
left(90)
pendown()
forward(120)
right(90)
forward(120)
right(90)
forward(120)
right(90)
forward(120)
right(90)
penup()
forward(40)
right(90)
forward(40)
left(90)
pendown()
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
    
sleep(1)
reset()

#####################
#  Solid Staircase  #
#####################
speed(0)
left(180)
forward(200)
right(90)
forward(200)
right(90)
begin_fill()
a=5
while a > 0:
    forward(50)
    right(90)
    forward(50)
    left(90)
    a-=1
left(180)
forward(250)
right(90)
forward(250)
end_fill()



sleep(1)
reset()


################    
#  Weird Face  #
################
speed(0)
right(60)
forward(40)
left(60)
forward(100)
left(60)
forward(40)
right(60)
right(90)
forward(40)
right(30)
forward(40)
right(60)
forward(100)
right(60)
forward(40)
right(30)
forward(40)
penup()
forward(100)
right(30)
pendown()
forward(50)
right(120)
forward(50)
right(120)
forward(50)
left(180)
penup()
forward(95)
pendown()
left(60)
forward(50)
right(120)
forward(50)
right(120)
forward(50)



sleep(1)
reset()

#######################
#  Gold 5 Point Star  #
#######################

speed(0)
a=5
color("gold")
begin_fill()
while a > 0:
    forward(200)
    right(144)
    a -= 1
end_fill()


sleep(1)
reset()

##########################
# Thick Rainbow Hexagon  #
##########################
speed(0)
width(30)
right(120)
color("purple")
forward(100)
left(60)
color("blue")
forward(100)
left(60)
color("green")
forward(100)
left(60)
color("yellow")
forward(100)
left(60)
color("orange")
forward(100)
left(60)
color("red")
forward(100)


sleep(1)
reset()

####################################      
#  Half Thick Half Thin Snowflake  #
####################################




#sleep(1)
#reset()

#####################      
#  Thinning Spiral  #
#####################
speed(0)
penup()
left(180)
forward(550)
right(90)
forward(300)
right(90)
pendown()
width(70)
forward(1100)
right(90)
width(65)
forward(600)
right(90)
width(60)
forward(1100)
right(90)
width(55)
forward(500)
right(90)
width(50)
forward(1000)
right(90)
width(45)
forward(400)
right(90)
width(40)
forward(900)
right(90)
width(35)
forward(300)
right(90)
width(30)
forward(800)
right(90)
width(25)
forward(200)
right(90)
width(20)
forward(700)
right(90)
width(15)
forward(100)
right(90)
width(10)
forward(600)
right(90)
width(5)
forward(50)
right(90)
width(2)
forward(500)




sleep(1)

###########
#  House  #
###########






 
update()
done()


  