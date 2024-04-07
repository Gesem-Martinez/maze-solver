import time
import random
from window import Cell


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        self._cells = []

        if seed is not None:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        for i in range(self._num_rows):
            row = []

            for j in range(self._num_cols):
                row.append(Cell(self._win))

            self._cells.append(row)

        if self._win is not None:
            for i in range(self._num_rows):
                for j in range(self._num_cols):
                    self._draw_cells(i, j)

    def _draw_cells(self, i, j):
        cell_x1 = (j * self._cell_size_x) + self._x1
        cell_y1 = (i * self._cell_size_y) + self._y1

        cell_x2 = cell_x1 + self._cell_size_x
        cell_y2 = cell_y1 + self._cell_size_y

        self._cells[i][j].draw(cell_x1, cell_y1, cell_x2, cell_y2)
        self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.02)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cells(0, 0)

        self._cells[self._num_rows - 1][self._num_cols -
                                        1].has_bottom_wall = False
        self._draw_cells(self._num_rows - 1, self._num_cols - 1)

    def _break_walls_r(self, i, j):
        curr_cell = self._cells[i][j]
        curr_cell._visited = True

        while True:
            not_visited = []

            if j > 0:
                left_cell = self._cells[i][j - 1]

                if not left_cell._visited:
                    not_visited.append((i, j - 1))

            if j + 1 < len(self._cells[0]):
                right_cell = self._cells[i][j + 1]

                if not right_cell._visited:
                    not_visited.append((i, j + 1))

            if i - 1 > 0:
                top_cell = self._cells[i - 1][j]

                if not top_cell._visited:
                    not_visited.append((i - 1, j))

            if i + 1 < len(self._cells):
                bottom_cell = self._cells[i + 1][j]

                if not bottom_cell._visited:
                    not_visited.append((i + 1, j))

            # Revisar visitados
            if len(not_visited) == 0:
                self._draw_cells(i, j)
                return

            else:
                direction = random.randint(0, len(not_visited) - 1)
                next_pos = not_visited[direction]
                next_cell = self._cells[next_pos[0]][next_pos[1]]

                if next_pos[1] < j:
                    curr_cell.has_left_wall = False
                    next_cell.has_right_wall = False

                if next_pos[1] > j:
                    curr_cell.has_right_wall = False
                    next_cell.has_left_wall = False

                if next_pos[0] < i:
                    curr_cell.has_top_wall = False
                    next_cell.has_bottom_wall = False

                if next_pos[0] > i:
                    curr_cell.has_bottom_wall = False
                    next_cell.has_top_wall = False

            self._break_walls_r(next_pos[0], next_pos[1])

    def _reset_cells_visited(self):
        for i in range(len(self._cells)):
            for j in range(len(self._cells[0])):
                self._cells[i][j]._visited = False

    def resolve(self):
        self._resolve_r()

    def _resolve_r(self):
        self._animate()

