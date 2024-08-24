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
        self._x1 = x1 # offset from the left side of the window
        self._y1 = y1 # offset from the top side of the window
        self._num_rows = num_rows # number of rows
        self._num_cols = num_cols # number of columns
        self._cell_size_x = cell_size_x # width of a cell
        self._cell_size_y = cell_size_y # height of a cell
        self._win = win # window object to draw the maze

        self._create_cells()
    
    def _create_cells(self):
        self._cells = []
        for i in range(self._num_cols):
            column = []
            for j in range(self._num_rows):
                cell = Cell(self._win)
                column.append(cell)
            self._cells.append(column)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)
    
    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i* self._cell_size_x 
        y1 = self._y1 + j* self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)
        # wait for a short time to see the animation
    
    def _break_entrance_and_exit(self):
        entrance = self._cells[0][0]
        exit = self._cells[self._num_cols-1][self._num_rows-1]
        entrance.has_left_wall = False
        exit.has_right_wall = False
        self._draw_cell(0, 0)
        self._draw_cell(self._num_cols-1, self._num_rows-1)



