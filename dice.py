from random import randint

class Dice:

    def __init__(self, num_sides):
        self._num_sides = num_sides

    def roll(self):
        return randint(1, self._num_sides)

