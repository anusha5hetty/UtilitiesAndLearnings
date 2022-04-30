from tkinter import *
from cell import Cell
from config import *

# STOPPED DEVELOPING AT 
# Stopped the video at 


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

# c1 = Cell()
# cell_btn_obj = c1.create_btn_obj(centre_frame)
# cell_btn_obj.grid(column=0, row=0)



for row_idx in range(GRID_SIZE):
    for col_idx in range(GRID_SIZE):
        c1 = Cell(row_idx, col_idx)
        cell_btn_obj = c1.create_btn_obj(centre_frame)
        cell_btn_obj.grid(column=col_idx, row=row_idx)
        
print(Cell.all_cells)
Cell.randomize_mines(NUM_MINES)

root.mainloop()
