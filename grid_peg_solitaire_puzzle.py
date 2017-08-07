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
                       (self._marker == other._marker) and (self._marker_set == other._marker_set))      
                
    def __str__(self):
        ret = ''
        for row in self._marker:
            ret += str(row) + '\n'
        return ret
    # __repr__ is up to you

    # TODO
    # override extensions
    # legal extensions consist of all configurations that can be reached by
    # making a single jump from this configuration
    def extensions(self):
        '''(self) -> list of puzzle obj
        
        '''
        # Call the get_empty_space method to get the coordinates of the empty
        # spaces.
        empty_space_coor = self.get_empty_space()
        # Get the numer of rows.
        num_row = len(self._marker) - 1
        # Get the number of elements in a row.
        num_sub_r = len(self._marker[0]) - 1
        # Init method vars.
        extensions, markers = [], self._marker_set
        # Loop through the coordinates list.
        for coor in empty_space_coor:
            # Get the row coor and col coor.
            row, sub_row = coor[0], coor[1]
            # CHECK FOR VALID MOVES.
            # UP DIRECTION MOVE
            if row + 2 <= num_row:
                # Make a deepcopy of the puzzle
                temp_puzzle = deepcopy(self._marker)
                # Check for pegs
                if (temp_puzzle[row + 1][sub_row] == '*') and (temp_puzzle[row + 2][sub_row] == '*'):
                    # Make the move by swapping the symbols.
                    temp_puzzle[row][sub_row] = '*'
                    temp_puzzle[row + 1][sub_row] = '.'
                    temp_puzzle[row + 2][sub_row] = '.'
                    extensions.append(GridPegSolitairePuzzle(temp_puzzle, markers))

            # DOWN DIRECTION MOVE
            if row - 2 >= 0:
                temp_puzzle = deepcopy(self._marker)
                if (temp_puzzle[row - 1][sub_row] == '*') and (temp_puzzle[row - 2][sub_row] == '*'):
                    # Make the move by swapping the symbols.
                    temp_puzzle[row][sub_row] = '*'
                    temp_puzzle[row - 1][sub_row] = '.'
                    temp_puzzle[row  - 2][sub_row] = '.'
                    extensions.append(GridPegSolitairePuzzle(temp_puzzle, markers))      
    
            # RIGHT DIRECTION MOVE
            if col + 2 <= num_sub_r:
                temp_puzzle = deepcopy(self._marker)
                # Check for pegs
                if (temp_puzzle[row][sub_row + 1] == '*') and (temp_puzzle[row][sub_row + 2] == '*'):
                    # Make the move by swapping the symbols.
                    temp_puzzle[row][sub_row] = '*'
                    temp_puzzle[row][sub_row + 2] = '.'
                    temp_puzzle[row][sub_row + 1] = '.'
                    extensions.append(GridPegSolitairePuzzle(temp_puzzle, markers))                    

            # LEFT DIRECTION MOVE
            if col - 2 >= 0:
                temp_puzzle = deepcopy(self._marker)
                # Check for pegs
                if (temp_puzzle[row][sub_row - 1] == '*') and (temp_puzzle[row][sub_row - 2] == '*'):
                    # Make the move by swapping the symbols.
                    temp_puzzle[row][sub_row] = '*'
                    temp_puzzle[row][sub_row - 2] = '.'
                    temp_puzzle[row][sub_row - 1] = '.'
                    extensions.append(GridPegSolitairePuzzle(temp_puzzle, markers))
        # Return the list of all the possible extensions.
        return extensions

    def get_empty_space(self):
        '''(self) -> list of tuples
        Given a puzzle, then returns the coordinates of all the epmty spaces.
        '''
        # Var for keeping count of the rows/sub_rows.
        row = 0
        col = 0
        coor = []
        # Loop through the rows of the puzzle
        for grid_row in self._marker:
            # Loop through the sub row.
            for sub_row in grid_row:
                # Look for the space.
                if sub_row == ".":
                    # Keep track of the space coor.
                    coor.append((row, col))
                # Increment the counter.
                col += 1
            # Reset the counter.
            col = 0
            row += 1
        # Return the tuple with the coor in a list.
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
