from random import randint
from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.herd = [Dinosaur('Brayden'), Dinosaur('Kayden'), Dinosaur('Hayden')]

    def get_dinosaur(self):
        dinosaur_index = randint(0,len(self.herd)-1)
        return self.herd[dinosaur_index]

    def kill_dinosaur(self, dinosaur_to_remove):
        for index_of_dinosaur in range(len(self.herd)):
            if self.herd[index_of_dinosaur] == dinosaur_to_remove:
                    self.herd.pop(index_of_dinosaur)
                    print(f'{dinosaur_to_remove.name} was killed!')
                    break

    