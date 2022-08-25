from random import randint
from robot import Robot

class Fleet:
    def __init__(self):
        self.fleet = [Robot('Jerry'), Robot('Terry'), Robot('Berry')]

    def get_robot(self):
        robot_index = randint(0,len(self.fleet)-1)
        return self.fleet[robot_index]

    def kill_robot(self, robot_to_remove):
        for index_of_robot in range(len(self.fleet)):
            if self.fleet[index_of_robot] == robot_to_remove:
                    self.fleet.pop(index_of_robot)
                    print(f'{robot_to_remove.name} was killed!')
                    break