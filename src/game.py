import time
import typing as tp

import pygame as pg

from .mark import Mark
from .mouse import Mouse
from .board import Board
from .screen import Screen
from config import GAME_NAME, FPS_LIMIT, SCREEN_WIDTH, SCREEN_HEIGHT


class Game:
    def __init__(self):
        self.running = False
        self.game_over = False
        self.board = Board()
        self.mouse = Mouse()
        self.mark = Mark.X

        self.clock: tp.Optional[pg.time.Clock] = None
        self.screen: tp.Optional[Screen] = None

    def reset(self):
        self.game_over = False
        self.mark = Mark.X
        self.board.reset()
        self.screen.reset()
        self.mouse.reset()

    def run(self):
        pg.init()
        pg.display.set_caption(GAME_NAME)

        self.clock = pg.time.Clock()
        self.board = Board()
        self.screen = Screen(SCREEN_WIDTH, SCREEN_HEIGHT, self.board)
        self.screen.set_background_color((255, 255, 255))

        self.running = True
        self.mainloop()

    def mainloop(self):
        while self.running:
            self.clock.tick(FPS_LIMIT)
            if self.process_click():
                self.check_game_over()
            self.screen.draw()
            pg.display.update()
            self.event_handler()
            self.game_over_screen()

    def event_handler(self):
        self.mouse.reset()
        self.mouse.set_position(pg.mouse.get_pos())

        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                self.mouse.set_bottom_down()
            if event.type == pg.MOUSEBUTTONUP:
                self.mouse.set_bottom_up()

    def process_click(self):
        if self.mouse.bottom_down:
            field_index = int(self.mouse.position[1] / (self.screen.height / 3)), \
                          int(self.mouse.position[0] / (self.screen.width / 3))

            if self.board.field_is_empty(field_index):
                self.board.add_mark(field_index, self.mark)
                self.switch_mark()
                return True

    def check_game_over(self):
        caption = "X Won!" if self.board.check_win(Mark.X) else None
        caption = "O Won!" if self.board.check_win(Mark.O) else caption
        caption = "Tie!" if self.board.check_tie() else caption

        if caption:
            self.screen.set_caption(caption)
            self.game_over = True

    def game_over_screen(self):
        if self.game_over:
            time.sleep(2)
            self.reset()

    def switch_mark(self):
        self.mark = Mark.X if self.mark == Mark.O else Mark.O
