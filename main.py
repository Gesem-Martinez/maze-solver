from window import Window, Line, Point, Cell


def main():
    window = Window(800, 600)
    celda = Cell(True, True, False, True, window)
    celda_3 = Cell(False, True, True, True, window)

    celda.draw(100, 300, 200, 400)
    celda_3.draw(700, 300, 800, 400)

    celda.draw_move(celda_3)

    window.wait_for_close()
