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

        
    def draw(self):
        if self._win:
            if self.has_left_wall:
                self._win.draw_line(Line(Point(self.x1, self.y1), Point(self.x1, self.y2)))
            if self.has_right_wall:
                self._win.draw_line(Line(Point(self.x2, self.y1), Point(self.x2, self.y2)))
            if self.has_top_wall:
                self._win.draw_line(Line(Point(self.x1, self.y1), Point(self.x2, self.y1)))
            if self.has_bottom_wall:
                self._win.draw_line(Line(Point(self.x1, self.y2), Point(self.x2, self.y2)))
        else:
            raise ValueError("Window object is not set. Cannot draw cell.")
        
    def draw_move(self, to_cell, undo=False):
        # Only proceed if we have a window and it's not destroyed
        if self._win is None:
            return
        
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
                    


            

            
       
        
            