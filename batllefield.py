from dinosaur import Dinosaur
from robot import Robot

class Battlefield:
    def __init__(self):
        self.robot = Robot()
        self.dinosaur = Dinosaur()
        self.winner = ''

    def run_game(self):
        pass
    
    def display_welcome(self):
        pass

    def battle_phase(self):
        while True:
            self.robot.attack(self.dinosaur)
            if self.dinosaur.health <= 0:
                self.winner = 'Dinosaur'
                break
            self.dinosaur.attack(self.robot)
            if self.robot.health <= 0:
                self.winner = 'Robot'
                break
        
    def display_winner(self):
        print(f'The winner of the battle is {self.winner}!')