import tkinter as tk
import random

h = 5
w = 5

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

root = tk.Tk()
root.geometry("500x500")

frame = tk.Frame(root)

tk.Grid.rowconfigure(root, 0, weight=1)
tk.Grid.columnconfigure(root, 0, weight=1)

frame.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)

grid = tk.Frame(frame)

grid.grid(sticky=tk.N+tk.S+tk.E+tk.W, column=0, row=7, columnspan=2)

tk.Grid.rowconfigure(frame, 7, weight=1)
tk.Grid.columnconfigure(frame, 0, weight=1)

not_clicked="black"
active="red"
default_color="white"


def main(list_of_board, board_object):
    width = len(list_of_board)
    height = len(list_of_board[0])
    
    for x in range(height):
        for y in range(width):
            btn = tk.Button(frame, bg=not_clicked)
            btn.grid(column=y, row=x, sticky=tk.N+tk.S+tk.E+tk.W)
            btn["text"] = list_of_board[x][y]
            btn["command"] = lambda btn=btn, x=x, y=y: click(btn, x, y, board_object)
            
    for x in range(width):
        tk.Grid.columnconfigure(frame, x, weight=1)
        
    for y in range(height):
        tk.Grid.rowconfigure(frame, y, weight=1)
        
    return frame

  for x in range(width):
    Grid.columnconfigure(frame, x, weight=1)

  for y in range(height):
    Grid.rowconfigure(frame, y, weight=1)

  return frame

def click(clicked_button, x, y, board_object):
    s = board_object.dig(x, y)
    if s:
        if(clicked_button["bg"] == 'black'):
            clicked_button["bg"] = default_color
    else:
        clicked_button["bg"] = active
        #root.destroy()



if __name__ == '__main__':
    board = Board(h, w)
    main(board.board, board)
    tk.mainloop()

