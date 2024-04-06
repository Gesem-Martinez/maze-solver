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
        self.__isWindowRunning = True
        while self.__isWindowRunning:
            self.redraw()

    def close(self):
        self.__isWindowRunning = False
