from time import sleep
from game import constants
from game.word import Word
from game.score import Score
from game.buffer import Buffer


class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.

    Stereotype:
        Controller

    Attributes:
        word (Word): The buffer's target.
        input_service (InputService): The input mechanism.
        keep_playing (boolean): Whether or not the game can continue.
        output_service (OutputService): The output mechanism.
        score (Score): The current score.
        buffer (Buffer): The player or buffer.
    """

    def __init__(self, input_service, output_service):
        """The class constructor.

        Args:
            self (Director): an instance of Director.
        """
        self._word = Word()
        self._input_service = input_service
        self._keep_playing = True
        self._output_service = output_service
        self._score = Score()
        self._buffer = Buffer()

    def start_game(self):
        """Starts the game loop to control the sequence of play.

        Args:
            self (Director): an instance of Director.
        """
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
            sleep(constants.FRAME_LENGTH)

    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the desired direction and moving the buffer.

        Args:
            self (Director): An instance of Director.
        """
        direction = self._input_service.get_direction()
        self._buffer.move_head(direction)

    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means checking for a collision and updating the score.

        Args:
            self (Director): An instance of Director.
        """
        self._handle_body_collision()
        self._handle_word_collision()

    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if there are stones left and declaring 
        the winner.

        Args:
            self (Director): An instance of Director.
        """
        self._output_service.clear_screen()
        self._output_service.draw_actor(self._word)
        self._output_service.draw_actors(self._buffer.get_all())
        self._output_service.draw_actor(self._score)
        self._output_service.flush_buffer()

    def _handle_body_collision(self):
        """Handles collisions between the buffer's head and body. Stops the game 
        if there is one.

        Args:
            self (Director): An instance of Director.
        """
        head = self._buffer.get_head()
        body = self._buffer.get_body()
        for segment in body:
            if head.get_position().equals(segment.get_position()):
                self._keep_playing = False
                break

    def _handle_word_collision(self):
        """Handles collisions between the buffer's head and the word. Grows the 
        buffer, updates the score and moves the word if there is one.

        Args:
            self (Director): An instance of Director.
        """
        head = self._buffer.get_head()
        if head.get_position().equals(self._word.get_position()):
            points = self._word.get_points()
            for n in range(points):
                self._buffer.grow_tail()
            self._score.add_points(points)
            self._word.reset()