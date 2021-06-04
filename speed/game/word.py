import random
from game import constants
from game.actor import Actor
from game.point import Point

class Word(Actor):
    def __init__(self):
        super().__init__()
        self._word_bank = []
        self.words_on_screen = []
        self._words_displayed = []
        self.word = []
        self._prepare_word()

    def get_all(self):
        # Returns a list of all the words on the screen

        return self.words_on_screen

    def _generate_words_in_list(self):
        # Make sure there is an if statement that makes is so it only generates new words if the others reache the end
        self._create_word_bank()
        for s in range(constants.STARTING_WORDS):
            word = self._word_bank[random.randint(1,9886)]
            self.words_on_screen.append(word)
        for word in self.words_on_screen:
            single_word_list = list(word)
            self._words_displayed.append(single_word_list)

    def generate_words(self):
        count = len(self.word) -1
        for n in range(count, -1, -1):
            segment = self.word[n]
            if n > 0:
                leader = self.word[-1]
                velocity = leader.get_velocity()
                segment.set_velocity(velocity)
            else:
                pass
            segment.move_next()



    def _create_word_bank(self):
        with open("words.txt", "rt") as reader:
            self._word_bank = reader.readlines()
        return self._word_bank

    def _prepare_word(self):
        """Prepares the word body by inputting its position
        
        Args:
            self (word): an instance of Word.
        """
        self._generate_words_in_list()
        x = int(constants.MAX_X / 2 )
        y = int(constants.MAX_Y / 2 )
        for n in range(len(self._words_displayed)):
            for letter in self._words_displayed[n]:
                text = letter
                position = Point(x - n, y)
                velocity = Point(1, 0)
                self._add_segment(text, position, velocity)

    def _add_segment(self, text, position, velocity):
        segment = Actor()
        segment.set_text(text)
        segment.set_position(position)
        segment.set_velocity(velocity)
        self.word.append(segment)