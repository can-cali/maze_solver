from point import *

class Line:
    def __init__(self, start, end): # start and end are Point objects
        self.start = start
        self.end = end
    
    def draw(self, canvas, color="black"):
        canvas.create_line(self.start.x, self.start.y, self.end.x, self.end.y, fill=color, width=2)
    
