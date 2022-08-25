from dinosaur import Dinosaur
from robot import Robot

class Battlefield:
    def __init__(self):
        self.robot = Robot()
        self.dinosaur = Dinosaur()
        self.winner = ''

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()
    
    def display_welcome(self):
        print('Welcome to the battle!')
        print('Robot and Dinosaur are going to face off in a battle to the LITERAL DEATH!')
        print('May the best battler win! (is battler a word? idk)')
        print('Good luck!')

    def battle_phase(self):
        while True:
            self.robot.attack(self.dinosaur)
            if self.dinosaur.health <= 0:
                self.winner = 'Robot'
                break
            self.dinosaur.attack(self.robot)
            if self.robot.health <= 0:
                self.winner = 'Dinosaur'
                break
        
    def display_winner(self):
        print(f'The winner of the battle is {self.winner}!')