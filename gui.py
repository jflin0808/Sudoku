import pygame, time, sys
from settings import *
from solver import *

class Grid:
    
    def __init__(self, window):
        self.window = window
        self.input = input
        self.board = board
        self.row = row
        self.col = col
        self.cells = [[Cell(self.board[x][y]) for y in range(col)] for x in range(row)]
        self.layout = None
        self.selected = None

    def update_grid(self):
        self.layout = [[self.cells[x][y].num for y in range(self.col)] for x in range(self.row)]

    def draw_grid(self, window):
        self.window.fill(WHITE)
        pygame.draw.rect(window, BLACK, (marginSize[0], marginSize[1], width-150, height-350), thick)
        
        for i in range(self.row):
            pygame.draw.line(window, BLACK, (i*cellSize + marginSize[0], 100), (i*cellSize + marginSize[0], 550), thick if i % 3 == 0 else 1)
            pygame.draw.line(window, BLACK, (75, i*cellSize + marginSize[1]), (525, i*cellSize + marginSize[1]), thick if i % 3 == 0 else 1)
        
        for x in range(self.row):
            for y in range(self.col):
                self.cells[x][y].fill_cells(window)

    
    def mouse_on_board(self, mousePos):
        # Compares mouse position to top and left border
        if mousePos[1] < marginSize[1] or mousePos[0] < marginSize[0]:
            return False
        # Compares mouse position to bottom and right border
        if mousePos[1] > marginSize[1]+boardSize or mousePos[0] > marginSize[0]+boardSize:
            return False
        # Returns the selected cell within the Sudoku board
        return ((mousePos[1]-marginSize[1]) // 50, (mousePos[0]-marginSize[0]) // 50)

    def triggered(self, selectedCells):
        self.cells[row][col].selected = selectedCells


class Cell:

    def __init__(self, num):
        self.num = num
        self.temp = 0
        self.row = row
        self.col = col
        self.selected = None
        
    def fill_cells(self, window):
        # numFont = pygame.font.SysFont("frenchscript", cellSize)
        # if self.temp !=0 and self.num == 0:
        #     text = numFont.render(str(self.temp), 1, GRAY)
        #     window.blit(text, (self.row*cellSize + marginSize[0], self.col*cellSize + marginSize[1]))
        # elif not self.num == 0:
        #     text = numFont.render(str(self.num),1, BLACK)
        #     numWidth = numFont.get_width()
        #     numHeight = numFont.get_height()
        #     self.row += (cellSize-numWidth) // 2
        #     self.col += (cellSize-numHeight) // 2
        #     window.blit(text, (self.row, self.col))

        if self.selected:
            self.highlight_selected_cells(window, selectedCells)

    def highlight_selected_cells(self, window, cell):
        pygame.draw.rect(window, LIGHTPINK, (cell[1]*cellSize + marginSize[0], cell[0]*cellSize + marginSize[1], cellSize, cellSize))  
    
    def highlight_locked_cells(self, window, lockedCell):
        for cell in lockedCell:
            pygame.draw.rect(window, LIGHTPURPLE, (cell[0]*cellSize + marginSize[0], cell[1]*cellSize + marginSize[1], cellSize, cellSize))

    def setNum(self, num):
        self.num = num

    def setTemp(self, num):
        self.temp = num

if __name__ == "__main__":
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Sudoku")
    board1 = Grid(window)
    input = None
    running = True
    pos = []
    timer = time.time()

    while running:  
        play_time = round(time.time() - timer)

        for event in pygame.event.get():
            # Closes window
            if event.type == pygame.QUIT:
                running = False
        
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                selectedCells = board1.mouse_on_board(mousePos)
                if selectedCells:
                    print(selectedCells)
                    board1.triggered(selectedCells)

        board1.draw_grid(window)
        pygame.display.update()
