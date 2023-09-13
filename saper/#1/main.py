import random
import re


class Board:
    def __init__(self, dim_size, num_bombs):
        
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        self.board = self.make_new_board()
        self.assign_values_to_board()

        # keep track of which locations we've uncovered
        self.dug = set() # if we dig at 0, 0, then self.dug = {(0,0)}


    # plant the bombs
    def make_new_board(self):

        # generate a new board
        # [[None, None, ..., None],
        #  [None, None, ..., None],
        #  [...                  ],
        #  [None, None, ..., None]]
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]

        # plant the bombs
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            # choose random location for our bombs
            loc = random.randint(0, self.dim_size**2 - 1)
            row = loc // self.dim_size
            col = loc % self.dim_size

            if board[row][col] == '*':
                # actually there was a bomb planted before, so keep going
                continue

            # plant the bomb
            board[row][col] = '*'
            bombs_planted += 1

        return board


    def assign_values_to_board(self):
        # put 1's and 2's and everything in aour board to show how many bombs are around
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                # if this is already a bomb, we do nothing
                if self.board[r][c] == '*':
                    continue
                self.board[r][c] = self.get_num_neighboring_bombs(r, c)


    def get_num_neighboring_bombs(self, row, col):
        num_neighboring_bombs = 0

        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                # don't check for original location
                if r == row and c == col:
                    continue
                if self.board[r][c] == '*':
                    num_neighboring_bombs += 1

        return num_neighboring_bombs

    def dig(self, row, col):
        # scenarios:
        # hit a bomb -> game over
        # dig at location with neighboring bombs -> finish dig
        # dig at location with no neighboring bombs -> recursively dig neighbors!

        # keeping track of where we dug
        self.dug.add((row, col))

        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True

        # else: self.board[row][col] == 0
        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                # we did dig here already
                if (r, c) in self.dug:
                    continue 
                self.dig(r, c)

        return True

    def __str__(self):
        # this helps us to represent currnet situation in game

        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]

        for row in range(self.dim_size):
            for col in range(self.dim_size):
                # if we did dig here show whats on original board, if not show space to tell user that he can dig this place
                if (row,col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '
        
        # put this into a string
        string_rep = ''
        # get max column widths for printing
        widths = []
        for i in range(self.dim_size):
            columns = map(lambda x: x[i], visible_board)
            widths.append(len(max(columns, key = len)))

        indices = [i for i in range(self.dim_size)]
        indices_row = '   '
        cells = []
        for i, col in enumerate(indices):
            format = '%-' + str(widths[i]) + "s"
            cells.append(format % (col))
        indices_row += '  '.join(cells)
        indices_row += '  \n'
        
        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for j, col in enumerate(row):
                format = '%-' + str(widths[j]) + "s"
                cells.append(format % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.dim_size)
        string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len

        return string_rep

# play the game
def play(dim_size=10, num_bombs=10):
    
    board = Board(dim_size, num_bombs)
    print(board.board)

    safe = True 

    while len(board.dug) < board.dim_size ** 2 - num_bombs:
        print(board)
        user_input = re.split(',(\\s)*', input("Where would you like to dig? Input as row,col: "))  # '0, 3'
        row, col = int(user_input[0]), int(user_input[-1])
        if row < 0 or row >= board.dim_size or col < 0 or col >= dim_size:
            print("Invalid location. Out of bounds. Try again.")
            continue

        safe = board.dig(row, col)
        # not safe so You dug a bomb
        if not safe:
            break

    if safe:
        print("Congratulations! YOU WENT THROUGH IT!")
    else:
        print("THATS GAME OVER :( SORRY")
        board.dug = [(r,c) for r in range(board.dim_size) for c in range(board.dim_size)]
        print(board)

if __name__ == '__main__':
    play()