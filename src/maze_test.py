import unittest
from maze import Maze
from window import Window
from cell import Cell

class MazeTest(unittest.TestCase):
    def setUp(self):
        # Create a window for testing
        self.win = Window(800, 600)
        # Initialize a maze with specific parameters
        self.maze = Maze(10, 10, 10, 10, 20, 20, self.win)

    def tearDown(self):
        # Close the window after tests
        if hasattr(self, 'window') and self.window:
            self.window.close()
    
    def test_create_cells(self):
        # Check if the cells are created correctly
        self.assertEqual(len(self.maze._cells), 10)
        self.assertEqual(len(self.maze._cells[0]), 10)
    
    def test_draw_cell(self):
        # Test drawing a cell
        cell = self.maze._cells[0][0]
        cell.draw()
        # Check if the cell's walls are drawn correctly
        self.assertTrue(cell.has_left_wall)
        self.assertTrue(cell.has_top_wall)
        self.assertTrue(cell.has_right_wall)
        self.assertTrue(cell.has_bottom_wall)
    
    def test_draw_move(self):
        # Test drawing a move between cells
        cell1 = self.maze._cells[0][0]
        cell2 = self.maze._cells[0][1]
        cell1.draw_move(cell2)
        # Check if the move was drawn correctly
        self.assertFalse(cell1.has_right_wall)
        self.assertFalse(cell2.has_left_wall)
        # Check if the cells are drawn in the window
        self.assertIsNotNone(cell1._win.canvas.find_all())
        self.assertIsNotNone(cell2._win.canvas.find_all())
    
    def test_draw_path(self):
        # Test drawing a path between cells
        cell1 = self.maze._cells[0][0]
        cell2 = self.maze._cells[1][0]
        cell1.draw_move(cell2)
        # Check if the path was drawn correctly
        
        
    
    def test_break_walls_r(self):
        # Test the recursive wall-breaking algorithm
        self.maze._break_walls_r(0, 0)
        # Check if the walls are broken correctly
        cell = self.maze._cells[0][0]
        self.assertFalse(cell.has_bottom_wall)
        self.assertFalse(cell.has_right_wall)
  
    def test_solve(self):
        # Test the maze-solving algorithm
        self.maze.solve()
        # Check if the path is found
        cell = self.maze._cells[0][0]
        self.assertTrue(cell.visited)
        # Check if the path is drawn correctly
        cell.draw()
        self.assertIsNotNone(cell._win.canvas.find_all())

    def test_solve_r(self):
        # Test the recursive maze-solving algorithm
        self.maze._solve_r(0, 0)
        # Check if the path is found
        cell = self.maze._cells[0][0]
        self.assertTrue(cell.visited)
        # Check if the path is drawn correctly
        cell.draw()
        self.assertIsNotNone(cell._win.canvas.find_all())

    def test_reset_cells_visited(self):
        # Test resetting visited cells
        self.maze._reset_cells_visited()
        for row in self.maze._cells:
            for cell in row:
                self.assertFalse(cell.visited)
    

    
    

if __name__ == "__main__":
    unittest.main()
    Window._run()
    







  