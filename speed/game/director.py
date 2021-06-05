from game.input_service import InputService
from game.output_service import OutputService
from asciimatics.screen import Screen
from game.score import Score
from game import constants
from time import sleep
from game.buffer import Buffer
from game.word import Word


class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    Stereotype:
        Controller
    Attributes:
        Buffer (Buffer): The Word's target.
        input_service (InputService): The input mechanism.
        keep_playing (boolean): Whether or not the game can continue.
        output_service (OutputService): The output mechanism.
        score (Score): The current score.
        Word (Word): The player or Word.
    """

    def __init__(self, input_service, output_service):
        """The class constructor.
        Args:
            self (Director): an instance of Director.
        """
        self._buffer = Buffer()
        self._input_service = input_service
        self._keep_playing = True
        self._output_service = output_service
        self._score = Score()
        self._word = Word()

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
        that means getting the desired direction and moving the Word.
        Args:
            self (Director): An instance of Director.
        """
        letter = self._input_service.get_letter()
        # VVV Make sure to include that if they hit enter it clears buffer.
        if letter != None:
            self._buffer.add_letter(letter) 

    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means checking for a collision and updating the score.
        Args:
            self (Director): An instance of Director.
        """
        # self._handle_body_collision()
        self._word.generate_words()
        # self._buffer._buffer_clear_word(self._word.get_all())
        self.check_words(self._buffer.get_buffer(), self._word.get_all())

    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if there are stones left and declaring 
        the winner.
        Args:
            self (Director): An instance of Director.
        """
        self._output_service.clear_screen()
        self._output_service.draw_actor(self._buffer)
        # self._output_service.draw_actors(self._word.get_all())
        self._output_service.draw_actor(self._score)
        self._output_service.flush_buffer()

    def check_words(self, buffer, words):
        # Remove word from screen if it is in buffer
        for word in words:
            if word in buffer:
                words.remove(word)