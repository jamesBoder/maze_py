from window import Window
from point import Point, Line
from cell import Cell
        
if __name__ == "__main__":
    win = Window(800, 600)
    cells = {}  # Dictionary to store unique cells by coordinates
    def create_cell(x1, x2, y1, y2):
        key = (x1, x2, y1, y2)  # Unique key based on cell coordinates
        if key not in cells:
            cells[key] = Cell(x1, x2, y1, y2, win)
        return cells[key]
    # Create and store unique cells
    cell = create_cell(50, 100, 50, 100)
    cell2 = create_cell(100, 150, 50, 100)  # Adjacent on the right
    cell3 = create_cell(50, 100, 100, 150)  # Adjacent below
    cell4 = create_cell(50, 100, 0, 50)     # Adjacent above    
    
    
    win.wait_for_close()
        

   
