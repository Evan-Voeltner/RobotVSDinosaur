from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapons = [Weapon('Laser', 20), Weapon('Taser', 40), Weapon('Wage Theft', 15)]
        self.active_weapon = None

    def attack(self, dinosaur):
        self.select_weapon()
        dinosaur.health -= self.active_weapon.attack_power
        print(f'{self.name} attacked {dinosaur.name} with {self.active_weapon.name}, and it delt {str(self.active_weapon.attack_power)} damage!')
        print(f'{dinosaur.name} has {str(dinosaur.health)} health left!')

    def select_weapon(self):
        for weapon in self.weapons:
            print(f'{weapon.name} | {str(weapon.attack_power)} Damage')
        selected_weapon = input('What weapon would you like to use?: ')
        for weapon in self.weapons:
            if weapon.name.lower() == selected_weapon:
                self.active_weapon = weapon

