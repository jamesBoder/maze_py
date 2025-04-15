from window import Window
from point import Point, Line
from cell import Cell
from maze import Maze
        
# Set up the screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def main():
    # Create a window with dimensions
    win = Window(800, 600)
    
    # Create a maze (adjust parameters as needed)
    maze = Maze(10, 10, 50, 50, 10, 10, win)
    
   
    
    
    
    # This is the key line - it starts the event loop that keeps the window open
    win._run()






if __name__ == "__main__":
    main()
    
    
    
    

    
        

   
