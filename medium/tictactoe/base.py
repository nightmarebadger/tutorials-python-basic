# -*- coding: utf-8 -*-

"""
    A basic implementation of the TicTacToe game which can be played by two
    human players.
"""


board_print_style = """

+---+---+---+
| {6} | {7} | {8} |
+---+---+---+
| {3} | {4} | {5} |
+---+---+---+
| {0} | {1} | {2} |
+---+---+---+
"""


def check_same(li):
    same = all([i == li[0] for i in li])
    if same and li[0] != ' ':
        return li[0]
    return False


class TicTacToe(object):
    """A class for the TicTacToe game."""
    def __init__(self):
        self.ply1 = 'X'
        self.ply2 = 'O'
        self.ply = self.ply1
        self.board = [' ' for i in range(9)]

    def change_players(self):
        if self.ply == self.ply1:
            self.ply = self.ply2
        else:
            self.ply = self.ply1

    def __str__(self):
        return board_print_style.format(*self.board)

    def make_move(self, n):
        self.board[n] = self.ply

    def get_possible_moves(self):
        return [i+1 for i in range(9) if self.board[i] == ' ']

    def get_move(self):
        moves = self.get_possible_moves()
        print("Possible moves: {0}".format(moves))
        try:
            x = int(raw_input("Next move: "))
        except ValueError:
            x = None
        while x not in moves:
            try:
                x = int(raw_input("Next move: "))
            except ValueError:
                pass
        return x

    def check_win(self):
        possible_win = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [6, 4, 2]
        ]

        for pos in possible_win:
            res = check_same([
                self.board[pos[0]],
                self.board[pos[1]],
                self.board[pos[2]]
            ])
            if res:
                print(self)
                print("{0} won!".format(res))
                return res

    def play(self):
        while not self.check_win() and self.get_possible_moves():
            print(self)

            x = self.get_move()

            self.make_move(x - 1)
            self.change_players()

        if not self.check_win():
            print(self)
            print("Nobody won!")


if __name__ == "__main__":
    ttt = TicTacToe()
    ttt.play()
