class Dinosaur:
    def __init__(self):
        self.name = ''
        self.health = 150
        self.attack_power = 25

    def attack(self, robot):
        robot.health -= self.attack_power
        print(f'Dinosaur attacked Robot, and it delt {str(self.attack_power)}!')
        print(f'Robot has {str(robot.health)} health left!')