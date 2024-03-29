"""
Some functions for working with puzzles
"""
from puzzle import Puzzle
from collections import deque
# set higher recursion limit
# which is needed in PuzzleNode.__str__
#import resource
import sys
#resource.setrlimit(resource.RLIMIT_STACK, (2**29, -1))
sys.setrecursionlimit(10**6)

# References:
# Uused for BFS
# http://code.activestate.com/recipes/579138-simple-breadth-first-depth-first-tree-traversal/
# https://en.wikipedia.org/wiki/Breadth-first_search (Pseudocode)
# https://stackoverflow.com/questions/713508/find-the-paths-between-two-given-nodes
# Used for DFS:
# https://stackoverflow.com/questions/26967139/depth-first-search-on-a-binary-tree
#https://stackoverflow.com/questions/21508765/how-to-implement-depth-first-search-for-graph-with-non-recursive-aprroach

# Used the pseudo code from wiki to implement DFS and BFS.

# TODO
# implement depth_first_solve
# do NOT change the type contract
# you are welcome to create any helper functions
# you like
def depth_first_solve(puzzle):
    """
    Return a path from PuzzleNode(puzzle) to a PuzzleNode containing
    a solution, with each child containing an extension of the puzzle
    in its parent.  Return None if this is not possible.

    @type puzzle: Puzzle
    @rtype: PuzzleNode
    """
    # Used as a stack
    stack = []
    # Append the puzzle to the list.
    stack.append(PuzzleNode(puzzle, puzzle.extensions()))
    # List to keep track of the visited nodes
    visited = []
     # Loop till the stack is empty.
    while len(stack) != 0:
        # Pop the item from the stack.
        temp = stack.pop()
        # Chck if the current puzzle is seen before or its unsolvable.
        if temp not in visited and not temp.puzzle.fail_fast():
            # Append the puzzle to the visited list.
            visited.append(temp)
            # Loop thorugh the extensions.
            for ext in temp.puzzle.extensions():
                stack.append(PuzzleNode(ext, ext.extensions(), temp))
            if temp.puzzle.is_solved():
                # Current temp node is the solution.
                return temp
    # Retrun None if there is no solution to the puzzle
    return None


# TODO
# implement breadth_first_solve
# do NOT change the type contract
# you are welcome to create any helper functions
# you like
# Hint: you may find a queue useful, that's why
# we imported deque
def breadth_first_solve(puzzle):
    """
    Return a path from PuzzleNode(puzzle) to a PuzzleNode containing
    a solution, with each child PuzzleNode containing an extension
    of the puzzle in its parent.  Return None if this is not possible.

    @type puzzle: Puzzle
    @rtype: PuzzleNode
    """
    # BFS and DFS looks the same, the only difference is BFS uses a queue. And
    # DFS uses a stack.
    # Got that from stackoverflow ^^

    # Call the deque functions
    q = deque()
    # Append the puzzle to the queue.
    q.append(PuzzleNode(puzzle, puzzle.extensions()))
    # List to keep track of the visited nodes
    visited = []
    # Loop till the queue is empty.
    while len(q) != 0:
        # Pop the item from the queue.
        temp = q.popleft()
        # Chck if the current puzzle is seen before or its unsolvable.
        if temp not in visited and not temp.puzzle.fail_fast():
            # Append the puzzle to the visited list.
            visited.append(temp)
            # Loop thorugh the extensions.
            for ext in temp.puzzle.extensions():
                # Make tree node and append to the queue.
                q.append(PuzzleNode(ext, ext.extensions(), temp))
            if temp.puzzle.is_solved():
                # Current temp node is the solution.
                return temp
    # Retrun None if there is no solution to the puzzle
    return None


# Class PuzzleNode helps build trees of PuzzleNodes that have
# an arbitrary number of children, and a parent.
class PuzzleNode:
    """
    A Puzzle configuration that refers to other configurations that it
    can be extended to.
    """

    def __init__(self, puzzle=None, children=None, parent=None):
        """
        Create a new puzzle node self with configuration puzzle.

        @type self: PuzzleNode
        @type puzzle: Puzzle | None
        @type children: list[PuzzleNode]
        @type parent: PuzzleNode | None
        @rtype: None
        """
        self.puzzle, self.parent = puzzle, parent
        if children is None:
            self.children = []
        else:
            self.children = children[:]

    def __eq__(self, other):
        """
        Return whether Puzzle self is equivalent to other

        @type self: PuzzleNode
        @type other: PuzzleNode | Any
        @rtype: bool

        >>> from word_ladder_puzzle import WordLadderPuzzle
        >>> pn1 = PuzzleNode(WordLadderPuzzle("on", "no", {"on", "no", "oo"}))
        >>> pn2 = PuzzleNode(WordLadderPuzzle("on", "no", {"on", "oo", "no"}))
        >>> pn3 = PuzzleNode(WordLadderPuzzle("no", "on", {"on", "no", "oo"}))
        >>> pn1.__eq__(pn2)
        True
        >>> pn1.__eq__(pn3)
        False
        """
        return (type(self) == type(other) and
                self.puzzle == other.puzzle and
                all([x in self.children for x in other.children]) and
                all([x in other.children for x in self.children]))

    def __str__(self):
        """
        Return a human-readable string representing PuzzleNode self.

        # doctest not feasible.
        """
        return "{}\n\n{}".format(self.puzzle,
                                 "\n".join([str(x) for x in self.children]))
