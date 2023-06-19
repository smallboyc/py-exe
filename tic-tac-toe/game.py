import time
from player import HumanPlayer, RandomComputerPlayer

class TicTacToe:
    def __init__(self):
        self.board = [' ' for i in range(9)]
        self.current_winner = None
    
    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")
    
    @staticmethod
    def print_board_nums():
        number_board = [str(i) for i in range(9)]
        for row in [number_board[i*3:(i+1)*3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")

    def empty_squares(self):
        return ' ' in self.board
    
    def num_of_empty_squares(self):
       return self.board.count(' ')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
    
    def make_move(self,square,letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square,letter):
                self.current_winner = True
            return True
        return False
    
    def winner(self,square,letter):
        #rows
        row_index = square // 3
        row = self.board[row_index * 3:(row_index+1)*3]
        if all([spot == letter for spot in row]):
            return True
        #cols
        col_index = square % 3
        col = [self.board[col_index + i*3] for i in range(3)]
        if all([spot == letter for spot in col]):
            return True
        #diags
        diag_index = square % 2
        if diag_index == 0:
            diag_one = [self.board[diag_index + i*4] for i in range(3)]#\
            if all([spot == letter for spot in diag_one]):
                return True
            diag_two = [self.board[diag_index + i*2] for i in range(1,4)]#/
            if all([spot == letter for spot in diag_two]):
                return True
        return False

    
def play(game, x_player, o_player):

    game.print_board_nums()

    letter = 'X'

    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else :
            square = x_player.get_move(game)
    
        if(game.make_move(square,letter)):
                print(f"{letter} makes a move to square {square}")
                game.print_board()
                print('')
        
        if game.current_winner:
            print(f"{letter} wins !")
            return letter
    
        letter = 'X' if letter == 'O' else 'O'
        time.sleep(0.8)
    
    print("It's a tie !")

if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    game = TicTacToe()
    play(game, x_player, o_player)