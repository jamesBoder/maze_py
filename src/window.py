import threading

from tkinter import Tk, BOTH, Canvas, TclError
from point import Point, Line


class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root = Tk()
        self.root.title("Maze")
        self.canvas = Canvas(self.root, width=width, height=height)
        self.canvas.pack(fill=BOTH, expand=True)
        self.is_running = True
        self.task_ids = []

        # Handle window closing
        self.root.protocol("WM_DELETE_WINDOW", self._on_close)

    def schedule_task(self, delay, func):
        # Schedule `func` to run after `delay` ms and store the ID
        task_id = self.root.after(delay, func)
        self.task_ids.append(task_id)

    
    def redraw(self):
        self.root.update_idletasks()
        self.root.update()


    def _run(self):
        # Run the Tkinter event loop
        self.root.mainloop()


    def _on_close(self):
        # Set the running flag to False to exit the loop
        self.is_running = False
        self.root.destroy()
        
            
    def close(self):
        # If the window is already closed, prevent destroying it again
        if not self.is_running:
            print("Window is already destroyed!")
            return False  # Return False to indicate it's already closed
    
        # Cancel all scheduled tasks
        for task_id in self.task_ids:
            try:
                self.root.after_cancel(task_id)
            except TclError:
                print("Task already canceled or irrelevant.")

        self.task_ids.clear()  # Clear the task IDs list

        self.is_running = False  # Mark the window as "not running" anymore
        try:
            self.root.destroy()  # Safely destroy the window
        except TclError:
            print("Cannot destroy the window because it has already been destroyed.")
            return False
        return True  # Successful closure
    
    def draw_line(self, line, fill_color="black"):
        if not self.is_running:
            print("Cannot draw-window is closed")
            return
        self.root.after(0, lambda: line.draw(self.canvas, fill_color))