from point import Point, Line

class Cell:
    def __init__(self,
                 x1,
                 x2,
                 y1,
                 y2,
                 _win,
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

            # Debugging: Print the coordinates of the cell
            print(f"Left Wall Before Draw: {self.has_left_wall}")  # Debug
            
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
        midpoint_x = (self.x1 + self.x2) // 2
        midpoint_y = (self.y1 + self.y2) // 2

        print(f"id(to_cell): {id(to_cell)}")

        if undo:
            if to_cell.x1 == self.x2:
                
                # draw right line
                self.has_right_wall = False
                to_cell.has_left_wall = False   
                #self._win.draw_line(Line(Point(self.x2, midpoint_y), Point(to_cell.x1, midpoint_y)), fill_color="red")
            elif to_cell.x2 == self.x1:
                
                # draw left line
                self.has_left_wall = False
                to_cell.has_right_wall = False
                #self._win.draw_line(Line(Point(self.x1, midpoint_y), Point(to_cell.x2, midpoint_y)), fill_color="red")
            elif to_cell.y1 == self.y2:
                
                # draw top line
                self.has_bottom_wall = False
                to_cell.has_top_wall = False
                #self._win.draw_line(Line(Point(midpoint_x, self.y2), Point(midpoint_x, to_cell.y1)), fill_color="red")
            elif to_cell.y2 == self.y1:
                
                # draw bottom line
                self.has_top_wall = False
                to_cell.has_bottom_wall = False
                #self._win.draw_line(Line(Point(midpoint_x, self.y1), Point(midpoint_x, to_cell.y2)), fill_color="red")
            else:
                raise ValueError("Invalid move direction.")
        else:
            if to_cell.x1 == self.x2:
                # draw left line
                self.has_right_wall = False
                to_cell.has_left_wall = False
                #self._win.draw_line(Line(Point(self.x2, midpoint_y), Point(to_cell.x1, midpoint_y)), fill_color="gray")
            elif to_cell.x2 == self.x1:
                # draw right line
                self.has_left_wall = False
                to_cell.has_right_wall = False
                #self._win.draw_line(Line(Point(self.x1, midpoint_y), Point(to_cell.x2, midpoint_y)), fill_color="gray")
            elif to_cell.y1 == self.y2:
                # draw top line
                print(f"Updating walls: self at ({self.x1}, {self.y1}), to_cell at ({to_cell.x1}, {to_cell.y1})")
                self.has_bottom_wall = False
                to_cell.has_top_wall = False
                print(f"self.has_bottom_wall AFTER Update: {self.has_bottom_wall}")  # Debugging
                print(f"to_cell.has_top_wall AFTER Update: {to_cell.has_top_wall}")  # Debugging
                #self._win.draw_line(Line(Point(midpoint_x, self.y2), Point(midpoint_x, to_cell.y1)), fill_color="gray")
            elif to_cell.y2 == self.y1:
                # draw bottom line
                self.has_top_wall = False
                to_cell.has_bottom_wall = False
                #self._win.draw_line(Line(Point(midpoint_x, self.y1), Point(midpoint_x, to_cell.y2)), fill_color="gray")
            else:
                raise ValueError("Invalid move direction.")


            
       
        
            