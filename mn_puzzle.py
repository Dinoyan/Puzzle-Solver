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
        return (type(other) == type(self) and
                       self.n == other.n and self.m == other.m and
                       self.from_grid == other.to_grid)        
            
    def __str__(self):
        '''(self) -> str
        Returns the 
        '''
        from_grid = ''
        for row in self.from_grid:
            from_grid += str(row) + '\n'
        to_grid = ''
        for row in self.to_grid:
            to_grid += str(row)  + '\n'
        return "From Grid:" +'\n' + from_grid + '\n' +  'To Grid' + '\n' + to_grid
        
    # __repr__ is up to you

    # TODO
    # override extensions
    # legal extensions are configurations that can be reached by swapping one
    # symbol to the left, right, above, or below "*" with "*"
    def extensions(self):
        '''(self) -> list
        '''
        extensions = []
        coor = self.get_space_coor()
        row, column = coor[0], coor[1]
        print('fefewfefwefefefwf' + str(column))
        print(self.m)
        print(self.n)
        # Down move
        if row + 1 < self.n:
            grid_copy = deepcopy(self.from_grid)
            lst_grid = self.convert_to_lst(grid_copy)
            value = lst_grid[row + 1][column]
            lst_grid[row + 1][column] = '*'
            lst_grid[row][column] = value
            extensions.append(MNPuzzle(self.convert_to_tuple(lst_grid), target_grid))    

        # Up move
        if row + 1 > self.n:
            grid_copy = deepcopy(self.from_grid)
            lst_grid = self.convert_to_lst(grid_copy)
            value = lst_grid[row - 1][column]
            lst_grid[row - 1][column] = '*'
            lst_grid[row][column] = value
            extensions.append(MNPuzzle(self.convert_to_tuple(lst_grid), target_grid))                    

        # Right Move
        if column + 1 < self.m:
            grid_copy = deepcopy(self.from_grid)
            lst_grid = self.convert_to_lst(grid_copy)
            value = lst_grid[row][column + 1]
            lst_grid[row][column + 1] = '*'
            lst_grid[row][column] = value
            extensions.append(MNPuzzle(self.convert_to_tuple(lst_grid), target_grid))

        # Left move
        if column + 1 > self.m:
            grid_copy = deepcopy(self.from_grid)
            lst_grid = self.convert_to_lst(grid_copy)
            value = lst_grid[row][column - 1]
            lst_grid[row][column - 11] = '*'
            lst_grid[row][column] = value
            extensions.append(MNPuzzle(self.convert_to_tuple(lst_grid), target_grid))              
        return extensions
    
    def get_space_coor(self):
        '''
        '''
        row_coor = 0
        space_coor = 0
        # Get the coordinate of the empty space '*'
        for sub_row in self.from_grid:
            for item in sub_row:
                if item == '*':
                    # Create a tuple with the coordinates
                    empty_coor = (row_coor, space_coor)
                space_coor += 1
            row_coor += 1
            space_coor = 0
        return empty_coor
    
    def convert_to_lst(self, grid):
        '''
        '''
        return list(list(row) for row in grid)


    def convert_to_tuple(self, grid):
        '''
        '''
        return tuple(tuple(row) for row in grid)
    

    # TODO
    # override is_solved
    # a configuration is solved when from_grid is the same as to_grid
    def is_solved(self):
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
