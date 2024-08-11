import turtle, random

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
        self.current_score = 0
        self.high_score = 0
        self.segments = []
        self.grow()
        self.vx = 30
        self.vy = 0
        self.score = None

    def u_score(self):
        self.score = turtle.Turtle()
        self.score.speed(0)
        self.score.shape("square")
        self.score.color("black")
        self.score.penup()
        self.score.hideturtle()
        self.score.goto(315, 610)
        self.score.write(
            "Score: {} High Score: {}".format(self.current_score, self.high_score),
            align="center",
            font=("Future", 20, "normal"),
        )

    def grow(self):
        head = turtle.Turtle()
        head.speed(0)
        head.fillcolor(self.color)
        head.shape('square')
        head.shapesize(1.5, 1.5)
        head.penup()
        head.setpos(self.x, self.y)
        self.segments.append(head)

    def restart(self):
        for seg in self.segments:
            seg.hideturtle()
        self.segments.clear() 
        self.current_score = 0 
        self.score.clear() 
        self.u_score()

    def move(self, pellet):
        if self.x == pellet.x and self.y == pellet.y:
            self.grow()
            self.current_score += 1
            pellet.random_pos()
            if self.current_score > self.high_score:
                self.high_score = self.current_score
            self.score.clear()
            self.u_score()
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