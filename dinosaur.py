class Dinosaur:
    def __init__(self, name):
        self.name = name
        self.health = 150
        self.attack_power = 25

    def attack(self, robot):
        robot.health -= self.attack_power
        print(f'{self.name} attacked {robot.name}, and it delt {str(self.attack_power)} damage!')
        print(f'{robot.name} has {str(robot.health)} health left!')