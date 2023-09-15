from tkinter import *
import tkinter
import random

#####################################################################################################################################################################################################################################################
# variables
h = 10
nr_bombs = 7
not_clicked="black"
active="red"
default_color="white"
#####################################################################################################################################################################################################################################################

#####################################################################################################################################################################################################################################################
# define Board objects class
class Board:
    def __init__(self, dim_size, num_bombs):
        
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        self.board = self.make_new_board()
        self.assign_values_to_board()
        self.dug = set() 


    def make_new_board(self):
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]

        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 - 1)
            row = loc // self.dim_size
            col = loc % self.dim_size

            if board[row][col] == '*':
                continue

            board[row][col] = '*'
            bombs_planted += 1

        return board


    def assign_values_to_board(self):
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
        self.dug.add((row, col))

        but = buttons[f'btn ({row},{col})']

        if self.board[row][col] == '*':
            but["bg"] = active
            #root.destroy()
            return False
        elif self.board[row][col] > 0:
            but["bg"] = default_color
            return True

        # else: self.board[row][col] == 0
        but["bg"] = default_color
        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                # we did dig here already
                if (r, c) in self.dug:
                    continue
                buttons[f'btn ({r},{c})']["bg"] = default_color
                self.dig(r, c)

        return True
#####################################################################################################################################################################################################################################################


#####################################################################################################################################################################################################################################################
# make window
root = Tk()
root.geometry("500x500")

frame=Frame(root)

Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)

frame.grid(row=0, column=0, sticky=N+S+E+W)

grid=Frame(frame)

grid.grid(sticky=N+S+E+W, column=0, row=7, columnspan=2)

Grid.rowconfigure(frame, 7, weight=1)
Grid.columnconfigure(frame, 0, weight=1)
#####################################################################################################################################################################################################################################################




#####################################################################################################################################################################################################################################################
def main(buttons, b, bb):
    width = len(b)
    height = len(b[0])
    for x in range(height):
        for y in range(width):
            btn = tkinter.Button(frame, bg=not_clicked)
            btn.grid(column=y, row=x, sticky=N+S+E+W)
            btn["text"] = b[x][y]
            btn["command"] = lambda x=x, y=y: bb.dig(x, y)

            buttons[f'btn ({x},{y})'] = btn

    for x in range(width):
        Grid.columnconfigure(frame, x, weight=1)

    for y in range(height):
        Grid.rowconfigure(frame, y, weight=1)

    return frame


buttons = {}
if __name__ == '__main__':
    board = Board(h, nr_bombs)
    print(board.board)
    main(buttons, board.board, board)
    tkinter.mainloop()
