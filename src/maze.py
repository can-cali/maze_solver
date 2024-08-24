from cell import Cell
import time
import random

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
        seed=None,
    ):
        self._x1 = x1 # offset from the left side of the window
        self._y1 = y1 # offset from the top side of the window
        self._num_rows = num_rows # number of rows
        self._num_cols = num_cols # number of columns
        self._cell_size_x = cell_size_x # width of a cell
        self._cell_size_y = cell_size_y # height of a cell
        self._win = win # window object to draw the maze
        if seed:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
    
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

    def _break_walls_r(self, i, j):
        curr = self._cells[i][j]
        curr.visited = True

        while True:
            neighbors = []
            #left
            if i > 0 and not self._cells[i - 1][j].visited:
                neighbors.append((i - 1, j))
            # right
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                neighbors.append((i + 1, j))
            # up
            if j > 0 and not self._cells[i][j - 1].visited:
                neighbors.append((i, j - 1))
            # down
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                neighbors.append((i, j + 1))
            
            if len(neighbors) == 0:
                self._draw_cell(i, j)
                break
            else:
                select = random.randint(0, len(neighbors)-1)
                selected = neighbors[select]
                # right
                if selected[0] == i + 1:
                    self._cells[i][j].has_right_wall = False
                    self._cells[i + 1][j].has_left_wall = False
                # left
                if selected[0] == i - 1:
                    self._cells[i][j].has_left_wall = False
                    self._cells[i - 1][j].has_right_wall = False
                # down
                if selected[1] == j + 1:
                    self._cells[i][j].has_bottom_wall = False
                    self._cells[i][j + 1].has_top_wall = False
                # up
                if selected[1] == j - 1:
                    self._cells[i][j].has_top_wall = False
                    self._cells[i][j - 1].has_bottom_wall = False
                
            
            self._break_walls_r(selected[0], selected[1])
    
    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in range (self._num_rows):
                self._cells[i][j].visited = False




