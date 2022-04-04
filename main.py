import turtle
import random
import time

'''
Estimates pi using Monte Carlo simulation

Virtual Dartboard has area 2 X 2 to accommodate unit circle
Total area is 4
Therefore, since area of unit circle = pi * radius^2 (and radius of 1 squared
  is 1), ratio of area of unit circle to area of board should be pi/4
  Theoretically, if you fill the entire board with darts, counting
  the number of darts that fall within the circle divided by the
  total number of darts thrown should give us that ratio (i.e., 1/4 * pi)
  Therefore, multiplying that result by 4 should give us an approx. of pi

Output to monitor:
  approximation of pi (float)
Output to window:
  colored dots that simulate unit circle on 2x2 square
Functions you must implement:
  drawSquare(myturtle=None, width=0, top_left_x=0, top_left_y=0, square_side_length=0) - to outline dartboard
  drawLine(myturtle=None, x_start=0, y_start=0, x_end=0, y_end=0) - to draw axes
  drawCircle(myturtle=None, radius=0) - to draw the circle
  setUpDartboard(myscreen=None, myturtle=None) - to set up the board using the above functions
  isInCircle(myturtle=None, circle_center_x=0, circle_center_y=0, radius=0, hit_color=None, miss_color=None) - determine if dot is in circle
  throwDart(myturtle=None, dartboard_length=0)
  playDarts(myturtle=None, dartboard_length=0) - a simulated game of darts between two players
  montePi(myturtle=None, num_darts=0) - simulation algorithm returns the approximation of pi
'''

#########################################################
#                   Your Code Goes Below                #
def drawAnything(myturtle=None,x=0,y=0):
  myturtle.color('black') #resets default color
  myturtle.down()
  myturtle.goto(x,y)
  myturtle.up()

def moveTurtle(myturtle=None, x=0, y=0):
  myturtle.color('black') #resets default color
  myturtle.up()
  myturtle.goto(x,y)
  myturtle.down()
  #drawAnything and moveTurtle function added to make code more dry

def drawSquare(myturtle=None, width=0, top_left_x=0, top_left_y=0, square_side_length=0):
  moveTurtle(myturtle=myturtle, x=top_left_x, y=top_left_y)
  for i in range(1,5):
    myturtle.forward(square_side_length)
    myturtle.right(90)

def drawLine(myturtle=None, x_start=0, y_start=0, x_end=0, y_end=0):
  moveTurtle(myturtle=myturtle, x=x_start, y=0)
  drawAnything(myturtle=myturtle, x=x_end, y=0)
  moveTurtle(myturtle=myturtle, x=0, y=y_start)
  drawAnything(myturtle=myturtle, x=0, y=y_end)

def drawCircle(myturtle=None, radius=0):
  myturtle.color('black')
  myturtle.up()
  myturtle.goto(0,-1*radius)
  myturtle.down()
  myturtle.speed(0) #otherwise it takes so long
  myturtle.circle(radius, steps=360) ##steps arg added by TA

def setUpDartboard(myscreen=None, myturtle=None, dartboard_length=0):
  myscreen.setworldcoordinates(-dartboard_length,-dartboard_length,dartboard_length,dartboard_length)
  drawLine(myturtle=myturtle, x_start=-dartboard_length, y_start=-dartboard_length, x_end=dartboard_length, y_end=dartboard_length)
  drawSquare(myturtle=myturtle, width=1, top_left_x=-dartboard_length/2, top_left_y=dartboard_length/2, square_side_length=dartboard_length) #since the dartboard is centered at the origin, top_left_x and top_left_y arguments are half dartboard length
  drawCircle(myturtle=myturtle, radius=1)

def isInCircle(myturtle=None, circle_center_x=0, circle_center_y=0, radius=0, hit_color=None, miss_color=None):
  dist_from_bullseye = myturtle.distance(circle_center_x, circle_center_y)
  boolean = dist_from_bullseye <= radius
  if boolean:
    myturtle.color(hit_color)
  else:
    myturtle.color(miss_color)
  myturtle.dot()
  return boolean

def throwDart(myturtle=None, dartboard_length=0):
  x_rand = random.uniform(-dartboard_length/2,dartboard_length/2)
  y_rand = random.uniform(-dartboard_length/2,dartboard_length/2)
  myturtle.up()
  myturtle.goto(x_rand,y_rand) 
  myturtle.dot()
  myturtle.up()

#########################################################

def playDarts(myturtle=None, dartboard_length=0):
  score_player_a = 0
  score_player_b = 0
  for i in range(1,11):
    throwDart(myturtle=myturtle, dartboard_length=dartboard_length)
    point_player_a = isInCircle(myturtle=myturtle, circle_center_x=0, circle_center_y=0, radius=1, hit_color='green', miss_color='red')
    if point_player_a:
      score_player_a += 1
    throwDart(myturtle=myturtle, dartboard_length=dartboard_length)
    point_player_b = isInCircle(myturtle=myturtle, circle_center_x=0, circle_center_y=0, radius=1, hit_color='green', miss_color='red')
    if point_player_b:
      score_player_b += 1
  print("Player A scored", score_player_a, "points, and Player B scored", score_player_b, "points.")
  if score_player_a > score_player_b:
    print("Player A wins!")
  elif score_player_a == score_player_b:
    print("It's a tie!")
  else:
    print("Player B wins!")
    #this function is more than 10 lines because there is a complex game between 2 players occuring

def montePi(myturtle=None, num_darts=0):
  inside_count = 0
  for i in range(0, num_darts):
    throwDart(myturtle=myturtle, dartboard_length=2)
    hit = isInCircle(myturtle=myturtle, circle_center_x=0, circle_center_y=0, radius=1, hit_color='green', miss_color='red')
    if hit:
      inside_count += 1
  pi_approx = (inside_count/num_darts)*4
  return pi_approx

#########################################################
#         Do not alter any code below here              #
#       Your code must work with the main proivided     #
#########################################################
def main():
    # Get number of darts for simulation from user
    # Note continuation character <\> so we don't go over 78 columns:
    print("This is a program that simulates throwing darts at a dartboard\n" \
        "in order to approximate pi: The ratio of darts in a unit circle\n"\
        "to the total number of darts in a 2X2 square should be\n"\
        "approximately  equal to pi/4")
    print("=========== Part A ===========")

    #Create window, turtle, set up window as dartboard
    window = turtle.Screen()
    darty = turtle.Turtle()
    darty.speed(0) # as fast as it will go!
    setUpDartboard(myscreen=window, myturtle=darty, dartboard_length=2)

    # Loop for 10 darts to test your code
    for i in range(10):
        throwDart(myturtle=darty, dartboard_length=2)
    print("\tPart A Complete...")
    print("=========== Part B ===========")
    darty.clear()
    setUpDartboard(myscreen=window, myturtle=darty, dartboard_length=2)
    playDarts(myturtle=darty, dartboard_length=2)
    print("\tPart B Complete...")
    # Keep the window up until dismissed
    print("=========== Part C ===========")
    darty.clear()
    setUpDartboard(myscreen=window, myturtle=darty, dartboard_length=2)
    
    # Includes the following code in order to update animation periodically
    # instead of for each throw (saves LOTS of time):
    BATCH_OF_DARTS = 5000
    window.tracer(BATCH_OF_DARTS)

    # Conduct simulation and print result
    number_darts = int(input("\nPlease input the number of darts to be thrown in the simulation:  "))
    approx_pi = montePi(darty, number_darts)
    print("\nThe estimation of pi using "+str(number_darts)+" virtual darts is " + str(approx_pi))
    print("\tPart C Complete...")
    # Don't hide or mess with window while it's 'working'
    # Keep the window up until dismissed
    print("=========== Part D ===========")
    darty.clear()
  #bullseye
    window.exitonclick()
'''
#main()

'''
darty=turtle.Turtle()
window = turtle.Screen()
setUpDartboard(myscreen=window, myturtle=darty, dartboard_length=2)
drawCircle(myturtle=darty, radius=0.125) 

target = isInCircle(myturtle=darty, circle_center_x=0, circle_center_y=0, radius=1, hit_color='green', miss_color='red')
bullseye = isInCircle(myturtle=darty, circle_center_x=0, circle_center_y=0, radius=0.125, hit_color='purple', miss_color='white')
for i in range(1,11):
  throwDart(myturtle=darty, dartboard_length=2)
  if bullseye:
    dart.color('blue')
    darty.write("Bullseye!")

window.exitonclick()