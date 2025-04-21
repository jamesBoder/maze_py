from point import Point, Line

class Cell:
    def __init__(self,
                 x1,
                 x2,
                 y1,
                 y2,
                 _win=None,
                 has_left_wall=True,
                 has_right_wall=True,
                 has_top_wall=True,
                 has_bottom_wall=True,):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self._win = _win
        self.visited = False  # Initialize visited attribute
        
    def draw(self):
        if self._win is None:
            return  # Exit if no window exists
            
        # Draw existing walls in black (or default color)
        if self.has_left_wall:
            self._win.draw_line(Line(Point(self.x1, self.y1), Point(self.x1, self.y2)))
        else:
            # Draw non-existent walls in white/background color
            self._win.draw_line(Line(Point(self.x1, self.y1), Point(self.x1, self.y2)), fill_color="#d9d9d9")
            
        if self.has_right_wall:
            self._win.draw_line(Line(Point(self.x2, self.y1), Point(self.x2, self.y2)))
        else:
            self._win.draw_line(Line(Point(self.x2, self.y1), Point(self.x2, self.y2)), fill_color="#d9d9d9")
            
        if self.has_top_wall:
            self._win.draw_line(Line(Point(self.x1, self.y1), Point(self.x2, self.y1)))
        else:
            self._win.draw_line(Line(Point(self.x1, self.y1), Point(self.x2, self.y1)), fill_color="#d9d9d9")
            
        if self.has_bottom_wall:
            self._win.draw_line(Line(Point(self.x1, self.y2), Point(self.x2, self.y2)))
        else:
            self._win.draw_line(Line(Point(self.x1, self.y2), Point(self.x2, self.y2)), fill_color="#d9d9d9")
        
    def draw_move(self, to_cell, undo=False):
        # Only proceed if we have a window and it's not destroyed
        if self._win is None:
            return
        
        # Check if cells share an edge and determine direction
        if to_cell.x1 == self.x2:  # Moving right
            self.has_right_wall = undo
            to_cell.has_left_wall = undo
        elif to_cell.x2 == self.x1:  # Moving left
            self.has_left_wall = undo
            to_cell.has_right_wall = undo
        elif to_cell.y1 == self.y2:  # Moving down
            self.has_bottom_wall = undo
            to_cell.has_top_wall = undo
        elif to_cell.y2 == self.y1:  # Moving up
            self.has_top_wall = undo
            to_cell.has_bottom_wall = undo
        
        # Redraw both cells to show the wall changes
        self.draw()
        to_cell.draw()
        
        try:
            # Calculate center of current cell
            current_center_x = (self.x1 + self.x2) / 2
            current_center_y = (self.y1 + self.y2) / 2
            
            # Calculate center of destination cell
            to_center_x = (to_cell.x1 + to_cell.x2) / 2
            to_center_y = (to_cell.y1 + to_cell.y2) / 2
            
            # Set the line color - red for normal, gray for undo
            color = "gray" if undo else "red"
            
            # Create line and draw it
            line = Line(
                Point(current_center_x, current_center_y),
                Point(to_center_x, to_center_y)
            )
            self._win.draw_line(line, fill_color=color)
        except:
            # Silently fail if drawing fails (e.g., window closed)
            pass

    def _reset_cells_visited(self):
        # reset the visited property of all cells
        for row in self._cells:
            for cell in row:
                cell.visited = False
                cell.has_left_wall = True
                cell.has_top_wall = True        
                cell.has_right_wall = True
                cell.has_bottom_wall = True
                
    
                    


            

            
       
        
            