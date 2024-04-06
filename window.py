from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, width=width,
                               height=height, background='gray75')
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

    def draw_line(self, line, color):
        line.draw(self.__canvas, color)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, point_A, point_B):
        self.__point_A = point_A
        self.__point_B = point_B

    def draw(self, canvas, color):
        x1 = self.__point_A.x
        y1 = self.__point_A.y

        x2 = self.__point_B.x
        y2 = self.__point_B.y

        canvas.create_line(x1, y1, x2, y2, fill=color, width=2)

        self.__canvas.pack(expand=1, fill=BOTH)



