import random

#Problem A.
class Character:
    '''
    Purpose: (What does an object of this class represent?)
    Instance variables: (What are the instance variables for this class,
    and what does each represent in a few words?)
    Methods: (What methods does this class have, and what does each do in a few words?)
    '''
    def __init__(self, name, color, num_tasks):
        self.name = name
        self.color = color
        self.alive = True
        self.role = 'Good'
        possible_tasks = ['Stabilize drill', 'Calibrate distributor',
        'Map course', 'Clear out O2 filter', 'Download files',
        'Redirect power', 'Empty garbage', 'Repair wiring',
        'Fill engines tanks', 'Inspect laboratory', 'Record temperature',
        'Sign in with ID', 'Enable manifolds', 'Upload files']
        self.task_list = random.sample(possible_tasks, num_tasks)

    def __repr__(self):
        if self.alive is True:
            status = 'Alive'
        else:
            status = 'Ghost'
        return f'{self.name}: {self.color} - Health Status: {status}'

    def get_identity(self):
        return 'Character'

#Problem B.
class Crewperson(Character):
    '''
    Purpose: (What does an object of this class represent?)
    Instance variables: (What are the instance variables for this class,
    and what does each represent in a few words?)
    Methods: (What methods does this class have, and what does each do in a few words?)
    '''
    def get_identity(self):
        return 'Crewperson'

    def complete_task(self):
        if len(self.task_list) == 0:
            print(f'{self.name} has completed all their tasks.')
        else:
            task = self.task_list[0]
            self.task_list.pop(0)
            print(f'{self.name} has completed task: {task}.')

class Pretender(Character):
    '''
    Purpose: (What does an object of this class represent?)
    Instance variables: (What are the instance variables for this class,
    and what does each represent in a few words?)
    Methods: (What methods does this class have, and what does each do in a few words?)
    '''
    def __init__(self, name, color, num_tasks):
        Character.__init__(self, name, color, num_tasks)
        self.role = 'Evil'

    def get_identity(self):
        return 'Pretender'

    def eliminate(self, target):
        target.alive = False
        print(f'{self.name} eliminated {target.name}.')

#Problem C.
class Sheriff(Crewperson):
    '''
    Purpose: (What does an object of this class represent?)
    Instance variables: (What are the instance variables for this class,
    and what does each represent in a few words?)
    Methods: (What methods does this class have, and what does each do in a few words?)
    '''
    def get_identity(self):
        return 'Sheriff'

    def encounter(self, target):
        if target.role == 'Evil':
            target.alive = False
        print(f'{self.name} eliminated {target.name}.')

#Problem D.
class Game:
    '''
    Purpose: (What does an object of this class represent?)
    Instance variables: (What are the instance variables for this class,
    and what does each represent in a few words?)
    Methods: (What methods does this class have, and what does each do in a few words?)
    '''
    def __init__(self, player_list):
        self.player_list = player_list

    def check_winner(self):
        goods = 0
        goods_tasks = 0
        goods_alive = 0
        evils_alive = 0
        for player in self.player_list:
            if player.role == 'Good':
                goods += 1
                if player.alive is True:
                    goods_alive += 1
                if len(player.task_list) == 0:
                    goods_tasks += 1
            elif player.role == 'Evil':
                if player.alive is True:
                    evils_alive += 1
        if evils_alive == 0 or goods == goods_tasks:
            print(f'Crewpersons win!')
            return 'C'
        elif evils_alive >= goods_alive:
            print(f'Pretenders win!')
            return 'P'
        else:
            return '-'

    def meeting(self):
        meeting = []
        for player in self.player_list:
            if player.alive is True:
                meeting.append(player)
        poorsoul = random.choice(meeting)
        for sussy in meeting:
            print(f'{sussy.name} voted for {poorsoul.name}.')
        print(f'{poorsoul.name} was voted out and eliminated')
        poorsoul.alive = False
        return f'{poorsoul.name}'

    def play_game(self):
        while True:
            the_living = []
            for player in self.player_list:
                if player.alive is True:
                    the_living.append(player)
            for player in self.player_list:
                if player.role == 'Good':
                    for i in range(random.randint(1,3)):
                        player.complete_task()
                    if player.get_identity() == 'Sheriff':
                        player.encounter(random.choice(the_living))
                elif player.role == 'Evil' and player.alive is True:
                    merk = random.choice(the_living)
                    if merk.role == 'Good' and merk.alive is True:
                        player.eliminate(merk)
            result = self.check_winner()
            if result == '-':
                self.meeting()
                result = self.check_winner()
                if result == 'C' or result == 'P':
                    return result
            else:
                return result
