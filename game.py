


# A Connect-4 game solver / best move finder for a player, using the minimax algorithm and alpha-beta pruning.







class GameManager():
    pass


class Game():
    pass


class Player():
    """An abstract class for a player."""
    
    def make_move(self) -> int:
        """Return the column where the player wants to place their piece."""
        return int(input("Enter a column: "))


class HumanPlayer(Player):
    pass


class AIPlayer(Player):
    pass



class Board():
    """
    A Connect-4 board.
    Data structure: 2D list of integers ordered by rows (dim1) and columns (dim2).
    Data entries are 0 if empty, 1 if player 1, 2 if player 2.
    """
    # Constants
    WIDTH = 7
    HEIGHT = 6

    def __init__(self, player1: Player = None, player2: Player = None):
        self.board: list[list[int]] = [[0 for _ in range(self.WIDTH)] for _ in range(self.HEIGHT)]
        self.turn: int = 1
        self.player1: Player = player1
        self.player2: Player = player2

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.board])

    def current_player(self) -> Player:
        return self.player1 if self.turn == 1 else self.player2

    def is_full(self) -> bool:
        return all(self.board[0])
    
    # The game will check for a win after each move, so we don't need to check for a win here.
    # Same for game over.

    def move(self, column: int) -> int:
        """
        Make a move in the given column.
        Returns the row where the piece was placed.
        """

        for row in range(self.HEIGHT):
            if self.board[row][column] == 0:
                self.board[row][column] = self.turn
                break
        
        self.turn = 3 - self.turn   # Switch player
        return row


    



if __name__ == '__main__':
    pass














