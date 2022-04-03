import typing as tp

import pygame as pg

from .board import Board
from .mark import Mark


class Screen:
    def __init__(self, width: int, height: int, board: Board, background_color=None):
        self.width = width
        self.height = height

        self.pg_screen = pg.display.set_mode((width, height))
        self.board = board
        self.background_color = background_color
        self.caption = ""
        self._font = pg.font.Font('freesansbold.ttf', 64)

    def reset(self):
        self.caption = ""

    def set_caption(self, caption: str):
        self.caption = caption

    def set_background_color(self, color):
        self.background_color = color

    def draw(self):
        if self.background_color:
            self.pg_screen.fill(self.background_color)
        self._draw_grid()
        self._draw_board()
        self._draw_caption((int(self.width / 2), int(self.height / 2)))

    def _draw_grid(self, width: int = 1, color: tp.Tuple[int, int, int] = None):
        color = color if color is not None else (0, 0, 0)

        pg.draw.line(self.pg_screen, color, (self.width / 3, 0), (self.width / 3, self.height), width=width)
        pg.draw.line(self.pg_screen, color, (self.width * 2 / 3, 0), (self.width * 2 / 3, self.height), width=width)
        pg.draw.line(self.pg_screen, color, (0, self.height / 3), (self.width, self.height / 3), width=width)
        pg.draw.line(self.pg_screen, color, (0, self.height * 2 / 3), (self.width, self.height * 2 / 3), width=width)

    def _draw_board(self):
        for i, row in enumerate(self.board.matrix):
            y = int(i * self.height / 3 + self.height / 6)
            for j, mark in enumerate(row):
                x = int(j * self.width / 3 + self.width / 6)
                if mark == Mark.X:
                    self._draw_x_mark((x, y), int(self.height / 6))
                if mark == Mark.O:
                    self._draw_o_mark((x, y), int(self.height / 6))

    def _draw_x_mark(self, center: tp.Tuple[int, int], size: int,
                     width: int = 1, color: tp.Tuple[int, int, int] = None):
        color = color if color is not None else (0, 0, 0)
        x1 = center[0] - size / 2
        x2 = center[0] + size / 2
        y1 = center[1] - size / 2
        y2 = center[1] + size / 2

        pg.draw.line(self.pg_screen, color, (x1, y1), (x2, y2), width=width)
        pg.draw.line(self.pg_screen, color, (x1, y2), (x2, y1), width=width)

    def _draw_o_mark(self, center: tp.Tuple[int, int], size: int,
                     width: int = 1, color: tp.Tuple[int, int, int] = None):
        color = color if color is not None else (0, 0, 0)
        pg.draw.circle(self.pg_screen, color, center, size / 2, width=width)

    def _draw_caption(self, center: tp.Tuple[int, int]):
        font = pg.font.Font('freesansbold.ttf', 64)
        text = font.render(self.caption, True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = center
        self.pg_screen.blit(text, text_rect)
