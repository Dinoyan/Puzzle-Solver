from puzzle import Puzzle
from copy import deepcopy

class MNPuzzle(Puzzle):
    """
    An nxm puzzle, like the 15-puzzle, which may be solved, unsolved,
    or even unsolvable.
    """

    def __init__(self, from_grid, to_grid):
        """
        MNPuzzle in state from_grid, working towards
        state to_grid

        @param MNPuzzle self: this MNPuzzle
        @param tuple[tuple[str]] from_grid: current configuration
        @param tuple[tuple[str]] to_grid: solution configuration
        @rtype: None
        """
        # represent grid symbols with letters or numerals
        # represent the empty space with a "*"
        assert len(from_grid) > 0
        assert all([len(r) == len(from_grid[0]) for r in from_grid])
        assert all([len(r) == len(to_grid[0]) for r in to_grid])
        self.n, self.m = len(from_grid), len(from_grid[0])
        self.from_grid, self.to_grid = from_grid, to_grid

    # TODO
    # implement __eq__ and __str__
    def __eq__(self, other):
        '''(self, MNPuzzle) -> bool
        Return True if both of the puzzle are exact same or else False.
        >>> start_grid = (("1", "2", "3"), ("4", "5", "*"))
        >>> target_grid = (("1", "2", "3"), ("4", "5", "*"))
        >>> p1 = MNPuzzle(start_grid, target_grid)
        >>> p2 = MNPuzzle(start_grid, target_grid)
        >>> p1 == p2
        True
        >>> start_grid = (("1", "2", "3"), ("4", "*", "5"))
        >>> start_grid2 = (("1", "2", "3"), ("4", "5", "*"))
        >>> target_grid = (("1", "2", "3"), ("4", "5", "*"))
        >>> p1 = MNPuzzle(start_grid, target_grid)
        >>> p2 = MNPuzzle(start_grid2, target_grid)
        >>> p1 == p2
        False
        '''
        # Check all the class attributes and class type.
        return (type(other) == type(self) and
                       self.n == other.n and self.m == other.m and
                       self.to_grid == other.to_grid and self.from_grid ==
                       other.from_grid)
            
    def __str__(self):
        '''(self) -> str
        Returns the string representation of the puzzle
        >>> start_grid = (("1", "2", "3"), ("4", "5", "*"))
        >>> target_grid = (("1", "2", "3"), ("4", "5", "*"))
        >>> a = MNPuzzle(start_grid, target_grid)
        >>> print(a)
        From Grid:
        ('1', '2', '3')
        ('4', '5', '*')
        To Grid
        ('1', '2', '3')
        ('4', '5', '*')
        <BLANKLINE>
        '''
        from_grid = ''
        for row in self.from_grid:
            from_grid += str(row) + '\n'
        to_grid = ''
        for row in self.to_grid:
            to_grid += str(row)  + '\n'
        return "From Grid:" + '\n' + from_grid + 'To Grid' + '\n' + to_grid
        
    # __repr__ is up to you

    # TODO
    # override extensions
    # legal extensions are configurations that can be reached by swapping one
    # symbol to the left, right, above, or below "*" with "*"
    def extensions(self):
        '''(self) -> list
        Returns a list with all the legal extensions. Legal extensions are confi
        gurations that can be reached by swapping one  symbol to the left,
        right, above, or below "*" with "*"
        >>> start_grid = (("2", "*", "3"), ("1", "4", "5"))
        >>> target_grid = (("1", "2", "3"), ("4", "5", "*"))
        >>> a = MNPuzzle(start_grid, target_grid)
        >>> l = a.extensions()
        >>> print(l[0])
        From Grid:
        ('2', '4', '3')
        ('1', '*', '5')
        To Grid
        ('1', '2', '3')
        ('4', '5', '*')
        <BLANKLINE>
        >>> print(l[2])
        From Grid:
        ('*', '2', '3')
        ('1', '4', '5')
        To Grid
        ('1', '2', '3')
        ('4', '5', '*')
        <BLANKLINE>
        >>> print(l[1])
        From Grid:
        ('2', '3', '*')
        ('1', '4', '5')
        To Grid
        ('1', '2', '3')
        ('4', '5', '*')
        <BLANKLINE>
        '''
        # List to store the extensions.
        extensions = []
        # Call the get_space_coor method.
        coor = self.get_space_coor()
        # Get the row and column ints.
        row, sub_row, to_grid = coor[0], coor[1], self.to_grid
        # Down move
        if row + 1 < self.n:
            grid_copy = deepcopy(self.from_grid)
            lst_grid = self.convert_to_lst(grid_copy)
            # Make the moves
            value = lst_grid[row + 1][sub_row]
            lst_grid[row + 1][sub_row] = '*'
            lst_grid[row][sub_row] = value
            # Create a MNPuzzle instances and append the list
            extensions.append(MNPuzzle(self.convert_to_tuple(lst_grid), to_grid))    

        # Up move
        if row - 1 >= 0:
            grid_copy = deepcopy(self.from_grid)
            lst_grid = self.convert_to_lst(grid_copy)
            # Make the moves
            value = lst_grid[row - 1][sub_row]
            lst_grid[row - 1][sub_row] = '*'
            lst_grid[row][sub_row] = value
            # Create a MNPuzzle instances and append the list
            extensions.append(MNPuzzle(self.convert_to_tuple(lst_grid), to_grid))                    

        # Right Move
        if sub_row + 1 < self.m:
            grid_copy = deepcopy(self.from_grid)
            lst_grid = self.convert_to_lst(grid_copy)
            # Make the moves
            value = lst_grid[row][sub_row + 1]
            lst_grid[row][sub_row + 1] = '*'
            lst_grid[row][sub_row] = value
            # Create a MNPuzzle instances and append the list
            extensions.append(MNPuzzle(self.convert_to_tuple(lst_grid), to_grid))

        # Left move
        if sub_row - 1 >= 0:
            grid_copy = deepcopy(self.from_grid)
            lst_grid = self.convert_to_lst(grid_copy)
            value = lst_grid[row][sub_row - 1]
            lst_grid[row][sub_row - 1] = '*'
            lst_grid[row][sub_row] = value
            extensions.append(MNPuzzle(self.convert_to_tuple(lst_grid), to_grid))              
        return extensions  

    def get_space_coor(self):
        '''(self) -> tuple of ints
        Find the empty space from the start grid and return a tuple with the
        coordinate of the emptyspace on the grid.(row, sub_row)
        >>> target_grid = (("1", "2", "3"), ("4", "5", "*"))
        >>> start_grid = (("*", "2", "3"), ("1", "4", "5"))
        >>> a = MNPuzzle(start_grid, target_grid)
        >>> a.get_space_coor()
        (0, 0)
        '''
        # Counter vars.
        row_coor = 0
        space_coor = 0
        # Get the coordinate of the empty space '*'
        for sub_row in self.from_grid:
            # Loop through the sub row.
            for item in sub_row:
                if item == '*':
                    # Create a tuple with the coordinates
                    empty_coor = (row_coor, space_coor)
                space_coor += 1
            # Increment the counter.
            row_coor += 1
            # Reset the counter.
            space_coor = 0
        # Return the coor.
        return empty_coor

    def convert_to_lst(self, grid):
        '''(self, tuple) -> list
        Helper Method: Given a grid as tuple then converts to a list.
        '''
        return list(list(row) for row in grid)


    def convert_to_tuple(self, grid):
        '''(self, list) -> tuple
        Helper Method: Given a grid as list then converts to a tuple.
        '''
        return tuple(tuple(row) for row in grid)

    # TODO
    # override is_solved
    # a configuration is solved when from_grid is the same as to_grid
    def is_solved(self):
        '''(self) -> bool
        Return the bool, if the puzzle is solved or not.
        >>> start_grid = (("1", "2", "3"), ("4", "5", "*"))
        >>> target_grid = (("1", "2", "3"), ("4", "5", "*"))
        >>> a = MNPuzzle(start_grid, target_grid)
        >>> a.is_solved()
        True
        >>> start_grid = (("*", "2", "3"), ("1", "4", "5"))
        >>> target_grid = (("1", "2", "3"), ("4", "5", "*"))
        >>> a = MNPuzzle(start_grid, target_grid)
        >>> a.is_solved()
        False
        '''
        # Check if the from_grid is equal to to_grid
        return self.from_grid == self.to_grid

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    target_grid = (("1", "2", "3"), ("4", "5", "*"))
    start_grid = (("*", "2", "3"), ("1", "4", "5"))
    from puzzle_tools import breadth_first_solve, depth_first_solve
    from time import time

    start = time()
    solution = breadth_first_solve(MNPuzzle(start_grid, target_grid))

    # __str__ method tester
    print(MNPuzzle(start_grid, target_grid))
    
    end = time()
    print("BFS solved: \n\n{} \n\nin {} seconds".format(
        solution, end - start))
    start = time()
    solution = depth_first_solve((MNPuzzle(start_grid, target_grid)))
    end = time()
    print("DFS solved: \n\n{} \n\nin {} seconds".format(
        solution, end - start))