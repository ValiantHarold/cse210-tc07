from game import constants
from game.actor import Actor
from game.point import Point


class Buffer(Actor):
    """A limbless reptile. The responsibility of Buffer is keep track of its segments. It contains methods for moving and growing among others.

    Stereotype:
        Structurer, Information Holder

    Attributes:
        _body (List): The buffer's body (a list of Actor instances)
    """

    def __init__(self):
        """The class constructor.

        Args:
            self (Buffer): An instance of buffer.
        """
        super().__init__()
        self._points = 0
        position = Point(1, -20)
        self.set_position(position)
        self.set_text(f"Buffer: {self._points}")
        # self._segments = []
        # self._prepare_body()

    def get_all(self):
        """Gets all the buffer's segments.

        Args:
            self (Buffer): An instance of buffer.

        Returns:
            list: The buffer's segments.
        """
        return self._segments

    def get_body(self):
        """Gets the buffer's body.

        Args:
            self (Buffer): An instance of buffer.

        Returns:
            list: The buffer's body.
        """
        return self._segments[1:]

    def get_head(self):
        """Gets the buffer's head.

        Args:
            self (Buffer): An instance of buffer.

        Returns:
            Actor: The buffer's head.
        """
        return self._segments[0]

    def grow_tail(self):
        """Grows the buffer's tail by one segment.

        Args:
            self (Buffer): An instance of buffer.
        """
        tail = self._segments[-1]
        offset = tail.get_velocity().reverse()
        text = "#"
        position = tail.get_position().add(offset)
        velocity = tail.get_velocity()
        self._add_segment(text, position, velocity)

    def move_head(self, direction):
        """Moves the buffer in the given direction.

        Args:
            self (Buffer): An instance of buffer.
            direction (Point): The direction to move.
        """
        count = len(self._segments) - 1
        for n in range(count, -1, -1):
            segment = self._segments[n]
            if n > 0:
                leader = self._segments[n - 1]
                velocity = leader.get_velocity()
                segment.set_velocity(velocity)
            else:
                segment.set_velocity(direction)
            segment.move_next()

    def _add_segment(self, text, position, velocity):
        """Adds a new segment to the buffer using the given text, position and velocity.

        Args:
            self (Buffer): An instance of buffer.
            text (string): The segment's text.
            position (Point): The segment's position.
            velocity (Point): The segment's velocity.
        """
        segment = Actor()
        segment.set_text(text)
        segment.set_position(position)
        segment.set_velocity(velocity)
        self._segments.append(segment)

    def _prepare_body(self):
        """Prepares the buffer body by adding segments.

        Args:
            self (Buffer): an instance of Buffer.
        """
        x = int(constants.MAX_X / 2)
        y = int(constants.MAX_Y / 2)
        for n in range(constants.SNAKE_LENGTH):
            text = "8" if n == 0 else "#"
            position = Point(x - n, y)
            velocity = Point(1, 0)
            self._add_segment(text, position, velocity)
