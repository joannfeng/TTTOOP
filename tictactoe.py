# tictactoe.py

import os
import sys

###


class Symbol:

    def __init__(self, identity, position):
        self.identity = identity
        self.position = position

    def get_position(self):
        return self.position

    def get_identity(self):
        return self.identity

###


class Player:

    def __init__(self, name, symbol):
        self.pieces = []
        self.name = name
        self.symbol = symbol

    def add_pieces(self, *symbols):
        for symbol in symbols:
            self.pieces.append(symbol)

    def get_name(self):
        return self.name

    def get_symbol(self):
        return self.symbol
    
    def get_pieces(self):
        return self.pieces
###


class Display:

    def __init__(self):
        self.board = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]

    def draw(self, symbol):
        # get symbol's position ex. (0,0) or (2,2)
        pos = symbol.get_position()
        # check to see if position is on board, if not return error
        if isinstance(pos, list) and len(pos) == 2:
            if pos[0] >= 0 and pos[0] <= 2 and pos[1] >= 0 and pos[1] <= 2:
                # based on position, write to board
                if self.board[pos[0]][pos[1]] == " ":
                    self.board[pos[0]][pos[1]] = symbol.get_identity()
                    return ""
                else:
                    return "This spot is taken.\n"
            else:
                return "This spot does not exist on the board.\n"
        else:
            return "Something happened. Internal Error.\n"

    def __str__(self):
        string = ''
        string += " .---.---.---.\n"
        for row in self.board:
            for item in row:
                string += " | " + item
            string += " |\n"
            string += " .---.---.---.\n"
        return string


class TicTacToe:

    def __init__(self):
        self.game_display = Display()
        # ask players for names and symbols

        name1 = input("Enter Player 1 name: ")
        symbol1 = input("Enter symbol for Player 1: ")
        while len(symbol1) != 1:
            symbol1 = input("Symbol must be a single character.\nEnter symbol for Player 1: ")
        print()
        
        name2 = input("Enter Player 2 name: ")
        symbol2 = input("Enter symbol for Player 2: ")
        while len(symbol2) != 1:
            symbol2 = input("Symbol must be a single character.\nEnter symbol for Player 2: ")
        while symbol1 == symbol2:
            symbol2 = input("Symbol already used. Enter symbol for Player 2: ")
        print()

        self.player_one = Player(name1, symbol1)
        self.player_two = Player(name2, symbol2)

    def run(self):

        print(self.game_display) # draw board

        while(1):

            for player in [self.player_one, self.player_two]:
                
                # ask for position
                while(1):
                    x_pos = int(input("Enter row: \n"))
                    y_pos = int(input("Enter column: \n"))

                    # draw board
                    symbol = Symbol(player.get_symbol(), [x_pos,y_pos])
                    player.add_pieces(symbol)
                    error = self.game_display.draw(symbol)

                    if error == "":
                        break
                    else:
                        print(error)
                    
                print(self.game_display)

                # check for win
            
                if self._check_for_win(player):
                    print(player.get_name() + " won!\n")
                    return


    def _check_for_win(self, player):
        
        # rows
        count_0 = 0
        count_1 = 0
        count_2 = 0
        for piece in player.get_pieces():
            if piece.get_position()[0] == 0:
                count_0 += 1
            if piece.get_position()[0] == 1:
                count_1 += 1
            if piece.get_position()[0] == 2:
                count_2 += 1
        if count_0 >= 3 or count_1 >= 3 or count_2 >= 3:
            return True

        # columns
        count_0 = 0
        count_1 = 0
        count_2 = 0
        for piece in player.get_pieces():
            if piece.get_position()[1] == 0:
                count_0 += 1
            if piece.get_position()[1] == 1:
                count_1 += 1
            if piece.get_position()[1] == 2:
                count_2 += 1
        if count_0 >= 3 or count_1 >= 3 or count_2 >= 3:
            return True

        # case 1
        diag_count = 0
        for piece in player.get_pieces():
            if piece in [[0,0],[1,1],[2,2]]:
                diag_count += 1
        if diag_count >= 3:
            return True
        
        # case 2
        diag_count = 0
        for piece in player.get_pieces():
            if piece in [[2,0],[1,1],[0,2]]:
                diag_count += 1
        if diag_count >= 3:
            return True
        
        return False
        
TicTacToe().run()

# i love uT
# 1-3 based indexing
# draw case
