from weapon import Weapon

class Robot:
    def __init__(self):
        self.name = ''
        self.health = 100
        self.active_weapon = Weapon('Laser', 35)

    def attack(self, dinosaur):
        dinosaur.health -= self.active_weapon.attack_power
        print(f'Robot attacked Dinosaur with {self.active_weapon.name}, and it delt {str(self.active_weapon.attack_power)}!')
        print(f'Dinosaur has {str(dinosaur.health)} health left!')