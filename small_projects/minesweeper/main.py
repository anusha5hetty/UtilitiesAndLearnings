from tkinter import *
from cell import Cell
from config import *

# CReated with the help of https://www.freecodecamp.org/news/object-oriented-programming-with-python-code-a-minesweeper-game/


def h_pcnt(percent):
    return (HEIGHT/100)*percent

def w_pcnt(percent):
    return (WIDTH/100)*percent

root = Tk()
root.title("Minesweeper")
root.configure(bg="black")
root.geometry(f'{WIDTH}x{HEIGHT}')
root.resizable(False, False)

top_frame = Frame(root, bg='black', width=WIDTH, height=h_pcnt(25))
top_frame.place(x=0, y=0)

left_frame = Frame(root, bg='black', width=w_pcnt(25), height=h_pcnt(75))
left_frame.place(x=0, y=h_pcnt(25))

centre_frame = Frame(root, bg='black', width=w_pcnt(75), height=h_pcnt(75))
centre_frame.place(x=w_pcnt(25), y=h_pcnt(25))

game_title = Label(top_frame, bg='black', fg='White', text='Minesweeper Game', font=("", 48))
game_title.place(x=w_pcnt(25), y=5)

for row_idx in range(GRID_SIZE):
    for col_idx in range(GRID_SIZE):
        c1 = Cell(row_idx, col_idx)
        cell_btn_obj = c1.create_btn_obj(centre_frame)
        cell_btn_obj.grid(column=col_idx, row=row_idx)
        
print(Cell.all_cells)
Cell.randomize_mines(NUM_MINES)

Cell.create_label_obj(left_frame)
Cell.cell_count_lbl_obj.place( x=0, y=0)

root.mainloop()
