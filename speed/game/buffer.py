from game.actor import Actor
from game.point import Point
from game import constants

class Buffer(Actor):
    def __init__(self):
        super().__init__()
        position = Point(1, constants.MAX_Y - 5)
        self.set_position(position)
        self._buffer = []
        self.refresh_buffer()


    def add_letter(self, letter):
        if letter == '\n' or letter == '\r':
            self.refresh_buffer()
        else:
            s = list(self._buffer)
            for i in range(0, 40):
                if s[i] != '-':
                    s[i] = s[i]
                else:
                    s[i] = letter
                    break
            self._buffer = ''.join(s)
            self.set_text(f"Buffer: {self._buffer}")
        

    def get_buffer(self):
        return self._buffer
    
    def refresh_buffer(self):
        s = []
        for i in range(0, 40):
            s.append('-')
        self._buffer = ''.join(s)
        self.set_text(f"Buffer: {self._buffer}")