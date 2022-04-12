import unittest
from numpy.testing import assert_array_equal


from game2048 import ArrowDirection, Game2048
import numpy as np

class TestsGame2048Methods(unittest.TestCase):

    def test_get_board(self):
        #Arrange
        expected_board = np.array([[2,0,0],[0,2,0],[0,0,0]])
        game = Game2048(expected_board)
        
        #Act
        output_board = game.get_board()

        #Assert
        assert_array_equal(expected_board, output_board)

    def test_step_board_forward_step_right(self):
        #Arrange
        init_board = np.array([[2,0,0],[0,2,0],[0,0,0]])
        expected_board = np.array([[0,0,2],[0,0,2],[0,0,0]])
        game = Game2048(init_board)
        
        #Act
        game.step_board_forward(ArrowDirection.RIGHT,prevent_new_number = True)
        output_board = game.get_board()

        #Assert
        assert_array_equal(expected_board, output_board)
    
    def test_step_board_forward_step_left(self):
        #Arrange
        init_board = np.array([[2,0,0],[0,2,0],[0,0,0]])
        expected_board = np.array([[2,0,0],[2,0,0],[0,0,0]])
        game = Game2048(init_board)
        
        #Act
        game.step_board_forward(ArrowDirection.LEFT,prevent_new_number = True)
        output_board = game.get_board()

        #Assert
        assert_array_equal(expected_board, output_board)

    def test_step_board_forward_step_down(self):
        #Arrange
        init_board = np.array([[2,0,0],[0,2,0],[0,0,0]])
        expected_board = np.array([[0,0,0],[0,0,0],[2,2,0]])
        game = Game2048(init_board)
        
        #Act
        game.step_board_forward(ArrowDirection.DOWN,prevent_new_number = True)
        output_board = game.get_board()

        #Assert
        assert_array_equal(expected_board, output_board)

    def test_step_board_forward_step_up(self):
        #Arrange
        init_board = np.array([[2,0,0],[0,2,0],[0,0,0]])
        expected_board = np.array([[2,2,0],[0,0,0],[0,0,0]])
        game = Game2048(init_board)
        
        #Act
        game.step_board_forward(ArrowDirection.UP,prevent_new_number = True)
        output_board = game.get_board()

        #Assert
        assert_array_equal(expected_board, output_board)

if __name__ == '__main__':
    unittest.main()