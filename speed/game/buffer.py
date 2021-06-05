from game import constants
from game.actor import Actor
from game.point import Point


class Buffer(Actor):
    def __init__(self):
        super().__init__()
        self._buffer = []
        self._empty_string = ""
        position = Point(1, constants.MAX_Y - 0)
        self.set_position(position)
        self.set_text(f"Buffer: ")

    def add_letter(self, letter):
        self._buffer += letter
        text = self._empty_string.join(self._buffer)
        self.set_text(f"Buffer: {text}")

    def refresh_buffer(self):
        guess = self._empty_string.join(self._buffer)
        self._buffer = []
        self._empty_string = ""
        return guess

    def get_buffer(self):
        return self._empty_string

    def delete_letter(self):
        if len(self._buffer) <= 0:
            return
        self._buffer.pop()
        text = self._empty_string.join(self._buffer)
        self.set_text(f"Buffer: {text}")
