import imp
from dinosaur import Dinosaur
from robot import Robot
from fleet import Fleet
from herd import Herd

class Battlefield:
    def __init__(self):
        self.robot = Robot()
        self.dinosaur = Dinosaur()
        self.robot_fleet = Fleet()
        self.dinosaur_herd = Herd()
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
            self.robot = self.robot_fleet.get_robot()
            self.robot.attack(self.dinosaur)
            if self.dinosaur.health <= 0:
                self.dinosaur_herd.kill_dinosaur()
                if len(self.dinosaur_herd.herd) == 0:
                    self.winner = 'Robots'
                    break
            
            self.dinosaur = self.dinosaur_herd.get_dinosaur()
            self.dinosaur.attack(self.robot)
            if self.robot.health <= 0:
                self.robot_fleet.kill_robot()
                if len(self.dinosaur_herd.herd) == 0:
                    self.winner = 'Dinosaurs'
                    break
        
    def display_winner(self):
        print(f'The winner of the battle are the {self.winner}!')