import time
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
                 win=None
            ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y

        # Create a window if one isn't provided
        if win is None:
            self.win = Window(800, 600)  # Adjust size as needed
        else:
            self.win = win

        # Empty 2d list to store cells
        self._cells = [[None for _ in range(self.num_rows)] for _ in range(self.num_cols)]
        
        self._create_cells()
        
    
    def _create_cells(self):
        # Populate the 2d list with Cell objects
        for i in range(self.num_cols):
            for j in range(self.num_rows):
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
            
            cell.draw()
            self._animate()

    def _animate(self):
        if self.win is None:
            return
        # visualize the cells
        self.win.redraw()
        time.sleep(0.05)
    