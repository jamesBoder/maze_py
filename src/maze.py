import time
import random
from cell import Cell
from window import Window



class Maze:
    def __init__(self,
                 x1,
                 y1,
                 num_rows,
                 num_cols,
                 cell_size_x,
                 cell_size_y,
                 win=None,
                 seed=None
            ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        if seed is not None:
            random.seed(seed)
        self.seed = seed


        # Create a window if one isn't provided
        if win is None:
            self.win = Window(800, 600)  # Adjust size as needed
        else:
            self.win = win

        # Empty 2d list to store cells
        self._cells = [[None for _ in range(self.num_cols)] for _ in range(self.num_rows)]
        
        self._create_cells()
        
    
    def _create_cells(self):
        # Populate the 2d list with Cell objects
        for i in range(self.num_rows):
            for j in range(self.num_cols):

                # Calculate the coordinates of the cell
                x1 = self.x1 + j * self.cell_size_x
                y1 = self.y1 + i * self.cell_size_y
                x2 = x1 + self.cell_size_x
                y2 = y1 + self.cell_size_y
                
                # Create the cell with correct coordinates
                cell = Cell(x1, x2, y1, y2, self.win)
                
                # Store the cell object in the 2d list
                self._cells[i][j] = cell
                
                # Draw the cell
                cell.draw()
                
        # Perform a single animation after all cells are created
        self._animate()
                

    def _draw_cell(self, i, j):
        if not self.win.is_running:
            return
       
        cell = self._cells[i][j]
        
        # draw the cell if we have a window
        if self.win is not None:
            
            
            # update visual representation of both cells whose walls were broken
            if i > 0:
                cell.draw_move(self._cells[i - 1][j], undo=False)
            if j > 0:
                cell.draw_move(self._cells[i][j - 1], undo=False)
            if i < self.num_rows - 1:
                cell.draw_move(self._cells[i + 1][j], undo=False)
            if j < self.num_cols - 1:
                cell.draw_move(self._cells[i][j + 1], undo=False)
        else:
            # If no window, just draw the cell
            cell.draw()
            self._animate()

    def _animate(self):
        if self.win is None:
            return
        # visualize the cells
        self.win.redraw()
        time.sleep(0.05)
    
    def _break_entrance_and_exit(self):
        # Break the entrance and exit walls
        entrance_cell = self._cells[0][0]
        exit_cell = self._cells[self.num_rows - 1][self.num_cols - 1]
        
        # Remove left wall of entrance cell 
        entrance_cell.has_left_wall = False 

        # remove bottom right wall of exit cell
        exit_cell.has_bottom_wall = False

        # Update graphical representation using _draw_cell
        entrance_cell.draw()
        exit_cell.draw()
        self._animate()

    def _break_walls_r(self, i, j):
        # Mark current cell as visited
        self._cells[i][j].visited = True
        
        
        # Get all potential neighbors
        neighbors = self._get_unvisited_neighbors(i, j)

        if not neighbors:
            self._draw_cell(i, j)
            return  # No unvisited neighbors, exit recursion
    
       
        while neighbors:
       
            # Pick a random neighbor
            idx = random.randrange(len(neighbors))
            ni, nj = neighbors.pop(idx)
                
            # Break walls between current cell and neighbor
            di, dj = ni - i, nj - j
            if di == -1:  # Moving up
                
                self._cells[i][j].has_top_wall = False
                self._cells[ni][nj].has_bottom_wall = False
                
            elif di == 1:  # Moving down
            
                self._cells[i][j].has_bottom_wall = False
                self._cells[ni][nj].has_top_wall = False
               
            elif dj == -1:  # Moving left
                
                self._cells[i][j].has_left_wall = False
                self._cells[ni][nj].has_right_wall = False
                
            elif dj == 1:  # Moving right
                
                self._cells[i][j].has_right_wall = False
                self._cells[ni][nj].has_left_wall = False
                
            # Draw bot cells to update the visual   
            self._draw_cell(i, j)
            self._draw_cell(ni, nj)

            # Recursively call the function on the neighbor
            self._break_walls_r(ni, nj)
        
        

    def _get_unvisited_neighbors(self, i, j):
        directions = [
            (-1, 0),  # Check top neighbor
            (1, 0),   # Check bottom neighbor
            (0, -1),  # Check left neighbor
            (0, 1)    # Check right neighbor
        ]

        neighbors = []

        for di, dj in directions:
            ni, nj = i + di, j + dj  # Calculate neighbor indices
            if (0 <= ni < self.num_rows and 0 <= nj < self.num_cols and
                    not self._cells[ni][nj].visited):  # Unvisited neighbor check
                neighbors.append((ni, nj))
        
        return neighbors

    def _reset_cells_visited(self):
        # reset the visited property of all cells
        for row in self._cells:
            for cell in row:
                cell.visited = False
                cell.has_left_wall = True
                cell.has_top_wall = True        
                cell.has_right_wall = True
                cell.has_bottom_wall = True
            
            
        
        
     
        
