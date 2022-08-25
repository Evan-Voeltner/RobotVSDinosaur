class Dinosaur:
    def __init__(self):
        self.name = ''
        self.health = 100
        self.attack_power = 50

    def attack(self, robot):
        robot.health -= self.active_weapon.attack_power
        print(f'Dinosaur attacked Robot, and it delt {str(self.active_weapon.attack_power)}!')
        print(f'Robot has {str(robot.health)} health left!')