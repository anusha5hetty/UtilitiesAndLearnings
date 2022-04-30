from tkinter import Button

import random

from config import *

class Cell:
    all_cells = []
    def __init__(self, row, column, is_mine=False) -> None:
        self.is_mine = is_mine
        self.cell_btn_obj = None
        self.row = row
        self.column = column
        Cell.all_cells.append(self)
        
    def show_mine(self):
        self.cell_btn_obj.configure(bg='red')            

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
    def mine_cells(self):
        mine_cells = [cell for cell in self.surrounded_cells if cell.is_mine]
        return mine_cells
        
    def show_cell(self):        
        print(f"CELL CLICKED: Cell({self.row},{self.column})")
        print("SURROUNDED CELL 2", self.surrounded_cells)
        self.cell_btn_obj.configure(text=len(self.mine_cells))
        
    def left_func(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            self.show_cell()       
            
    def right_func(self, event):
        print("well it prints!! Great!!")
    
    def create_btn_obj(self, location):
        
            
        btn = Button(location, width=12, height=4)
        # btn = Button(location, text=f"{self.row},{self.column}", width=12, height=4)
        
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