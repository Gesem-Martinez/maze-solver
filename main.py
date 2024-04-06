from window import Window, Line, Point


def main():
    window = Window(800, 600)
    linea = Line(Point(10, 10), Point(20, 20))


    window.draw_line(linea, "red")

    window.wait_for_close()
