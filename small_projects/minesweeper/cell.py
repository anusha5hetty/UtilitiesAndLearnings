from tkinter import Button, Label, PhotoImage
import random
import sys
import ctypes
from config import *

class Cell:
    all_cells = []
    remaining_cells = NUM_CELLS
    cell_count_lbl_obj = None
    def __init__(self, row, column, is_mine=False) -> None:
        self.is_mine = is_mine
        self.is_mine_candidate = False
        self.cell_btn_obj = None
        self.row = row
        self.column = column
        self.is_open = False
        Cell.all_cells.append(self)   

    @property
    def surrounded_cells(self):
        cells = []
        # mine_cells = []
        row_start_idx = self.row-1
        column_start_idx = self.column-1
        for idx_row in range(3):
            row = row_start_idx + idx_row
            for idx_col in range(3):
                column = column_start_idx + idx_col
                if (row not in (-1, GRID_SIZE) and column not in (-1, GRID_SIZE)):
                    cell = self.get_cell_by_axis(row, column)
                    cells.append(cell)
        return cells
        
    @property
    def mine_cells_count(self):
        mine_cells = [cell for cell in self.surrounded_cells if cell.is_mine]
        return len(mine_cells)
    
    def show_mine(self):
        self.cell_btn_obj.configure(bg='red')
        ctypes.windll.user32.MessageBoxW(0, 'You stepped on a mine!!', 'Ahhhhhhh', 0)
        sys.exit()
        
    def show_cell(self):   
        print(f"CELL CLICKED: Cell({self.row},{self.column})")
        print("SURROUNDED CELL 2", self.surrounded_cells)
        self.cell_btn_obj.configure(text=self.mine_cells_count)
        
        if self.is_mine_candidate:
            self.cell_btn_obj.configure(bg='SystemButtonFace')
        
        if not self.is_open:
            self._cell_open()
            
        if Cell.remaining_cells == 0:
            ctypes.windll.user32.MessageBoxW(0, "Congratulations!! You are not dumb afterall!!", "Big Woop!!", 0)
            
    def _cell_open(self):
        self.is_open = True
        Cell.remaining_cells -= 1
        Cell.cell_count_lbl_obj.configure(text=f'Remaining Cells {Cell.remaining_cells}')
        
    def _cell_close(self):
        self.is_open = False
        Cell.remaining_cells += 1
        Cell.cell_count_lbl_obj.configure(text=f'Remaining Cells {Cell.remaining_cells}')
        
    def left_func(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            self.show_cell()
            if self.mine_cells_count == 0:
                list(map(lambda cell: cell.show_cell(), self.surrounded_cells))

        self.cell_btn_obj.unbind('<Button-1>')
        self.cell_btn_obj.unbind('<Button-3>')
                
    def right_func(self, event):
        if not self.is_mine_candidate:
            self.is_mine_candidate = True
            self.cell_btn_obj.configure(bg='orange')
            self._cell_open()
        else:
            self.is_mine_candidate = False
            self.cell_btn_obj.configure(bg='SystemButtonFace')
            self._cell_close()
    
    @staticmethod
    def create_label_obj(location):
        lbl = Label(location, text=f'Remaining Cells {Cell.remaining_cells}', fg='White', bg='Black', font=("", 30))
        Cell.cell_count_lbl_obj = lbl
        return lbl
            
    def create_btn_obj(self, location):
        # photo = PhotoImage(file = "C:/Users/ashetty/Documents/Personal_Git/UtilitiesAndLearnings/small_projects/minesweeper/mine.png")
            
        btn = Button(location, width=12, height=4)
        # btn = Button(location, width=12, height=4, image=photo)
        
        # <Button-1> is convension for Left click
        btn.bind('<Button-1>', self.left_func)
        
        # # <Button-3> is convension for right click
        btn.bind('<Button-3>', self.right_func)
        self.cell_btn_obj = btn
        return self.cell_btn_obj

    def get_cell_by_axis(self, row, column):
        for cell in Cell.all_cells:
            if cell.row == row and cell.column == column:
                return cell
    
    def __repr__(self):
        return f'Cell({self.row},{self.column})'
    
    @staticmethod
    def randomize_mines(num_mines):
        mine_cells = random.sample(Cell.all_cells, num_mines)
        for mine_cell in mine_cells:
            mine_cell.is_mine = True