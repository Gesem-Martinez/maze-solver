from window import Window, Line, Point, Cell
from maze import Maze

def main():
    window = Window(800, 600)
    maze = Maze(100, 100, 12, 16, 50, 50, window)

    maze._create_cells()

    window.wait_for_close()
