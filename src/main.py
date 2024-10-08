from window import Window
from point import Point
from line import Line
from cell import Cell
from maze import Maze

def main():
    win = Window(800,600)
    maze = Maze(10, 10, 10, 10, 80, 60, win)
    maze.solve()
    win.redraw()
    win.wait_for_close()


if __name__ == "__main__":
    main()