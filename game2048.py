from enum import Enum
import numpy as np
import random
import math
import copy

class GameStatus(Enum):
    RUNNING = 1
    WIN = 2
    LOSS = 3


class ArrowDirection(Enum):
    LEFT = 1
    RIGHT = 2
    UP = 3
    DOWN = 4


class Game2048:
    def __init__(self, board = None):
        if board is None:
            self._board = self.__initialize_board()
        else:
            self._board = board
        self.game_status = GameStatus.RUNNING

    def get_board(self):
        return self._board

    def step_board_forward(self, direction, prevent_new_number = False):
        if direction not in ArrowDirection:
            return None

        # rotating so it would be like RIGHT move
        new_board = self._board
        new_board = self.__rotate_to_right(direction, new_board)
        new_board = self.__calc_next_right_dir(new_board, prevent_new_number)
        self._board = self.__rotate_back(direction, new_board)

    def __rotate_back(self, direction, board):
        # rotating back
        if direction is ArrowDirection.LEFT:
            board = np.fliplr(board)
        elif direction is ArrowDirection.UP:
            board = np.fliplr(board)
            board = np.transpose(board)
        elif direction is ArrowDirection.DOWN:
            board = np.transpose(board)
        return board

    def __rotate_to_right(self, direction, board):
        if direction is ArrowDirection.LEFT:
            board = np.fliplr(board)
        elif direction is ArrowDirection.UP:
            board = np.transpose(board)
            board = np.fliplr(board)
        elif direction is ArrowDirection.DOWN:
            board = np.transpose(board)
        return board

    def __initialize_board(self):
        new_board = np.zeros(16)
        initial_indices_with_2 = random.sample(
            range(0, new_board.size), 2)
        new_board[initial_indices_with_2] = 2
        return new_board.reshape(int(math.sqrt(16)), int(math.sqrt(16)))

    def __calc_next_right_dir(self, board, prevent_new_number):
        row_num = 0
        before_board = copy.copy(board)
        for row in board:
            new_row = self.__cumsum_row(row)
            board[row_num, :] = new_row
            if 2048 in new_row:
                self.game_status = GameStatus.WIN
            row_num = row_num + 1

        if self.game_status == GameStatus.RUNNING:
            all_zeros_indices = np.where(board == 0)
            if len(all_zeros_indices[0]) == 0:
                self.game_status = GameStatus.LOSS
                return board
            if not np.array_equal(before_board,board) and not prevent_new_number:
                board = self.__add_new_2(board, all_zeros_indices)

        return board

    def __cumsum_row(self, row): 
        all_zeros = row[np.where(row == 0)]
        all_none_zeros_before_duplicating = row[np.where(row != 0)]
        
        if len(all_none_zeros_before_duplicating) == 1:
            return np.concatenate([all_zeros, all_none_zeros_before_duplicating])

        for i in range(len(all_none_zeros_before_duplicating)-1,-1,-1):
                if i > 0 and all_none_zeros_before_duplicating[i] == all_none_zeros_before_duplicating[i-1]:
                    all_none_zeros_before_duplicating[i] = 2*all_none_zeros_before_duplicating[i-1]
                    all_none_zeros_before_duplicating[i-1] = 0
        all_none_zeros = all_none_zeros_before_duplicating[np.where(all_none_zeros_before_duplicating != 0)]
        all_extra_zeros = all_none_zeros_before_duplicating[np.where(all_none_zeros_before_duplicating == 0)]

        return np.concatenate([all_zeros, all_extra_zeros,all_none_zeros])

    def __add_new_2(self, next_board, all_zeros_in_board):
        rnd_sample = random.randint(0,len(all_zeros_in_board[0]) - 1)
        new_index_with_2 = (all_zeros_in_board[0][rnd_sample],all_zeros_in_board[1][rnd_sample])
        next_board[new_index_with_2] = 2
        return next_board
