# -*- coding: utf-8 -*-

"""
A basic implementation of the TicTacToe game which can be played humans or
computer players (human vs human, human vs ai, ai vs ai).
"""

import random
import time


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
    """Check if all elements in the list are the same and not equal ' '.
    Returns False of the value in the list."""

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

        self.computer = None

    def change_players(self):
        """Change between the players."""

        if self.ply == self.ply1:
            self.ply = self.ply2
        else:
            self.ply = self.ply1

    def __str__(self):
        """Print a nice presentation of the board."""

        return board_print_style.format(*self.board)

    def make_move(self, n):
        """Make a move on the location ``n``."""

        self.board[n] = self.ply

    def get_possible_moves(self):
        """Return a list of all possible moves."""

        return [i+1 for i in range(9) if self.board[i] == ' ']

    def get_move(self):
        """Ask the player to input a move. Must input a possible move or it
        will ask again.

        :returns: The move to be made
        :rtype: ``int``
        """

        moves = self.get_possible_moves()
        print("Possible moves: {0}".format(moves))
        try:
            x = int(input("Next move: "))
        except (ValueError, NameError):
            x = None
        while x not in moves:
            try:
                x = int(input("Next move: "))
            except (ValueError, NameError):
                pass
        return x

    def _check_win(self):
        """Check if someone won. Returns None or the winning value."""

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
                return res

    def check_win(self):
        res = self._check_win()

        if res:
            print(self)
            print("{0} won!".format(res))
            return res

    def play_human(self):
        """Play the game against a human opponent."""

        self.computer = False

        while not self.check_win() and self.get_possible_moves():
            print(self)

            x = self.get_move()

            self.make_move(x - 1)
            self.change_players()

        if not self.check_win():
            print(self)
            print("Nobody won!")

    def computer_turn(self):
        return self.ply == self.ply2

    def judge(self):
        win = self._check_win()

        if win == self.ply1:
            return 1
        elif win == self.ply2:
            return -1

        if not self.get_possible_moves():
            return 0

    def computer_move(self):
        assessments = []
        for move in self.get_possible_moves():
            try:
                self.make_move(move - 1)
                self.change_players()
                # assessments.append((move, self.assess_move(move)))
                assessments.append((move, self.assess_move_optimised(move)))
            finally:
                self.revert_move(move - 1)
                self.change_players()

        # Shuffle so we don't always start the same
        random.shuffle(assessments)
        # Sort so we choose the best option
        assessments.sort(key=lambda x: x[1])

        print('Computer assessment (lower is better): {}'.format(assessments))
        if self.ply == self.ply2:
            return assessments[0][0]
        else:
            return assessments[-1][0]

    def assess_move(self, current_move):
        score = self.judge()
        if score is not None:
            return score

        assessments = []
        for move in self.get_possible_moves():
            try:
                self.make_move(move - 1)
                self.change_players()
                assessments.append(self.assess_move(move))
            finally:
                self.revert_move(move - 1)
                self.change_players()

        if self.ply == self.ply1:
            return max(assessments)
        else:
            return min(assessments)

    def assess_move_optimised(self, current_move):
        score = self.judge()
        if score is not None:
            return score

        assessments = []
        for move in self.get_possible_moves():
            try:
                self.make_move(move - 1)
                self.change_players()
                assessment = self.assess_move_optimised(move)
                # This looks 'wrong' because we're still on the 'changed'
                # player, so the scores need to be 'turned around'
                if self.ply == self.ply2 and assessment == 1:
                    return 1
                elif self.ply == self.ply1 and assessment == -1:
                    return -1
                assessments.append(assessment)
            finally:
                self.revert_move(move - 1)
                self.change_players()

        if self.ply == self.ply1:
            return max(assessments)
        else:
            return min(assessments)

    def revert_move(self, n):
        """Make a move on the location ``n``."""

        self.board[n] = ' '

    def play_vs_computer(self):
        """Play the game against a computer opponent."""

        self.computer = True

        while not self.check_win() and self.get_possible_moves():
            if not self.computer_turn():
                print(self)

                x = self.get_move()

                self.make_move(x - 1)
                self.change_players()
            else:
                t = time.time()
                self.make_move(self.computer_move() - 1)
                print('Thinking time: {}s'.format(time.time() - t))
                self.change_players()

        if not self.check_win():
            print(self)
            print("Nobody won!")

    def play_computer_vs_computer(self):
        """Play the game computer vs computer."""

        self.computer = True

        while not self.check_win() and self.get_possible_moves():
            print(self)
            t = time.time()
            self.make_move(self.computer_move() - 1)
            tt = time.time() - t
            print('Thinking time: {}s'.format(tt))
            self.change_players()

            if tt < 1:
                time.sleep(1 - tt)

        if not self.check_win():
            print(self)
            print("Nobody won!")


if __name__ == "__main__":
    ttt = TicTacToe()
    ttt.play_vs_computer()
