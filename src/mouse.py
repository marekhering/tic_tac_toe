import typing as tp


class Mouse:
    def __init__(self, position: tp.Tuple[int, int] = None):
        self.bottom_up = False
        self.bottom_down = False
        self.position = position

    def set_position(self, position: tp.Tuple[int, int]):
        self.position = position

    def set_bottom_up(self):
        self.bottom_up = True

    def set_bottom_down(self):
        self.bottom_down = True

    def reset(self):
        self.bottom_up = False
        self.bottom_down = False

    def __repr__(self):
        return f'Mouse({self.position} UP:{self.bottom_up} DOWN:{self.bottom_down})'
