import turtle, random

#Problem A.
class Game:
    '''
    Purpose: The board on which the game is played
    Instance variables: self.player - the snake/person playing & self.pellet - the
    food pellets on the board
    Methods: gameloop(self) - a method that calls itself to either move the snake
    and continue the game or to end the game
    '''
    def __init__(self):
        turtle.setup(700, 700)
        turtle.setworldcoordinates(-40, -40, 640, 640)
        cv = turtle.getcanvas()
        cv.adjustScrolls()
        turtle.hideturtle()
        turtle.delay(0)
        turtle.tracer(0, 0) #Extra credit #4: game speed optimization
        turtle.speed(0)
        for i in range(4):
            turtle.forward(600)
            turtle.left(90)
        self.player = Snake(315, 315, 'green')
        self.pellet = Food()
        self.gameloop()
        turtle.onkeypress(self.player.go_down, 'Down')
        turtle.onkeypress(self.player.go_up, 'Up')
        turtle.onkeypress(self.player.go_left, 'Left')
        turtle.onkeypress(self.player.go_right, 'Right')
        turtle.listen()
        turtle.mainloop()

    def gameloop(self):
        self.player.move(self.pellet)
        if (self.player.selfcollision() is True) or (self.player.wallcollision() is True):
            turtle.write('GAME OVER GAME OVER', align='left', font=('Futura', 44, 'bold'))
        elif (self.player.selfcollision() is False) or (self.player.wallcollision() is False):
            turtle.ontimer(self.gameloop, 200)
            turtle.update()

class Snake():
    '''
    Purpose: The snake being controlled by the player
    Instance variables: self.x - the x coordinate of the head of the snake;
    self.y - the y coordinate of the head of the snake; self.color - the color
    of the snake; self.segments - a list containing the snake segments;
    self.vx - the velocity of the snake in the x direction; & self.vy - the
    velocity of the snake in the y direction
    Methods: grow(self) - a method for adding segments to the snake; move(self) -
    a method for moving the snake and checking for food pellets; go_down(self) -
    a method for moving the snake downwards; go_up(self) - a method for moving the
    snake upwards; go_left(self) - a method for moving the snake leftwards;
    go_right(self) - a method for moving the snake rightwards; wallcollision(self)
    - a method for checking if the snake hit the game's boundary; & selfcollision(self)
    - a method for checking if the snake hit itself.
    '''
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.segments = []
        self.grow()
        self.vx = 30
        self.vy = 0

    def grow(self):
        head = turtle.Turtle()
        head.speed(0)
        head.fillcolor(self.color)
        head.shape('square')
        head.shapesize(1.5, 1.5)
        head.penup()
        head.setpos(self.x, self.y)
        self.segments.append(head)

    def move(self, pellet):
        if self.x == pellet.x and self.y == pellet.y:
            self.grow()
            pellet.move_p()
        else:
            for i in range(len(self.segments)-1):
                self.segments[i].setpos(self.segments[i+1].xcor(), self.segments[i+1].ycor())
        self.x += self.vx
        self.y += self.vy
        self.segments[-1].setpos(self.x, self.y)

    def go_down(self):
        self.vx = 0
        self.vy = -30

    def go_up(self):
        self.vx = 0
        self.vy = 30

    def go_left(self):
        self.vx = -30
        self.vy = 0

    def go_right(self):
        self.vx = 30
        self.vy = 0
#Problem C.
    def wallcollision(self):
        if self.segments[-1].xcor() > 600 or 0 > self.segments[-1].xcor() or self.segments[-1].ycor() > 600 or 0 > self.segments[-1].ycor():
            return True
        else:
            return False

    def selfcollision(self):
        for i in range(len(self.segments)-1):
            if 15 > self.segments[i].distance(self.segments[-1]):
                return True
        return False

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

    def move_p(self):
        self.x = 15 + 30*random.randint(0,19)
        self.y = 15 + 30*random.randint(0,19)
        self.pellet.setpos(self.x, self.y)

Game()
