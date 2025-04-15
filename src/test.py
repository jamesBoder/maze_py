import unittest
from window import Window
from point import Point, Line
from cell import Cell

def setUp(self):
    self.win = Window(800, 600)
    self.cells = {}  # Dictionary to store unique cells by coordinates

    def create_cell(x1, x2, y1, y2):
        key = (x1, x2, y1, y2)  # Unique key based on cell coordinates
        if key not in self.cells:
            self.cells[key] = Cell(x1, x2, y1, y2, self.win)
        return self.cells[key]

    # Create and store unique cells
    self.cell = create_cell(50, 100, 50, 100)
    self.cell2 = create_cell(100, 150, 50, 100)  # Adjacent on the right
    self.cell3 = create_cell(50, 100, 100, 150)  # Adjacent below
    self.cell4 = create_cell(50, 100, 0, 50)     # Adjacent above
    self.cell5 = create_cell(0, 50, 50, 100)     # Adjacent on the left
    self.cell6 = create_cell(100, 150, 0, 50)    # Another adjacent above
    self.cell7 = create_cell(100, 150, 50, 100)  # Same logical location as cell2
    self.cell8 = create_cell(50, 100, 0, 50)     # Same logical location as cell4

    def test_draw(self):
        # Test drawing the cell
        self.cell.draw()
        # Check if the cell has walls drawn
        self.assertTrue(self.cell.has_left_wall)
        self.assertTrue(self.cell.has_right_wall)
        self.assertTrue(self.cell.has_top_wall)
        self.assertTrue(self.cell.has_bottom_wall)
        # Check if the cell is drawn in the window
        self.assertIsNotNone(self.cell._win.canvas.find_all())
        # Check if the cell is drawn in the window
        self.assertTrue(self.cell._win.canvas.winfo_width() > 0)
        

    def test_draw_move(self):
        print(f"ID of self.cell2 in test: {id(self.cell2)}")
        # Test moving to the left
        self.cell.draw_move(self.cell2)
        # Test moving to the right
        self.cell.draw_move(self.cell3)
        # Test moving up
        self.cell.draw_move(self.cell4)
        # Test moving down
        self.cell.draw_move(self.cell5)
        # Test undo move
        self.cell.draw_move(self.cell6, undo=True)
        # Test invalid move direction
        with self.assertRaises(ValueError):
            self.cell.draw_move(self.cell, undo=True)
        with self.assertRaises(ValueError):
            self.cell.draw_move(self.cell, undo=False)
        with self.assertRaises(ValueError):
            self.cell.draw_move(self.cell, undo=True)
        with self.assertRaises(ValueError):
            self.cell.draw_move(self.cell, undo=False)
        with self.assertRaises(ValueError):
            self.cell.draw_move(self.cell, undo=True)
        with self.assertRaises(ValueError):
            self.cell.draw_move(self.cell, undo=False)
        with self.assertRaises(ValueError):
            self.cell.draw_move(self.cell, undo=True)
        with self.assertRaises(ValueError):
            self.cell.draw_move(self.cell, undo=False)
        with self.assertRaises(ValueError):
            self.cell.draw_move(self.cell, undo=True)
        with self.assertRaises(ValueError):
            self.cell.draw_move(self.cell, undo=False)
        with self.assertRaises(ValueError):
            self.cell.draw_move(self.cell, undo=True)
        with self.assertRaises(ValueError):
            self.cell.draw_move(self.cell, undo=False)
        with self.assertRaises(ValueError):
            self.cell.draw_move(self.cell, undo=True) 
                                 

if __name__ == "__main__":
    unittest.main()