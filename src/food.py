from snake import Snake
import turtle, random


#Problem B.
class Food():
    '''
    Purpose: A food pellet
    Instance variables: self.pellet - a turtle object representing a food pellet;
    self.x - a randomized x coordinate; & self.y - a randomized y coordinate
    Methods: move_p(self) - a method for randomly placing a pellet
    '''
    def __init__(self):
        self.pellet = turtle.Turtle()
        self.pellet.speed(0)
        self.pellet.fillcolor('tomato')
        self.pellet.shape('circle')
        self.pellet.shapesize(1.5, 1.5)
        self.pellet.penup()
        self.x = 15 + 30*random.randint(0,19)
        self.y = 15 + 30*random.randint(0,19)
        self.pellet.setpos(self.x, self.y)

    def random_pos(self):
        self.x = 15 + 30*random.randint(0,19)
        self.y = 15 + 30*random.randint(0,19)
        self.pellet.setpos(self.x, self.y)