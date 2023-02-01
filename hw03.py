#Problem A.
def sound(weight):
    '''
    Purpose: To translate a dog's given
    weight into what their bark would sound like

    Parameter: The dog's weight in pounds

    Return Value: What the dog's bark would sound like
    '''

    if round(weight) < 13:
        print("'Yip'")
    elif 13 <= round(weight) <= 30:
        print("'Ruff'")
    elif 30 < round(weight) <= 70:
        print("'Bark'")
    else:
        print("'Boof'")

#Problem B.
def sound2(weight, is_cat):
    '''
    Purpose: To determine not only what sound a
    pet might make, but if they're a cat or dog

    Parameters: The pet's weight and if they're
    a cat or not

    Return Value: The sound the pet would make
    '''

    if is_cat == True:
        print("'Meow'")
    else:
        sound(weight)

#Problem C.
def selection(text, optionA, optionB, optionC):
    '''
    Purpose: To print a situation or problem with
    three choices to choose from

    Parameters: The prompt and three options

    Return Value: The selected option
    '''

    print(text)
    print('A. ', optionA)
    print('B. ', optionB)
    print('C. ', optionC)
    choice = input('Choose A, B, or C: ')
    if choice == 'A':
        return choice
    elif choice == 'B':
        return choice
    elif choice == 'C':
        return choice
    else:
        print("Invalid option, defaulting to A")
        return 'A'

#Problem D.
def adventure():
    '''
    Purpose: To tell an interactive story

    Parameters: None

    Return Values: Whichever choice the user makes
    '''

    one = selection("You are me. You've just woken up, your ankle is injured, and you have to get to class.", "Screw it, no boot", "Strap on your boot", "Class is overrated, I'm tired")
    if one == 'C':
        print("You slept through several classes and are now stressed and behind. Oh yeah, and your ankle still hurts. Better luck next time.")
        return False
    elif one == 'A':
        three = selection("You hop on one foot out of bed, get dressed, and hop to the elevators. They're closed. So you hop to the stairs, where you promptly tumble down them. You're understandably scared to get up.", "Call your roommate", "Slowly try and get up", "Sit and cry")
        if three == 'B':
            print("You hesitantly try and apply pressure on your injured right ankle. You set it down at such an angle so that it instantly snaps. You collapse down on your left leg, also tearing your ACL. Ow.")
            return False
        elif three == 'C':
            print("You cry, and then you bawl. You bawl and bawl until your CA opens the door to the stairs to check on who could've let a feral cat in the building. Luckily for you, after explaining your situation, they give you a lollipop and tell you to attend the lecture virtually. Oh yeah... you forgot you could do that.")
            return True
        elif three == 'A':
            four = selection('You call your roommate and they pick up immediately, but before you have a chance to utter a single syllable, they say: \n Hey. Wake up. It\'s been 13 years.\nHow do you react?', "Close your eyes and breathe deeply", "Laugh and explain your situation", "Something is wrong. Hang up.")
            if four == 'A':
                print("You exhale sharply and sit up. It's so bright behind your eyelids. You hesistantly open them, and see that you're in a hospital bed. You look to your left at a window overlooking Mars. You look to your right and your wife is looking at you, smiling and crying. Damn, total recall is scary. Thank goodness you're okay!")
                return True
            if four == 'B':
                print("There's a long silence. He hangs up, but not before saying a single name you faintly recall from what feels like a past life. Oh well, I guess you'll be late to class while you figure this out.")
                return False
            if four == 'C':
                print("You hang up as a panic surges in your throat. It feels as though your mind is collpasing over itself, and everything is turning bright white. They must've pulled the cord. Oh well, there's always next life!")
                return False
    elif one == 'B':
        two = selection("You strap your boot on and walk out the door. You've almost made it to the elevators when you realize you put ONLY your boot on. You hobble back to your door. Oh man. It's jammed.", "Kick the door", "Screw it, no clothes", "Call your roommate")
        if two == 'A':
            print("You perform a spinning back heel kick with your injured foot. Surprisingly, the door opens! Oh yeah, and your foot is completely realigned. You get dressed and jog to class. Nice.")
            return True
        elif two == 'C':
            print("It's a hit! Everyone loves the avant-garde look you're scouted by several major modeling agencies.")
            return True
        elif two == 'B':
            four = selection('You call your roommate and they pick up immediately, but before you have a chance to utter a single syllable, they say: \n Hey. Wake up. It\'s been 13 years.\nHow do you react?', "Close your eyes and breathe deeply", "Laugh and explain your situation", "Something is wrong. Hang up.")
            if four == 'A':
                print("You exhale sharply and sit up. It's so bright behind your eyelids. You hesistantly open them, and see that you're in a hospital bed. You look to your left at a window overlooking Mars. You look to your right and your wife is looking at you, smiling and crying. Damn, total recall is scary. Thank goodness you're okay!")
                return True
            if four == 'B':
                print("There's a long silence. He hangs up, but not before saying a single name you faintly recall from what feels like a past life. Oh well, I guess you'll be late to class while you figure this out.")
                return False
            if four == 'C':
                print("You hang up as a panic surges in your throat. It feels as though your mind is collpasing over itself, and everything is turning bright white. They must've pulled the cord. Oh well, there's always next life!")
                return False
