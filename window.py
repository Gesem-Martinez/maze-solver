from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, width=width,
                               height=height, background='white')
        self.__canvas.pack(expand=1, fill=BOTH)
        self.__isWindowRunning = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__root.mainloop()
        self.__isWindowRunning = True
        while self.__isWindowRunning:
            self.redraw()

    def close(self):
        self.__isWindowRunning = False

    def draw_line(self, line, color="black"):
        line.draw(self.__canvas, color)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, point_A, point_B):
        self.point_A = point_A
        self.point_B = point_B

    def draw(self, canvas, color="black"):
        x1 = self.point_A.x
        y1 = self.point_A.y

        x2 = self.point_B.x
        y2 = self.point_B.y

        canvas.create_line(x1, y1, x2, y2, fill=color, width=2)

        canvas.pack(expand=1, fill=BOTH)


class Cell:
    def __init__(self, win=None, left_wall=True, top_wall=True, right_wall=True, bottom_wall=True):
        self.has_left_wall = left_wall
        self.has_top_wall = top_wall
        self.has_right_wall = right_wall
        self.has_bottom_wall = bottom_wall
        self.__x1 = None
        self.__x2 = None
        self.__y1 = None
        self.__y2 = None
        self.__win = win
        self._visited = False

    def draw(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2

        if self.has_left_wall:
            self.__win.draw_line(Line(Point(x1, y1), Point(x1, y2)))
        else:
            self.__win.draw_line(Line(Point(x1, y1), Point(x1, y2)), "white")

        if self.has_top_wall:
            self.__win.draw_line(Line(Point(x1, y1), Point(x2, y1)))
        else:
            self.__win.draw_line(Line(Point(x1, y1), Point(x2, y1)), "white")

        if self.has_right_wall:
            self.__win.draw_line(Line(Point(x2, y1), Point(x2, y2)))
        else:
            self.__win.draw_line(Line(Point(x2, y1), Point(x2, y2)), "white")

        if self.has_bottom_wall:
            self.__win.draw_line(Line(Point(x1, y2), Point(x2, y2)))
        else:
            self.__win.draw_line(Line(Point(x1, y2), Point(x2, y2)), "white")

    def draw_move(self, to_cell, undo=False):
        own_middle_x = abs((self.__x2 - self.__x1) / 2) + self.__x1
        own_middle_y = abs((self.__y2 - self.__y1) / 2) + self.__y1

        own_middle = Point(own_middle_x, own_middle_y)

        other_middle_x = abs(
            ((to_cell.__x2 - to_cell.__x1) / 2) + to_cell.__x1)
        other_middle_y = abs(
            ((to_cell.__y2 - to_cell.__y1) / 2) + to_cell.__y1)

        other_middle = Point(other_middle_x, other_middle_y)

        middle_line = Line(own_middle, other_middle)

        color = "red"

        if undo:
            color = "gray"

        self.__win.draw_line(middle_line, color)
