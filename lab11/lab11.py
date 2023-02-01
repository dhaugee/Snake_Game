import turtle
import random

# Warmup:
class Rational:
    def __init__(self,num=0,den=1):
        self.numerator = num
        if den == 0:
            self.denominator = 1
        else:
            self.denominator = den

    def __str__(self):
        if self.denominator == 1:
            return str(self.numerator)
        elif self.numerator == 0:
            return '0'
        else:
            return str(self.numerator) + '/' + str(self.denominator)

# Stretch
class Vec2:
    def __init__(self, xval=0.0, yval=0.0):
        self.x = xval
        self.y = yval

    def __str__(self):
        return f'<{self.x}, {self.y}>'

    def get_values(self):
        return [self.x, self.y]

    def set_values(self, comps):
        self.x = comps[0]
        self.y = comps[1]

    def __add__(self, other):
        newx = self.x + other.x
        newy = self.y + other.y
        return Vec2(newx, newy)

    def __mul__(self, scalar):
        newx = self.x * scalar
        newy = self.y * scalar
        return Vec2(newx, newy)

# if __name__ == '__main__':
#     mass = 0.5
#     accel1 = Vec2(1, 2)
#     print(accel1) #should output <1, 2>
#     accel2 = Vec2(2, -2)
#     total_accel = accel1 + accel2
#     print(total_accel) #should output <3, 0>
#     force = total_accel * mass
#     flist = force.get_values()
#     print(flist) #should output [1.5, 0.0]
#     accel1.set_values(flist)
#     print(accel1) #should output <1.5, 0.0>

# Workout:
class Particle:
    def __init__(self, mass, pos, vel):
        self.mass = mass #this is a float or int
        self.pos = pos #this is a Vec2 object
        self.vel = vel #this is a Vec2 object
        self.t = turtle.Turtle()    #don’t forget to import turtle!
        self.t.shape("circle")
        self.t.shapesize(mass, mass)
        self.t.speed(0)
        self.t.penup()
        self.move()  #uncomment this after you implement move()
        self.t.pendown()



    def __str__(self):
        return f'mass:{self.mass}, pos:{self.pos}, vel:{self.vel}'

    def move(self):
        pos_list = self.pos.get_values()
        xval = pos_list[0]
        yval = pos_list[1]
        self.t.setpos(xval, yval)
        turtle.tracer(0,0)


    def accelerate(self, a, t):
        self.pos = (self.pos) + (self.vel*t) + (a*.5*(t**2))
        self.vel = (self.vel) + (a*t)
        self.move()
        turtle.update()

# if __name__ == '__main__':
#     p1 = Particle(50,Vec2(-200,-50),Vec2(30,30))
#     p2 = Particle(20,Vec2(100,50),Vec2(-20,0))
#     print(p2) #should output mass:20, pos:<100, 50>, vel:<-20, 0>
#     p2.accelerate(Vec2(0,-10),2)
#     print(p2) #should output mass:20, pos:<60.0, 30.0>, vel:<-20, -20>
#     p2.accelerate(Vec2(20,20),3)
#     print(p2) #should output mass:20, pos:<90.0, 60.0>, vel:<40, 40>
#     for i in range(100):
#         p1.accelerate(Vec2(0,-10),0.1)
#         p2.accelerate(Vec2(0,-10),0.1)
#     print(p1) #should output mass:50, pos:<100.0, -250.0>, vel:<30.0, -70.0>
#     print(p2) #should output mass:20, pos:<490.0, -40.0>, vel:<40.0, -60.0>


# Challenge:

#:(
# def solar_system():
#     planets = []
#     for i in range(10):
#         mass = random.randint(1,100)
#         pos = Vec2(random.randint(-300, 300), random.randint(-300,300))
#         vel = Vec2(random.randint(-50,50), random.randint(-50,50))
#         planets.append(Particle(mass, pos, vel))
#     for i in range(100):
#         for planet in planets:
#             for other_planet in planets:
#
#             planet.accelerate()

def gravity():
    particle_list = []
    for i in range(20):
        mass = 1
        pos = Vec2(random.randint(-200, 200), random.randint(-200,200))
        vel = Vec2(random.randint(-50,50), random.randint(-50,50))
        particle_list.append(Particle(mass, pos, vel))

    print(particle_list)
    for i in range(100):
        for particle in particle_list:
            particle.accelerate(Vec2(0, -9.8), 0.1)
