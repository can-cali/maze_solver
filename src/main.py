from window import Window
from point import Point
from line import Line
from cell import Cell

def main():
    win = Window(800,600)
    p1 = Point(100,100)
    p2 = Point(200,200)
    l = Line(p1,p2)
    win.draw_line(l)

    p3 = Point(300,300)
    p4 = Point(100,400)
    l2 = Line(p3,p4)
    win.draw_line(l2, "red")

    c = Cell(win, False, True, False, True)
    c.draw(100,100,200,200)
    c.draw(300,300,400,400)
    win.wait_for_close()


if __name__ == "__main__":
    main()