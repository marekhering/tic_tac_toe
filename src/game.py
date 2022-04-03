import typing as tp

import pygame as pg

from .screen import Screen
from config import GAME_NAME, FPS_LIMIT, SCREEN_SIZE


class Game:
    def __init__(self):
        self.clock: tp.Optional[pg.time.Clock] = None
        self.running: bool = False
        self.screen: tp.Optional[Screen] = None

    def run(self):
        pg.init()
        pg.display.set_caption(GAME_NAME)

        self.clock = pg.time.Clock()
        self.screen = Screen(*SCREEN_SIZE)
        self.running = True
        self.mainloop()

    def mainloop(self):
        while self.running:
            self.clock.tick(FPS_LIMIT)
            self.screen.draw()
            self.event_handler()
            pg.display.update()

    def event_handler(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
