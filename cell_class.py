import pygame
from settings import *

class Cell:

    def __init__(self, num, col):
        self.num = num
        self.temp = 0
        self.row = row
        self.col = col
        self.selected = False
        
    def fill_cells(self, window):
        numFont = pygame.font.SysFont("frenchscript", cellSize)
        if self.temp !=0 and self.num == 0:
            text = numFont.render(str(self.temp), 1, GRAY)
            window.blit(text, (self.row*cellSize + marginSize[0], self.col*cellSize + marginSize[1]))
        elif not self.num == 0:
            text = numFont.render(str(self.num),1, BLACK)
            numWidth = numFont.get_width()
            numHeight = numFont.get_height()
            self.row += (cellSize-numWidth) // 2
            self.col += (cellSize-numHeight) // 2
            window.blit(text, (self.row, self.col))

    def highlight_selected_cells(self, window, cell):
        pygame.draw.rect(window, LIGHTPINK, (cell[1]*cellSize + marginSize[0], cell[0]*cellSize + marginSize[1], cellSize, cellSize))  
    
    def highlight_locked_cells(self, window, lockedCell):
        for cell in lockedCell:
            pygame.draw.rect(window, LIGHTPURPLE, (cell[0]*cellSize + marginSize[0], cell[1]*cellSize + marginSize[1], cellSize, cellSize))

    def setNum(self, num):
        self.num = num

    def setTemp(self, num):
        self.temp = num