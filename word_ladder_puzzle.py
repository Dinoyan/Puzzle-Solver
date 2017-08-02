from puzzle import Puzzle
import codecs

class WordLadderPuzzle(Puzzle):
    """
    A word-ladder puzzle that may be solved, unsolved, or even unsolvable.
    """

    def __init__(self, from_word, to_word, ws):
        """
        Create a new word-ladder puzzle with the aim of stepping
        from from_word to to_word using words in ws, changing one
        character at each step.

        @type from_word: str
        @type to_word: str
        @type ws: set[str]
        @rtype: None
        """
        (self._from_word, self._to_word, self._word_set) = (from_word,
                                                            to_word, ws)
        # set of characters to use for 1-character changes
        self._chars = "abcdefghijklmnopqrstuvwxyz"

    # TODO
    # implement __eq__ and __str__
    # __repr__ is up to you
    def __eq__(self, other):
        return ((self.from_word == other._from_word) and (self._to_word == 
                other._to_word) and (self._word_set == other._word_set))
    
    def __str__(self):
        ret = 'From Word: ' + str(self._from_word) + ' to_word: ' + str(self._to_word)
        return ret

    # TODO
    # override extensions: DONE
    # legal extensions are WordLadderPuzzles that have a from_word that can
    # be reached from this one by changing a single letter to one of those
    # in self._chars
    def extensions(self):
        # Create an empty list to store the extensions.
        extensions_lst = []
        # Counter var to keep track of the char index.
        char_index = 0
        # Loop through the self._from_word.
        for char in self._from_word:
            # Loop through the self._chars.
            for alpha in self._chars:
                # Get the new extension word
                new_extension = self._from_word[:char_index] + alpha + self._from_word[char_index + 1:]
                # Check if the new extension word is in the word set.
                if ((new_extension in self._word_set) and 
                    (new_extension not in extensions_lst)):
                    # Add the word to the extension list
                    extensions_lst.append(new_extension)
        return extensions_lst

    # TODO
    # override is_solved: DONE
    # this WordLadderPuzzle is solved when _from_word is the same as
    # _to_word
    def is_solved(self):
        '''(self) -> bool
        >>> puzzle1 = WordLadderPuzzle('dinoyan', 'dinoyan', {'dino', 'dinoyan'})
        >>> puzzle1.is_solved()
        True
        >>> puzzle2 = WordLadderPuzzle('dinoyan', 'dino', {'dino', 'dinoyan'})
        >>> puzzle2.is_solved()
        False
        '''
        return self._from_word == self._to_word


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    from puzzle_tools import breadth_first_solve, depth_first_solve
    from time import time
    with codecs.open("words", "r", 'utf-8') as words:
        word_set = set(words.read().split())
    w = WordLadderPuzzle("same", "cost", word_set)
    start = time()
    sol = breadth_first_solve(w)
    end = time()
    print("Solving word ladder from same->cost")
    print("...using breadth-first-search")
    print("Solutions: {} took {} seconds.".format(sol, end - start))
    start = time()
    sol = depth_first_solve(w)
    end = time()
    print("Solving word ladder from same->cost")
    print("...using depth-first-search")
    print("Solutions: {} took {} seconds.".format(sol, end - start))
