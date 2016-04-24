#-----Task Description-----------------------------------------------#
#
#  SKYLINES
#
#  This task tests your skills at defining functions, processing
#  data stored in lists and performing the arithmetic calculations
#  necessary to display a complex visual image.  The incomplete
#  Python script below is missing a crucial function,
#  "draw_buildings".  You are required to complete this function
#  so that when the program is run it produces a drawing of a city
#  skyline, using data stored in a list to determine the number,
#  proportions and styles of the buildings.  See the instruction
#  sheet accompanying this file for full details.
#
#--------------------------------------------------------------------#  



#-----Preamble and Test Data-----------------------------------------#
#
#

# Module provided
#
# You may use only the turtle graphics functions for this task

from turtle import *


# Given constants
#
# These constant values are used in the main program that sets up
# the drawing window - do not change any of these values

window_height = 600 # pixels
window_width = 1100 # pixels
half_width = window_width / 2 # maximum x coordinate in either direction
grass_depth = 75 # vertical depth of the "grass", in pixels
max_height = window_height - grass_depth # maximum positive y coordinate
offset = 5 # offset of the x-y coordinates from the screen's edge, in pixels
font_size = 10 # size of characters in the grid, in pixels
grid_size = 50 # gradations for the x and y scales shown on the screen


# Test data
#
# The following six lists each describe the set of buildings forming a city
# skyline.  The first four lists are special cases intended to help
# you debug your code (and make it easy for us to mark it).  The final
# two cases produce "realistic" looking skylines and should be
# used only when you have all of your building definitions working.
#
# Each list element specifies one building in four parts:
#
#    [width, height, x_coord_centreline, building_style]
#
# The 'width' and 'height' are the width and height of the building's main
# structure (including the roof, but excluding "add-ons" such as chimneys,
# antennae, etc).  The 'x_coord_centreline' is the x coordinate
# of the building's midpoint or centreline.  The 'building_style' is the
# unique building style; each style should differ in terms of shape, colour and
# 'additional elements' (doors, windows, balconys, advertising signs, etc).


# Skyline No. 1: All buildings the same style; decreasing heights
# from left to right; no overlaps
skyline_1 = [[ 50, 490, -470, 'style_A'],
             [265, 440, -308, 'style_A'],
             [100, 390, -120, 'style_A'],
             [148, 340,    7, 'style_A'],
             [290, 290,  230, 'style_A'],
             [120, 240,  440, 'style_A']]

### Skyline No. 2: All six different building styles; decreasing heights
### from left to right; no overlaps
skyline_2 = [[ 50, 490, -470, 'style_A'],
             [265, 440, -308, 'style_B'],
             [100, 390, -120, 'style_C'],
             [148, 340,    7, 'style_D'],
             [290, 290,  230, 'style_E'],
             [120, 240,  440, 'style_F']]
##
### Skyline No. 3: Different building styles and sizes; symmetrically
### arranged with the highest in the middle; buildings touching
skyline_3 = [[ 50, 190, -455, 'style_A'],
             [260, 290, -300, 'style_B'],
             [100, 390, -120, 'style_C'],
             [140, 490,    0, 'style_E'],
             [100, 390,  120, 'style_C'],
             [260, 290,  300, 'style_B'],
             [50, 190,   455, 'style_A']]
##               
### Skyline No. 4: Different styles; three 'layers' overlapped;
### increasing heights from left to right in each layer;
### decreasing heights from the furthest to the closest layer
skyline_4 = [[ 50, 400, -404, 'style_A'],
             [100, 430,  -60, 'style_A'],
             [160, 460,  300, 'style_B'],
             [ 40, 490,  460, 'style_B'],
             [170, 360,  400, 'style_C'],
             [250, 320,   85, 'style_C'],
             [160, 280, -200, 'style_D'],
             [170, 240, -420, 'style_D'],
             [164, 130, -380, 'style_E'],
             [300, 170,  -50, 'style_E'],
             [200, 210,  265, 'style_F'],
             [100, 250,  440, 'style_F']]
##
### Skyline No. 5: A more 'natural' looking Central Business
### District   
skyline_5 = [[ 45, 480, -160, 'style_D'],
             [150, 380, -200, 'style_A'],
             [100, 495,  -60, 'style_B'],
             [160, 450,  100, 'style_E'],
             [40,   490, 460, 'style_A'],
             [170, 390,  400, 'style_D'],
             [150, 360,   20, 'style_F'],
             [160, 280, -160, 'style_C'],
             [170, 440, -420, 'style_F'],
             [200, 300, -340, 'style_B'],
             [170, 100, -270, 'style_E'],
             [300, 170,  -50, 'style_D'],
             [200, 210,  265, 'style_C'],
             [100, 320,  440, 'style_F'],
             [130, 200, -420, 'style_A']]
##
### Skyline No. 6: Another 'realistic' CBD
skyline_6 = [[ 45, 460,  180, 'style_D'],
             [100, 495,  260, 'style_E'],
             [150, 380,  140, 'style_A'],
             [140, 430,  350, 'style_F'],
             [ 40, 490,  460, 'style_A'],
             [170, 350,  400, 'style_D'],
             [250, 240,  -10, 'style_F'],
             [160, 200, -160, 'style_B'],
             [170, 450, -420, 'style_F'],
             [200, 300, -340, 'style_D'],
             [170, 100, -270, 'style_F'],
             [300, 150,  -20, 'style_E'],
             [200, 210,  265, 'style_B'],
             [100, 300,  440, 'style_C'],
             [150, 200, -420, 'style_C']]

#***** If you want to create your own test data put it here

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the task by replacing the dummy function below with
#  your code

def draw_buildings(skyline):
    for value in range(len(skyline)): 
        building(skyline[value][0], skyline[value][1], skyline[value][2], skyline[value][3])
        value = value + 1

#Determine which building style to call
def building(width, height, x_coord_centreline, building_style): 
    goto(x_coord_centreline + (width / 2), 0)
    if building_style is 'style_A':
        style_A(width, height, x_coord_centreline)
    elif building_style is 'style_B':
        style_B(width, height, x_coord_centreline)
    elif building_style is 'style_C':
        style_C(width, height, x_coord_centreline)
    elif building_style is 'style_D':
        style_D(width, height, x_coord_centreline)
    elif building_style is 'style_E':
        style_E(width, height, x_coord_centreline)
    elif building_style is 'style_F':
        style_F(width, height, x_coord_centreline)


#-----Defining functions for shapes on the buildings-----#


def rectangle(width, height, colour):
    fill(True)
    color(colour)
    pendown()
    setheading(90)
    forward(height)
    left(90)
    forward(width)
    left(90)
    forward(height)
    left(90)
    forward(width)
    fill(False)
    penup()

#Draw a triangle using x_coord_centreline as a substitute to Pythagoras' Theorm
def triangle(width, height, x_coord_centreline, colour):
    fill(True)
    color(colour)
    setheading(90)
    pendown()
    forward(height / 3)
    goto(x_coord_centreline - (width / 2), height)
    setheading(0)
    forward(width)
    penup()
    fill(False)

#Draw an antenna on the left side of a building's roof
def antenna(width, height, x_coord_centreline):
    #Draw the antenna pole
    goto(x_coord_centreline - (width / 6), height)
    pensize(0.5)
    setheading(90)
    pendown()
    forward(20) 
    penup()
    #Draw the horizontal wire
    goto(x_coord_centreline, height + 10)
    setheading(180)
    pendown()
    forward(width / 3) 
    penup()
    #Draw the first vertical outer wire (right)
    goto(x_coord_centreline - ((width / 3) / 4), height + 15)
    setheading(270)
    pendown()
    forward(10) 
    penup()
    #Draw the second vertical outer wire (left)
    goto(x_coord_centreline - (((width / 3) / 4) * 3), height + 15)
    setheading(270)
    pendown()
    forward(10)
    penup()

#Draw a trapezium using x_coord_centreline as a substitue to Pythagoras' Theorem
def trapezium(width, height, x_coord_centreline, colour):
    fill(True)
    color(colour)
    setheading(0)
    forward(width / 2)
    left(120)
    goto(x_coord_centreline + ((width * 3 / 8)), height)
    setheading(180)
    forward(width - (width / 4))
    left(60)
    goto(x_coord_centreline - (width / 2), height - 50)
    fill(False)

#Draw a window and prepare for the drawing of another window below it
def window(width, height, space, colour):
    rectangle(width, height, colour)
    setheading(270) 
    forward(space)
    

#-----Defining functions for each building style-----#


def style_A(width, height, x_coord_centreline):
#Draw the initial building
    rectangle(width, height - 10, "violet")
#Draw an additional section on top of the initial building
    goto(x_coord_centreline, height - 10)
    rectangle((width / 3), 10, "violet")
    goto(x_coord_centreline + (width / 2 - 10), height - 50)
#Draw the initial windows
    for each in range((height - 75) / 20):      
        window((width - 20), 10, 20, "white")    
#Calculate the gap between the building's edge and the first and last windows
    space = 20 #The space allowal for the gap
    window_space = 15 #Width of the window plus the gap between windows
    if (width - space) % window_space < 5:   
        gap = 15                  
    else:
        gap = ((width - space) % window_space) / 2     
#Draw the lines which separate the windows
    for each in range((width - (space / 2)) / window_space):
        goto((x_coord_centreline - ((width - space) / 2)) + gap, 40)
        pensize(2)
        pencolor("violet")
        pendown()
        setheading(90)
        forward(height - 50)
        penup()
        gap = gap + window_space 
    antenna(width, height, x_coord_centreline)

def style_B(width, height, x_coord_centreline):
#Draw the initial building
    rectangle(width, height - (height / 3), "coral")
#Draw a triangle on top of the initial building
    goto(x_coord_centreline + (width / 2), height - (height / 3))
    triangle(width, ((height * 2) / 3), x_coord_centreline, "coral")
#Calculate the gap between the building's edge and the first and last windows
    window_space = 50 
    if width % window_space == 0: 
        gap = 37.5    
    else:           
        gap = (((width % window_space) + (window_space / 2))/ 2.0) + (window_space / 2)
#Draw the windows
    for row in range(width / window_space):
        goto((x_coord_centreline - (width / 2)) + gap, ((height * 2) / 3) - window_space)
        for each in range(((height * 2) / 3) / window_space):
            window(25, 25, window_space, "moccasin")
        gap = gap + window_space

def style_C(width, height, x_coord_centreline):
#Draw Initial building
    rectangle(width, height - (height / 4), "limegreen")
#Draw first additional top section
    goto(x_coord_centreline + (width / 4), height - (height / 4))           
    rectangle((width / 2), (height / 16), "limegreen")                      
#Draw second additional top section
    goto(x_coord_centreline + (width / 8), height - ((height * 3) / 16))
    rectangle((width / 4), (height / 16), "limegreen")                     
#Draw the central spire
    goto(x_coord_centreline, height - (height / 8))
    setheading(90)
    pendown()
    pensize(5)
    forward(height / 8) 
    penup()
    pensize(1)
#Draw the windows
    window_space = 80
    gap = 40
    for each in range(((height * 3) / 4) / (window_space - 10)):
        goto(x_coord_centreline + (width / 2) - 20, height - (height / 4) - gap)
        rectangle(width - 40, 20, "honeydew")
        gap = gap + window_space   

def style_D(width, height, x_coord_centreline):
#Draw initial building
    pensize(1)
    rectangle(width, height - ((width - 20) / 2), "steelblue")
#Draw a semicircle on top of the building
    goto(x_coord_centreline + (width / 2) - 10, height - ((width - 20) / 2))
    pendown()
    setheading(90)
    fill(True)
    circle(((width - 20) / 2), 180)         
    fill(False)
    penup()
    pencolor("paleturquoise")
#Draw an outline of the semicircle which extends down vertically to the ground
    goto(x_coord_centreline + (width / 2) - 10, 0)
    setheading(90)
    pendown()
    pensize(3) 
    forward(height - ((width - 20) / 2))
    circle(((width - 20) / 2), 180)
    forward(height - ((width - 20) / 2))
    penup()
#Draw the windows
    window_space = 20
    space = 20
    gap = 20 
    for each in range((height - (((width - space) / 2) + 40)) / 25):
        goto(x_coord_centreline + (width / 2) - space, height - ((width - space) / 2) - gap)
        setheading(180)
        pendown()
        forward(width - 40)
        penup()
        gap = gap + window_space
#Draw the doorway and outline
    goto(x_coord_centreline + ((width - 10)/ 4), 0)
    setheading(90)
    pendown()
    rectangle((width - 10) / 2, 40, "white")
    goto(x_coord_centreline + ((width - 10)/ 4), 0)
    pendown()
    setheading(90)
    pencolor("midnightblue")
    forward(40)
    left(90)
    forward((width - 10)/2)
    left(90)
    forward(40)
    penup()
    goto(x_coord_centreline, 0)
    setheading(90)
    pendown()
    forward(40)
    penup()

def style_E(width, height, x_coord_centreline):
#Draw the initial building
    goto(x_coord_centreline + ((width * 3) / 8), 0)
    rectangle(width - (width / 4), height - 50, "crimson")
#Draw the trapezium top
    goto(x_coord_centreline, height - 50)
    trapezium(width, height, x_coord_centreline, "crimson")
#Draw the windows
    window_space = (width / 3)
    gap = 0
    for column in range(2):     
        goto(x_coord_centreline - ((width - (width / 4)) / 4) + gap , height - (25 + width / 4))
        for each in range((height - 50) / window_space): 
            color("mistyrose")
            dot(width / 4)
            setheading(270)
            forward(width / 3)
        gap = gap + window_space

def style_F(width, height, x_coord_centreline):
#Draw the initial building
    rectangle(width, height - (width / 2), "cornsilk")                          
#Draw an additional section on top
    goto(x_coord_centreline + (width / 2) - (width / 8), height - (width / 2))
    rectangle(width * 3 / 4, width / 4, "cornsilk")                             
#Draw a semicircle on the top of the building
    goto(x_coord_centreline + (width / 2) - (width / 4), height - (width / 4))
    setheading(90)
    pendown()
    fill(True)
    circle(width / 4, 180)  
    fill(False)
    penup()
#Calculate the gap between the building's edge and the first and last windows 
    window_space = 20
    space = 20
    gap = ((((width - space) % window_space) + 5) / 2) + (window_space / 2)                 
#Draw the windows
    for each in range((width - space) / window_space):                   
        goto(x_coord_centreline - (width / 2) + 15 + gap, 10) 
        setheading(90)
        rectangle(15, height - (width / 2) - 20, "black")
        gap = gap + window_space

#
#--------------------------------------------------------------------#



#-----Main Program---------------------------------------------------#
#
# This main program sets up the drawing environment, ready for you
# to start drawing your buildings.  You may not change any of
# this code except the lines marked '*****'
    
# Set up the drawing window with coordinate (0, 0) at the
# centre of the "grass"
setup(window_width, window_height)
setworldcoordinates(-half_width, -grass_depth, half_width, max_height)
title('Skylines')

# Draw as quickly as possible by minimising animation
hideturtle()     #***** You may comment out this line while debugging
                 #***** your code, so that you can see the turtle
speed('fastest') #***** You may want to change the drawing speed
                 #***** while debugging your code

# Decide whether or not to draw the grid numbers
grid_on = True   #***** Make this False to avoid drawing the
                 #***** coordinates to produce a prettier picture

# Colour the sky                    
bgcolor('sky blue')

# Draw the grass
penup()
fillcolor('lawn green')
goto(-half_width, 0)
begin_fill()
forward(window_width)
right(90)
forward(grass_depth)
right(90)
forward(window_width)
end_fill()

# Draw x coordinates along the bottom of the screen (to aid
# debugging and marking)
if grid_on:
    for x_coord in range(-half_width + grid_size, half_width, grid_size):
        goto(x_coord, -grass_depth + offset)
        write('| ' + str(x_coord), font=('Arial', font_size, 'normal'))

# Draw y coordinates on the left-hand edge of the screen (to aid
# debugging and marking)
if grid_on:
    for y_coord in range(-grid_size, max_height, grid_size):
        goto(-half_width + offset, y_coord - offset)
        write(y_coord, font=('Arial', font_size, 'normal'))       

# Call the function to draw a skyline (using one of the lists
# skyline_1 to skyline_6)
draw_buildings(skyline_2) #***** Change the argument for different tests
    
# Exit gracefully
hideturtle()
done()

#
#--------------------------------------------------------------------#




