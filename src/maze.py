from cell import Cell
import time

class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        
        self._create_cells()
    
    def _create_cells(self):
        self._cells = []
        for i in range(self._num_cols):
            column = []
            for j in range(self._num_rows):
                cell = Cell(self._win)
                column.append(cell)
            self._cells.append(column)
        self._draw_cell(self._cell_size_x, self._cell_size_y)
    
    def _draw_cell(self, i, j):
        for row in range(self._num_rows):
            for col in range(self._num_cols):
                self._cells[col][row].draw(i*col, j*row, i*(col+1), j*(row+1))
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)
        # wait for a short time to see the animation


