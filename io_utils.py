import click
import keyboard
from game2048 import ArrowDirection, Game2048, GameStatus


class IO_Utils:
    def __init__(self):
        self._arrows = {'4': ArrowDirection.LEFT, '6': ArrowDirection.RIGHT, '8': ArrowDirection.UP, '2':ArrowDirection.DOWN }

    def __init_game(self):
        while True:
            click.echo('Start Game? [yn] ', nl=False)
            c = click.getchar()
            click.echo(c)
            if c == 'y':
                return Game2048()
            elif c == 'n':
                click.echo('Bye Bye :)')
                exit()
            else:
                click.echo('Not a valid input.')

    def run_game(self):
        self._game = self.__init_game()
        should_print = True
        while self._game.game_status is GameStatus.RUNNING:
            if should_print:
                self.__print_board()
            click.echo('Click an Arrow')
            should_print = self.__get_next_move()

        if self._game.game_status is GameStatus.WIN:
            self.__print_board()
            click.echo('Congratulation! You Won!')
        elif self._game.game_status is GameStatus.LOSS:
            click.echo('Oops! You Lost!')

    def __get_next_move(self):
        c = click.getchar()
        if c not in self._arrows:
            click.echo('Not a valid input.')
            return False
        else:
            self._game.step_board_forward(self._arrows[c])
            return True

    def __print_board(self):
        board = self._game.get_board()
        for line in board:
            click.echo('  '.join(map(self.__str_zeros_to_hashes, line)))

    def __str_zeros_to_hashes(self, number):
        str_num = str(int(number)) if number != 0 else '#'
        num_of_spaces = 4 - len(str_num)
        return str_num + num_of_spaces*' '
