#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""The old  game classic "TicTacToe" in Python

    @todo: Add minimax

"""

class TicTacToe:


    board = []

    player_label = ["X", "O"]

    def _init(self):
        self.board = [[" ", " ", " "],
                      [" ", " ", " "],
                      [" ", " ", " "]]

    def _show_board(cls, board):
        print() 
        print("      A     B     C\n")

        for idx, row in enumerate(board):
            print(" " + str(idx + 1) + "    " + '  |  '.join(str(x) for x in row))
            if idx != len(board) - 1: print("    -----------------")
        print() 
        print() 

    def _are_three_equal(cls, a, b, c):
        return a == b and b == c and c != " "

    def _get_winner(cls, board):
        won_player = -1

        # Check rows and columns
        for x in range(len(board)):
            # Check columns
            if(cls._are_three_equal(board[0][x], board[1][x], board[2][x])):
                won_player = board[0][x]
                break

            # Check row
            if(cls._are_three_equal(board[x][0], board[x][1], board[x][2])):
                won_player = board[x][0]
                break

        # Check diagonals if no winner found
        if won_player == -1 and cls._are_three_equal(board[0][0], board[1][1], board[2][2]):
            won_player = board[0][0]
        if won_player == -1 and cls._are_three_equal(board[0][2], board[1][1], board[2][0]):
            won_player = board[0][2]       

        return won_player

    def run(self):
        self._init()

        next_player = 0

        print()
        print("############ TicTacToe ############")
        print()

        # Game loop
        run_game = True
        while(run_game):
            self._show_board(self.board)


            # Some won the game?
            tmp_winner = self._get_winner(self.board)
            if tmp_winner != -1:
                print()
                print(tmp_winner + " won the game!")
                print()
                run_game = False
                break
            elif sum( x.count(" ") for x in self.board) == 0:
                print()
                print("Tie!")
                print()
                run_game = False
                break
        
            # Get input until it's valid
            next_pos_user = []
            while(next_pos_user == []):

                input_pos = input("It's " + self.player_label[next_player] + "'s turn. Please select your next position (e.g. A2): ")     
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
                if self.board[ next_pos_user_tmp[1]][next_pos_user_tmp[0]] != " ":
                    print("Position is already occupied!")
                    continue                     

                next_pos_user = next_pos_user_tmp
             
            # Set player's choice
            self.board[ next_pos_user_tmp[1]][next_pos_user_tmp[0]] = self.player_label[next_player]

            # Who's next?
            next_player = ( next_player + 1 ) % 2





# Start application
if __name__ == '__main__':
    game = TicTacToe()
    game.run()
