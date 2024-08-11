from food import Food
from snake import Snake
import turtle

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
        turtle.title("Snake Game by Dylan Haugee")
        turtle.bgcolor("dark green")
        self.is_game_over = False
        self.player = Snake(315, 315, 'chartreuse3')
        self.pellet = Food()
        self.player.u_score()
        self.gameloop()
        self.game_over = turtle.Turtle()
        self.game_over.hideturtle()
        self.is_game_over = False
        turtle.onkeypress(self.player.go_down, 'Down')
        turtle.onkeypress(self.player.go_up, 'Up')
        turtle.onkeypress(self.player.go_left, 'Left')
        turtle.onkeypress(self.player.go_right, 'Right')
        turtle.onkeypress(self.restart, 't')
        turtle.listen()
        turtle.mainloop()

    def gameloop(self):
        self.player.move(self.pellet)
        if (self.player.selfcollision() is True) or (self.player.wallcollision() is True):
            self.player.current_score = 0
            self.player.score.clear()
            self.player.u_score()
            self.game_over.penup()
            self.game_over.setpos(315, 315)
            self.game_over.write('GAME OVER', align='center', font=('Futura', 44, 'bold'))
            self.game_over.setpos(315, 300)
            self.game_over.write('Press t to try again', align='center', font=('Futura', 18,))
            self.is_game_over = True
        elif (self.player.selfcollision() is False) or (self.player.wallcollision() is False):
            turtle.ontimer(self.gameloop, 200)
            turtle.update()

    def restart(self):
        self.player.restart()
        self.player.x = 315
        self.player.y = 315
        self.player.color = 'chartreuse3'
        self.player.grow()
        self.player.vx = 30
        self.player.vy = 0
        self.pellet.random_pos()
        if self.is_game_over:
            self.game_over.clear()
            self.is_game_over = False
            self.gameloop()