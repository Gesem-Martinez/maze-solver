from window import Window
from maze import Maze


def main():
    window = Window(800, 600)
    maze = Maze(100, 100, 12, 16, 50, 50, window, 0)

    maze._create_cells()

    window.wait_for_close()
