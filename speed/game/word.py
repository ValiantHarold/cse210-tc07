import random
from game import constants
from game.actor import Actor
from game.point import Point


class Word(Actor):
    def __init__(self):
        super().__init__()
        self._words = []

    def get_all(self):
        """Returns a list of all the words on the screen"""

        return self._words

    def generate_word(self):
        """Makes a new word"""

        x = random.randint(1, 40)
        y = 1

        text = constants.LIBRARY[random.randint(1, 7733)]
        position = Point(x, y)
        velocity = Point(0, 1)

        new_word = Actor()
        new_word.set_text(text)
        new_word.set_position(position)
        new_word.set_velocity(velocity)
        self._words.append(new_word)

    def move_word(self):
        """Moves the word down"""

        count = len(self._words) - 1
        for n in range(count, -1, -1):
            word = self._words[n]
            word.move_next()
            y_min = word.get_position()._y
            if y_min == 20:
                self._words.remove(word)

    def check_word(self, guess):

        points = 0
        count = len(self._words) - 1
        for n in range(count, -1, -1):
            word = self._words[n]
            text = word.get_text()
            if text == guess:
                points = len(text)
                self._words.remove(word)
        return points
