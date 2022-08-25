from fleet import Fleet
from herd import Herd

class Battlefield:
    def __init__(self):
        self.robot_fleet = Fleet()
        self.dinosaur_herd = Herd()
        self.winner = ''

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()
    
    def display_welcome(self):
        print('Welcome to the battle!')
        print('Robots and Dinosaurs are going to face off in a battle to the LITERAL DEATH!')
        print('May the best battler win! (is battler a word? idk)')
        print('Good luck!')

    def battle_phase(self):
        while True:
            self.robot_fleet.current_robot = self.robot_fleet.get_robot()
            self.robot_fleet.current_robot.attack(self.dinosaur_herd.current_dinosaur)
            if self.dinosaur_herd.current_dinosaur.health <= 0:
                self.dinosaur_herd.kill_dinosaur(self.dinosaur_herd.current_dinosaur)
                if len(self.dinosaur_herd.herd) == 0:
                    self.winner = 'Robots'
                    break
            
            self.dinosaur_herd.current_dinosaur = self.dinosaur_herd.get_dinosaur()
            self.dinosaur_herd.current_dinosaur.attack(self.robot_fleet.current_robot)
            if self.robot_fleet.current_robot.health <= 0:
                self.robot_fleet.kill_robot(self.robot_fleet.current_robot)
                if len(self.robot_fleet.fleet) == 0:
                    self.winner = 'Dinosaurs'
                    break
        
    def display_winner(self):
        print(f'The winner of the battle are the {self.winner}!')