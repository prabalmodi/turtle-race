from turtle import *
from random import randint
import time
import numpy

# To set outout screen parameters
screen = Screen()
screen.bgcolor("light blue")
screen.setup(width=1.0, height=1.0)
ht()

# Number of tracks in race
steps = 10


# Drawing track
def draw_track():
    screen.tracer(0, 0)  # Won't show track drawing

    # Defining track initial position and color
    pen(speed=0, pencolor="White", pensize=10)
    pu()
    goto(-400, 400)
    pd()
    for i in range(steps):
        pu()
        right(90)
        fd(20)
        pd()
        for l in range(20):
            if l % 2 == 0:
                pd()
                fd(40)
                pu()
            else:
                pu()
                fd(40)
        backward(820)
        left(90)
        if(i == steps-1):
            pencolor("Black")
            write("Finish", align="center", font=("Times new roman", 30, "bold"))
            goto(0, 500)
            write("Press s to start", align="center", font=("Times new roman", 30, "bold"))
        fd(800/steps)
    ht()


# Turning on animation
screen.tracer(1, 1)

# Array of racing turtles
turtles = []

# Number of turtles taking part in race
num = 6


# Defining color of racing Turtles
Racer_colors = ["Red", "Blue", "Green", "Orange", "Black", "Maroon"]


def draw_racers():
    screen.tracer(1, 3)
    for i in range(num):
        turtles.append(Turtle())
        turtles[i].pen(pencolor=Racer_colors[i], fillcolor=Racer_colors[i], speed=1, pensize=1)
        turtles[i].shape("turtle")
        turtles[i].pu()
        turtles[i].goto(-430, 350-(840/num)*i)
        turtles[i].turtlesize(3, 3, 2)


# For graphics at the end of race
ds = Turtle()
ds.ht()  # Hiding Turtle


def draw_spiral(rad=200, Turtle=ds):
    ds.ht()
    screen.tracer(0)  # Animation off for spiral drawing

    def spiral():
        for i in range(rad):
            ds.pensize(10-(10/rad)*i)
            ds.circle(i, 20)
        ds.pu()
        ds.goto(-700, 0)
        ds.pd()
    ip = 0
    # Animating the Spiral
    while ip < 100:
        spiral()
        update()
        ds.clear()
        ip = (ip+0.5)
        ds.right(ip)

    ds.write("Press 'r' \nto restart", font=("Times new roman", 40, "bold"), align="center")
    screen.onkey(restart_race, "r")
    screen.listen()


# To store score of each racer
score = [0]*num


# To start the race
def start_race():
    score = [0]*num
    for j in range(130):
        for i in range(num):
            if(score[i] > 705):
                break
            movement = randint(1, 10)
            turtles[i].fd(movement)
            score[i] = score[i]+movement
    winner_index = numpy.argmax(score)
    goto(700, -100)

    # To create outline of text
    pencolor("White")
    write(Racer_colors[winner_index]+"\nTurtle\nWins", move=False, align="center", font=("Times new roman", 62, "normal"))
    pencolor(Racer_colors[winner_index])
    write(Racer_colors[winner_index]+"\nTurtle\nWins", move=False, align="center", font=("Times new roman", 60, "normal"))
    pd()
    ds.pencolor(Racer_colors[winner_index])
    time.sleep(1)
    draw_spiral()


# To restrat the race
def restart_race():
    clear()
    reset()
    draw_track()
    screen.tracer(1, 2)
    draw_racers()
    start_race()


draw_track()
draw_racers()

print("Press S to start the reace")

# Pressing "s" will start race
screen.onkey(start_race, "s")

# Taking input from keyboard
screen.listen()


# To save output image
def save_image():
    ts = getscreen()
    ts.getcanvas().postscript(file="duck.eps")


# Will not clost the output window
done()
