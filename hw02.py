import math

#TODO: Fill out the Purpose, Parameter(s), and Return Value
# for each of the two functions below in comments, and then write
# additional functions for parts B and C, and fill out the same information
# for those functions as well.

# Example functions for background reading

def nickels_to_cents(nickels):
    '''
    Purpose:
        Converts from a given number of nickels to
        the number of cents they represent
    Parameter(s):
        nickels: The number of nickels we have
    Return Value:
        The amount in cents we have
    '''
    total = nickels * 5
    return total

def degrees_to_radians(deg):
    '''
    Purpose:
        Converts from degrees to radians
    Parameter(s):
        deg: The number of degrees in a given angle
    Return Value:
        The given angle's measure in radians
    '''
    radians = deg * math.pi / 180
    return radians




# Part A: Two functions that you should add documentation to
def celsius_to_fahrenheit(celsius):
    '''
    Purpose:
        Converts from celsius to fahrenheit
    Parameter(s):
        celsius: temperature in celsius
    Return Value:
        The given temperature in celsius in fahrenheit
    '''
    fahr = (celsius * 9 / 5) + 32
    return fahr

def print_25_stars():
    '''
    Purpose:
        Prints 25 stars
    Parameter(s):
        None
    Return Value:
        None
    '''
    print('*****')
    print('*****')
    print('*****')
    print('*****')
    print('*****')


# Part B: Write out a few simple conversions

def area_circle(radius):
    '''
    Purpose:
        Calculates the area of a circle given the radius
    Parameter(s):
        radius: The length of a given radius
    Return Value:
        The area of the circle
    '''
    area = math.pi * radius ** 2
    return area

def meters_to_feet(meters):
    '''
    Purpose:
        Converts from meters to feet
    Parameter(s):
        meters: The length in meters
    Return Value:
        The length in feet
    '''
    feet = meters * 3.28084
    return feet

def minutes_to_days(minutes):
    '''
    Purpose:
        Converts from minutes to days
    Parameter(s):
        minutes: The number of minutes
    Return Value:
        The amount of days equal to the given amount of minutes
    '''
    days = minutes * 0.00069444
    return days

# Part C: Simulate changes in fish population over three weeks

def population(small, middle, big):
    '''
    Purpose:
        Gives the population changes for 3 fish populations in a lake
    Parameter(s):
        small: The initial number of smallfish
        middle: The initial number of middlefish
        big: The initial number of bigfish
    Return Value:
        The change in their populations over 3 weeks
    '''
    small = round(small * 1.1)
    middle = round(middle * 0.95)
    big = round(big * 0.9)

    eatenS = round(0.0001 * small * middle)

    small = small - eatenS
    middle = middle + eatenS * 2

    eatenM = round(0.0002 * middle * big)

    middle = middle - eatenM
    big = big + eatenM

    print("Week 1 - Small:", small,", Middle:", middle,", Big:", big)

    small = round(small * 1.1)
    middle = round(middle * 0.95)
    big = round(big * 0.9)

    eatenS = round(0.0001 * small * middle)

    small = small - eatenS
    middle = middle + eatenS * 2

    eatenM = round(0.0002 * middle * big)

    middle = middle - eatenM
    big = big + eatenM

    print("Week 2 - Small:", small,", Middle:", middle,", Big:", big)

    small = round(small * 1.1)
    middle = round(middle * 0.95)
    big = round(big * 0.9)

    eatenS = round(0.0001 * small * middle)

    small = small - eatenS
    middle = middle + eatenS * 2

    eatenM = round(0.0002 * middle * big)

    middle = middle - eatenM
    big = big + eatenM

    print("Week 3 - Small:", small,", Middle:", middle,", Big:", big)

    total = small + middle + big
    return total
