import random, turtle

def disp_xy(x, y):
    print("Clicked at", x, y)

turtle.onscreenclick(disp_xy)
turtle.listen()

#Warmup:
class Shape:
    '''
    Purpose: Some shape with coordinates
    Instance variables: self.x is the x coordinate, slef.y is the y coordinate,
    and self.color is a random;y assigned color
    Methods: a constructor for setting the initial variables and a string constructor
    for printing the shape's location and color
    '''
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.color = random.choice(["red", "orange", "yellow",
                         "green", "blue", "purple"])
    def __str__(self):
        loc = "(x="+str(self.x)+", y="+str(self.y)+"), "
        col = self.color
        return loc + col

class Circle(Shape):
    '''
    Purpose: A circle with coordinates
    Instance variables: self.rad, the radius of the circle
    Methods: an initial constructor for setting the color, x-y coordinates, and
    radius; a string constructor for pritning the circles, coordinates, color, and
    radius; and a turtle method for drawing the circle.
    '''
    def __init__(self, x=0, y=0, rad=0):
        Shape.__init__(self,x,y)
        self.rad = rad

    def __str__(self):
        shape_str = Shape.__str__(self)
        return shape_str + ", rad="+str(self.rad)

    def draw(self,t):
        t.penup()
        t.setpos(self.x,self.y-self.rad)
        t.pendown()
        t.fillcolor(self.color)
        t.begin_fill()
        t.circle(self.rad)
        t.end_fill()

    #Workout:
    def contains(self, x, y):
        max_dist = self.rad
        pt_dist = (((self.x - x)**2) + ((self.y - y)**2))**.5
        if max_dist > pt_dist:
            return True
        else:
            return False


#Stretch:
class Rectangle(Shape):
    '''
    Purpose: A rectangle with coordinates
    Instance variables: self.width, the width of the rectangle, and self.height,
    the height of the rectangle
    Methods: an initial constructor holding the coordinates, width and height of
    the rectangle, a string constructor to return its coordinates, color, width and height,
    and the draw method to draw a rectangle
    '''
    def __init__(self, x, y, width=20, height=20):
        Shape.__init__(self,x,y)
        self.width = width
        self.height = height

    def __str__(self):
        shape_str = Shape.__str__(self)
        return shape_str + ", w:"+str(self.width)+", h:"+str(self.height)

    def draw(self, t):
        t.penup()
        t.setpos(self.x,self.y)
        t.pendown()
        t.fillcolor(self.color)
        t.begin_fill()
        t.forward(self.width)
        t.left(90)
        t.forward(self.height)
        t.left(90)
        t.forward(self.width)
        t.left(90)
        t.forward(self.height)
        t.left(90)
        t.end_fill()

    #Workout:
    def contains(self, x, y):
        if (x > self.x and (self.x + self.width) > x) and (y > self.y and (self.y + self.height) > y):
            return True
        else:
            return False

#Warmup cont.:
class Display:
    '''
    Purpose: Displaying and storing a circle
    Instance variables: self.shapes, a list of shapes, self.t, a Turtle class instance,
    and self.mouse_event, a drawn circle
    Methods: An initial constructor to set up turtle and the onscreenclick method,
    and the mouse_event constructor to draw a circle wherever was clicked
    '''
    def __init__(self):
        self.shapes = []
        self.t = turtle.Turtle()
        self.t.speed(0)
        self.t.hideturtle()
        turtle.delay(0)
        turtle.onscreenclick(self.mouse_event)
        turtle.listen()
        turtle.mainloop()  #Required for some IDEs

    def mouse_event(self,x,y):
        new_circ = Circle(x,y,random.randint(10,50))
        new_rect = Rectangle(x,y,random.randint(10,50), random.randint(10,50))
        new_shape = random.choice([new_circ, new_rect])
        for shape in self.shapes:
            if shape.contains(x, y):
                print(shape)
                return
        self.shapes.append(new_shape)
        new_shape.draw(self.t)

Display()
