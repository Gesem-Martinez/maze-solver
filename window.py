from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root_wg = Tk()
        self.__root_wg.title = "root"
        self.canvas = Canvas()
        self.canvas.pack(expand=1)
        self.is_running = False

        self.__root_wg.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root_wg.update_idletasks()
        self.__root_wg.update()

    def wait_for_close(self):
        self.is_running = True
        while self.is_running:
            self.redraw()

    def close(self):
        self.is_running = False

