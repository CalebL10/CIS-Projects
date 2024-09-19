"""
File: Project 7.1 (Draw_circle).py
Project 7.1

Draws a circle.

1. The inputs are the coordinates of the center point and the radius.

"""

import math
from turtle import Turtle

def drawCircle(t, x, y, radius):
    """Draws a circle with the given center point and radius."""
    t.up()
    t.goto(x, y)
    t.forward(radius)
    t.left(90)
    t.down()
    for x in range(120):
        t.left(3)
        t.forward(2 * math.pi * radius / 120)

def main():
    x = 50
    y = 75
    radius = 100
    drawCircle(Turtle(), x, y, radius)
    input()

if __name__ == "__main__":
    main()
