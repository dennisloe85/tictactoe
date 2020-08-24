#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""The old  game classic "TicTacToe" in Python

    @todo: Add minimax

"""

from copy import deepcopy
from enum import Enum, auto
from random import randint

class TicTacToe:


    board = []

    class BoardElem(Enum):
        X       = auto()
        O       = auto()
        EMPTY   = auto()

    def _init(self):


        empty = self.BoardElem.EMPTY

        self.board = [[empty, empty, empty],
                      [empty, empty, empty],
                      [empty, empty, empty]]

    def _get_random_move(cls, board):
        available_pos = []

        # Get list of available moves
        for v in range(0, len(board)):
            for h in range(0, len(board[v])):
                if board[v][h] == cls.BoardElem.EMPTY:
                    available_pos.append([h,v])


        if len(available_pos) == 0:
            return []
        else:
            # Chose randomly from available moves
            return available_pos[ randint( 0, len(available_pos) - 1 ) ]

   
    def _show_board(cls, board):
        print() 
        print("      A     B     C\n")

        for idx, row in enumerate(board):
            print(" " + str(idx + 1) + "    " + '  |  '.join(" " if x == cls.BoardElem.EMPTY else x.name for x in row))
            if idx != len(board) - 1: print("    -----------------")
        print() 
        print() 

    def _are_three_equal(cls, a, b, c):
        return a == b and b == c

    def _get_winner(cls, board):
        won_player = cls.BoardElem.EMPTY

        # Check rows and columns
        for x in range(len(board)):
            # Check columns
            if cls._are_three_equal(board[0][x], board[1][x], board[2][x]) and board[0][x] != cls.BoardElem.EMPTY:
                won_player = board[0][x]
                break

            # Check row
            if cls._are_three_equal(board[x][0], board[x][1], board[x][2]) and board[x][0] != cls.BoardElem.EMPTY:
                won_player = board[x][0]
                break

        # Check diagonals if no winner found
        if won_player == cls.BoardElem.EMPTY and cls._are_three_equal(board[0][0], board[1][1], board[2][2]) and board[0][0] != cls.BoardElem.EMPTY:
            won_player = board[0][0]
        if won_player == cls.BoardElem.EMPTY and cls._are_three_equal(board[0][2], board[1][1], board[2][0]) and board[0][2] != cls.BoardElem.EMPTY:
            won_player = board[0][2]       

        return won_player

    def run(self, ai_active = True):
        self._init()

        curr_player = self.BoardElem.X

        print()
        print("############ TicTacToe ############")
        print()

        # Game loop
        run_game = True
        while(run_game):
            self._show_board(self.board)


            # Some won the game?
            tmp_winner = self._get_winner(self.board)
            if tmp_winner != self.BoardElem.EMPTY:
                print()
                print(tmp_winner.name + " won the game!")
                print()
                run_game = False
                break
            elif sum( x.count(self.BoardElem.EMPTY) for x in self.board) == 0:
                print()
                print("Tie!")
                print()
                run_game = False
                break



            # Get next move either from AI for "O" or from human input
            next_pos = []
            if ai_active and curr_player == self.BoardElem.O:
                next_pos = self._get_random_move(self.board)
                print("It's " + curr_player.name + "'s turn. " + curr_player.name + " selects " + chr(ord("A") + next_pos[0]) + str(next_pos[1] + 1) + ".")
            else:
                # Get input until it's valid
                while(next_pos == []):

                    input_pos = input("It's " + curr_player.name + "'s turn. Please select your next position (e.g. A2): ")     
                    print()      

                    # Remove whitespaces, tabs, new lines etc.
                    input_pos = "".join( input_pos.split() )
                    input_pos = input_pos.upper()

                    # Check length
                    if len(input_pos) != 2:
                        print("Wrong format entered!")
                        print()
                        continue 

                    # Check format (e.g. A2)
                    if not (input_pos[0] in ["A", "B", "C"] and input_pos[1] in ["1", "2", "3"]):
                        print("Wrong format entered!")
                        print()
                        continue 

                    # Get indices
                    next_pos_user_tmp = [ ord(input_pos[0]) - ord("A") , ord(input_pos[1]) - ord("1")]
                    if self.board[ next_pos_user_tmp[1]][next_pos_user_tmp[0]] != self.BoardElem.EMPTY:
                        print("Position is already occupied!")
                        continue                     

                    next_pos = next_pos_user_tmp
             
            # Set player's choice
            self.board[ next_pos[1] ][ next_pos[0] ] = curr_player

            # Who's next?
            curr_player = self.BoardElem.X if curr_player == self.BoardElem.O else self.BoardElem.O






# Start application
if __name__ == '__main__':
    game = TicTacToe()
    game.run(ai_active = True)
