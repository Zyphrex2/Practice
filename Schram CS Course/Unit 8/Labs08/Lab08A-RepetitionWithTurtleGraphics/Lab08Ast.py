# Lab08Ast.py
# "Repetition with Turtle Graphics"
# This is the student, starting version of Lab 08A.
# After completing each shape, student need to "un-comment"
# the 4 commands which follow before they start the next shape.


from turtle import * 
from time import sleep

setup(1300,700)
tracer(0,0) 

while True:
    #######################
    #  Solid Red Octagon  #
    #######################
    color("red")
    begin_fill()
    for i in range(8):
        forward(100)
        left(45)
    end_fill()



    update()
    sleep(1)
    reset()
    tracer(0,0)


    ###################
    #  12 Point Star  #
    ###################

    for i in range(12):
        forward(300)
        right(150)




    update()
    sleep(1)
    reset()
    tracer(0,0)


    ###############
    #  Plus Sign  #
    ###############

    for i in range(4):
        forward(150)
        right(90)
        forward(100)
        right(90)
        forward(150)
        left(90)




    update()
    sleep(1)
    reset()
    tracer(0,0)


    ###############
    #  Snowflake  #
    ###############

    for i in range(18):
        width(5)
        forward(200)
        right(180)
        forward(200)
        left(170)
        width(1)
        forward(150)
        right(180)
        forward(150)
        left(170)




    update()
    sleep(1)
    reset()
    tracer(0,0)


    ############
    #  Circle  #
    ############

    for i in range(360):
        forward(2)
        right(1)



    update()
    sleep(1)
    reset()
    tracer(0,0)


    #############
    #  Zig-Zag  #
    #############
    penup()
    left(180)
    forward(600)
    left(90)
    forward(300)
    left(180)
    pendown()
    for i in range(12):
        forward(600)
        right(90)
        forward(50)
        right(90)
        forward(600)
        left(90)
        forward(50)
        left(90)



    update()
    sleep(1)
    reset()
    tracer(0,0)


    ##################
    #  Cool Pattern  #
    ##################

        





    #update()
    #sleep(20)
    #reset()
    #tracer(0,0)


    ##########################
    #  Flower of 10 Squares  #
    ##########################

    for i in range(10):
        for i in range(4):
            forward(150)
            right(90)
        right(36)




    update()
    sleep(1)
    reset()
    tracer(0,0)


    ##########################
    #  Flower of 12 Circles  #
    ##########################


    for i in range(12):
        for i in range(360):
            forward(2)
            right(1)
        right(30)



    update()
    sleep(1)
    reset()
    tracer(0,0)


    ##################################
    #  Comet a.k.a. Thickening Line  #
    ##################################
    left(180)
    forward(650)
    wid = 1
    right(180)
    for i in range(225):
        forward(5)
        wid += 1
        width(wid)





    update()
    sleep(1)
    reset()
    tracer(0,0)


    ################
    #  Box Spiral  #
    ################
    distance = 20
    for i in range(25):
        forward(distance)
        right(90)
        distance+=20




    update()
    sleep(1)
    reset()
    tracer(0,0)


    ##################
    #  Round Spiral  #
    ##################

    distance=1
    for i in range(153):
        forward(distance)
        right(10)
        if i%5 == 0:
            distance+=2

    update()
    sleep(1)
    reset()
    tracer(0,0)
