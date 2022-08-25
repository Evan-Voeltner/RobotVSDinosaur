from random import randint
from robot import Robot

class Fleet:
    def __init__(self):
        self.fleet = [Robot('Jerry'), Robot('Terry'), Robot('Berry')]

    def get_robot(self):
        robot_index = randint(0,2)
        return self.fleet[robot_index]