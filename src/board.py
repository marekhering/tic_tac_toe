import typing as tp

import numpy as np

from .mark import Mark


class Board:
    def __init__(self):
        self.matrix = np.zeros((3, 3))

    def reset(self):
        self.matrix = np.zeros((3, 3))

    def add_mark(self, field_index: tp.Tuple[int, int], mark: Mark):
        assert self.field_is_empty(field_index)
        self.matrix[field_index] = mark

    def check_win(self, mark: Mark):
        marked_matrix = self.matrix == mark
        columns = np.all(np.logical_and(self.matrix == self.matrix[0, :], marked_matrix), axis=0)
        rows = np.all(np.logical_and(self.matrix, marked_matrix), axis=1)
        diagonals = np.all(np.stack([marked_matrix.diagonal(), np.fliplr(marked_matrix).diagonal()]), axis=1)
        if np.any(np.concatenate([columns, rows, diagonals], axis=0)):
            return True
        return False

    def check_tie(self):
        return not np.any(self.matrix == 0)

    def field_is_empty(self, field_index):
        return self.matrix[field_index] == 0

    def get_matrix(self):
        return self.matrix
