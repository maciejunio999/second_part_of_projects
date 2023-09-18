from tkinter import *
import tkinter
import random

#####################################################################################################################################################################################################################################################
# variables
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

    def dig(self, row, col, roo):
        self.dug.add((row, col))

        but = buttons[f'btn ({row},{col})']

        if self.board[row][col] == '*':
            but["bg"] = active
            roo.destroy()
            return False
        elif self.board[row][col] > 0:
            self.loose = ''
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
                self.dig(r, c, roo)

        return True
#####################################################################################################################################################################################################################################################


#####################################################################################################################################################################################################################################################
# make a window to play
def main(buttons, b, bb):

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

    width = len(b)
    height = len(b[0])
    for x in range(height):
        for y in range(width):
            btn = tkinter.Button(frame, bg=not_clicked)
            btn.grid(column=y, row=x, sticky=N+S+E+W)
            btn["text"] = b[x][y]
            btn["command"] = lambda x=x, y=y: bb.dig(x, y, root)

            buttons[f'btn ({x},{y})'] = btn

    for x in range(width):
        Grid.columnconfigure(frame, x, weight=1)

    for y in range(height):
        Grid.rowconfigure(frame, y, weight=1)

    return frame

#####################################################################################################################################################################################################################################################
# make menu window
def menu():
    root = Tk()
    root.title("Saper") # window title
    root.geometry('500x250') # windows size

    header = Label(root, text='Minesweeper', font='45')
    header.pack()
    
    upper_frame = Frame(root)
    upper_frame.pack()

    mid_frame = Frame(root)
    mid_frame.pack()

    down_frame = Frame(root)
    down_frame.pack()

    label_for_board_size = Label(upper_frame, text="Choose size of Your board")
    label_for_board_size.pack(side=LEFT)

    BOARDS_SIZES = [i for i in range(2, 10)]
    board_size_var = StringVar(root)
    board_size_var.set(BOARDS_SIZES[0])
    board_size_menu = OptionMenu(upper_frame, board_size_var, *BOARDS_SIZES)
    board_size_menu.pack(side=LEFT)

    label_for_number_of_bombs = Label(mid_frame, text="Choose of bombs for this board")
    label_for_number_of_bombs.pack(side=LEFT)

    NUMBERS_FOR_BOMBS = [1, 2, 3, 5, 7, 8, 9, 10, 15, 20, 25, 30, 35, 40, 50, 60, 70, 80, 85, 90, 99]
    number_of_bombs_var = StringVar(root)
    number_of_bombs_var.set(NUMBERS_FOR_BOMBS[0])
    number_of_bombs_menu = OptionMenu(mid_frame, number_of_bombs_var, *NUMBERS_FOR_BOMBS)
    number_of_bombs_menu.pack(side=LEFT)
    
    def submit_func():
        board = Board(int(board_size_var.get()), int(number_of_bombs_var.get()))
        main(buttons, board.board, board)

    submit_button = Button(down_frame, text='Submit', command=submit_func)
    submit_button.pack()

#####################################################################################################################################################################################################################################################


buttons = {}
if __name__ == '__main__':
    menu()
    tkinter.mainloop()
