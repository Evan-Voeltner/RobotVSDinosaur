from random import randint
from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.herd = [Dinosaur('Brayden'), Dinosaur('Kayden'), Dinosaur('Hayden')]

    def get_robot(self):
        dinosaur_index = randint(0,2)
        return self.herd[dinosaur_index]