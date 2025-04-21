from window import Window
from point import Point, Line
from cell import Cell
from maze import Maze
        
# Set up the screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def main():

    
    # Create a maze with appropriate dimensions
    maze = Maze(
        x1=50,               # Starting x position
        y1=50,               # Starting y position
        num_rows=10,         # Number of rows
        num_cols=10,         # Number of columns
        cell_size_x=30,      # Cell width
        cell_size_y=30,      # Cell height
        seed=0               # Optional seed for consistent testing
    )
    # Draw the maze
    for row in maze._cells:
        for cell in row:
            cell.draw()

    # Break entrance and exit walls
    maze._break_entrance_and_exit()
    
    # Start the recursive wall-breaking algorithm
    maze._break_walls_r(0, 0)

    # Reset visited cells
    maze._reset_cells_visited()

    

    
    
   # Keep window running
    maze.win._run()
    
    # Close the window after use
    maze.win.close()
    
    
    
   






if __name__ == "__main__":
    main()
    
    
    
    

    
        

   
