# Warm-up

import turtle, random, math
turtle.speed(0)
turtle.delay(0)


def div27(num):
    is_divisible = False
    for i in range(2,8):
        if num % i == 0:
            is_divisible = True
    return is_divisible

def filled_square(side):
    r = random.random()
    g = random.random()
    b = random.random()
    turtle.color(r,g,b)
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(side)
        turtle.left(90)
    turtle.end_fill()

def spiro(num, side):
    for sq in range(num):
        filled_square(side)
        turtle.right(360 / num)

# Stretch

def mul(a,b):
    '''
    Purpose: To give the product of two integers using a for loop

    Parameters: Two integers

    Return value: The product
    '''

    product = 0
    for i in range(a):
        product += b
    return product

def mul2(a,b):
    '''
    Purpose: To give the product of two integers using a while loop

    Parameters: Two integers

    Return value: The product
    '''

    product = 0
    i = 0
    while i < a:
        i += 1
        product += b
    return product

def expo(x,y):
    '''
    Purpose: To exponentiate two integers and return the product

    Parameters: Two integers

    Return value: The product of the exponentiation
    '''

    product = 1
    for i in range(y):
        product *= x
    return product

def expo2(x,y):
    '''
    Purpose: To exponentiate two integers and return the product

    Parameters: Two integers

    Return value: The product of the exponentiation
    '''

    product = 1
    for i in range(y):
        product = mul(product, x)
    return product

# Workout

def drunkwalk():
    escaped = False
    num_walks = 0
    while escaped != True:
        turtlehead = random.randint(1,4)
        turtle.setheading((turtlehead -1) * 90)
        turtle.forward(30)
        num_walks += 1
        if (turtle.xcor() > 300 or turtle.xcor() < -300):
            escaped = True
        if (turtle.ycor() > 300 or turtle.ycor() < -300):
            escaped = True

    turtle.penup()
    turtle.goto(0,0)
    turtle.write(num_walks, font=("Comic Sans", 20, "normal"))

# Challenge
def pi_sim():
    turtle.penup()
    turtle.goto(-150,-150)
    turtle.pendown()
    turtle.forward(150)
    turtle.circle(150)
    turtle.forward(150)
    for i in range(3):
        turtle.left(90)
        turtle.forward(300)

    total_dots = 0
    dots_in_circle = 0
    for j in range(1000):
        randx = random.uniform(-150,150)
        randy = random.uniform(-150,150)
        turtle.penup()

        distance_from_center = math.sqrt(randx ** 2 + randy ** 2)
        if distance_from_center <= 150:
            color = 'green'
            dots_in_circle += 1
        else:
            color = 'red'

        total_dots += 1
        turtle.goto(randx, randy)
        turtle.dot(5, color)

    prob_in_circle = dots_in_circle / total_dots
    pi = prob_in_circle * 4
    print(pi)
