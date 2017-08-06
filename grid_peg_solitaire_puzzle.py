from puzzle import Puzzle
from copy import deepcopy


class GridPegSolitairePuzzle(Puzzle):
    """
    Snapshot of peg solitaire on a rectangular grid. May be solved,
    unsolved, or even unsolvable.
    """

    def __init__(self, marker, marker_set):
        """
        Create a new GridPegSolitairePuzzle self with
        marker indicating pegs, spaces, and unused
        and marker_set indicating allowed markers.

        @type marker: list[list[str]]
        @type marker_set: set[str]
                          "#" for unused, "*" for peg, "." for empty
        """
        assert isinstance(marker, list)
        assert len(marker) > 0
        assert all([len(x) == len(marker[0]) for x in marker[1:]])
        assert all([all(x in marker_set for x in row) for row in marker])
        assert all([x == "*" or x == "." or x == "#" for x in marker_set])
        self._marker, self._marker_set = marker, marker_set

    # TODO
    # implement __eq__, __str__ methods
    def __eq__(self, other):
        return (type(other) == type(self) and
                       self._marker == other._marker and self._marker_set == other._marker_set)      
                
    def __str__(self):
        pass
    # __repr__ is up to you

    # TODO
    # override extensions
    # legal extensions consist of all configurations that can be reached by
    # making a single jump from this configuration
    def extensions(self):
        coor = self.get_empty_space()
        row, col = coor[0], col[1]
        row_len = len(self._marker[0])
        
    
    def get_empty_space(self):
        row = 0
        col = 0
        for grid_row in self._marker:
            for sub_row in grid_row:
                if sub_row == ".":
                    coor = (row, col)
                col += 1
            col = 0
            row += 1
        return coor
    # TODO
    # override is_solved
    # A configuration is solved when there is exactly one "*" left
    def is_solved(self):
        '''(self) -> bool
        Return True if the puzzle is solved, else False
        '''
        # Set is_solved to True.
        is_solved = True
        # num_peg var to keep count of the pegs on the grid.
        num_peg = 0
        # Loop through the grid.
        for row in self._marker:
            # Check for *.
            for sub_row in row:
                if sub_row == "*":
                    # Increment the num_peg by 1
                    num_peg += 1
        # Check if the num_peg is greater than 1.
        if num_peg > 1:
            # Set is_solved to False.
            is_solved = False
        # Return is_solved bool. 
        return is_solved


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    from puzzle_tools import depth_first_solve

    grid = [["*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*"],
            ["*", "*", ".", "*", "*"],
            ["*", "*", "*", "*", "*"]]
    gpsp = GridPegSolitairePuzzle(grid, {"*", ".", "#"})
    import time

    start = time.time()
    solution = depth_first_solve(gpsp)
    end = time.time()
    print("Solved 5x5 peg solitaire in {} seconds.".format(end - start))
    print("Using depth-first: \n{}".format(solution))
