import pygame, sys, time
from settings import *
from button_class import *

class Gui:
    # Initialization Function
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((width, height))
        self.running = True
        self.board = board
        self.solvedBoard = []
        self.clicking = False
        self.right_clicking = False
        self.temp = 0
        self.selectedCells = []
        self.tempCells = []
        self.lockedCells = []
        self.mousePos = []
        self.completed = False
        self.cellFlag = False
        self.state = "in_game"
        self.menu_buttons = []
        self.in_game_buttons = []
        self.end_buttons = []
        self.font = pygame.font.SysFont("frenchscript", cellSize + 10)
        self.smallFont = pygame.font.SysFont("frenchscript", 30)
        self.load()


    def run(self):
        while self.running:
            if self.state == "in_game":
                self.in_game_events()
                self.in_game_update()
                self.in_game_display()
        pygame.quit()
        sys.exit()
        

########## In-Game Functions ##########


    def in_game_events(self):

        tempCells = []
        if self.clicking and self.mouse_position() not in self.selectedCells and self.mouse_position() not in self.lockedCells:
            self.selectedCells.append(self.mouse_position())

        if self.right_clicking == True:
            self.selectedCells.clear()
            self.right_clicking = False
        
        for event in pygame.event.get():
            # Closes window
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.clicking = True
                if event.button == 3:
                    self.right_clicking = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.clicking = False
                
            # Key press event
            if event.type == pygame.KEYDOWN:
                # 1 key
                
                if event.key == pygame.K_1:
                    if self.selectedCells and self.selectedCells not in self.lockedCells:
                        self.temp = 1
                        print(tempCells)
                # 2 key
                if event.key == pygame.K_2:
                    if self.selectedCells and self.selectedCells not in self.lockedCells:
                        self.temp = 2
                # 3 key
                if event.key == pygame.K_3:
                    if self.selectedCells and self.selectedCells not in self.lockedCells:
                        self.temp = 3
                # 4 key
                if event.key == pygame.K_4:
                    if self.selectedCells and self.selectedCells not in self.lockedCells:
                        self.temp = 4
                # 5 key
                if event.key == pygame.K_5:
                    if self.selectedCells and self.selectedCells not in self.lockedCells:
                        self.temp = 5
                # 6 key
                if event.key == pygame.K_6:
                    if self.selectedCells and self.selectedCells not in self.lockedCells:
                        self.temp = 6
                # 7 key
                if event.key == pygame.K_7:
                    if self.selectedCells and self.selectedCells not in self.lockedCells:
                        self.temp = 7
                # 8 key
                if event.key == pygame.K_8:
                    if self.selectedCells and self.selectedCells not in self.lockedCells:
                        self.temp = 8
                # 9 key
                if event.key == pygame.K_9:
                    if self.selectedCells and self.selectedCells not in self.lockedCells:
                        self.temp = 9
                # Delete key
                if event.key == pygame.K_DELETE:
                    if self.selectedCells and self.selectedCells not in self.lockedCells:
                        self.temp = 0
                # Return key
                if event.key == pygame.K_RETURN:
                    self.solve(board)


    def in_game_update(self):
        # Updates whenever there is mouse movement
        self.mousePos = pygame.mouse.get_pos()

        # Updates button object with mouse position
        for button in self.in_game_buttons:
            button.update(self.mousePos)

    def in_game_display(self):
        # Fill background colour
        self.window.fill(WHITE)

        # Calls function to draw button in window
        for button in self.in_game_buttons:
            button.draw(self.window)

        # Calls function to highlight locked cells
        self.highlight_locked_cells(self.window, self.lockedCells)

        # Calls function to highlight selected cells whenever theres a change to selected cells
        if self.selectedCells:
            self.highlight_selected_cells(self.window, self.selectedCells)

        if self.temp != 0:
            self.pencil_in(self.window, str(self.temp))

        # Calls function to draw sudoku board
        self.draw_board(self.window)

        # Calls function to draw numbers on Sudoku board
        self.num_layout(self.window)

        # Reset the cell triggered flag
        self.cellFlag = False

        # Updates display
        pygame.display.update()


########### Task Functions ##########

    # Draws complete Sudoku board
    def draw_board(self, window):
        # Create square sudoku board
        pygame.draw.rect(window, BLACK, (marginSize[0], marginSize[1], width-150, height-350), thick)
        # Draw lines to separate board into quadrants and cells
        for i in range(9):
            pygame.draw.line(window, BLACK, (i*cellSize + marginSize[0], 100), (i*cellSize + marginSize[0], 550), thick if i % 3 == 0 else 1)
            pygame.draw.line(window, BLACK, (75, i*cellSize + marginSize[1]), (525, i*cellSize + marginSize[1]), thick if i % 3 == 0 else 1)

    # Converts number list into board positions
    def num_layout(self, window):
            for y, row in enumerate(board):
                for x, num in enumerate(row):
                    if num != 0:
                        pos = [x * cellSize + marginSize[0], y * cellSize + marginSize[1]]
                        self.lock_in(window, str(num), pos)

    # Places numbers onto game board
    def lock_in(self, window, num, pos, colour = BLACK):
        font = self.font.render(num, True, colour)
        numWidth = font.get_width()
        numHeight = font.get_height()
        pos[0] += (cellSize-numWidth) // 2
        pos[1] += (cellSize-numHeight) // 2
        window.blit(font, pos)

    def pencil_in(self, window, tempNum, colour = GRAY):
        font = self.smallFont.render(tempNum, True, GRAY)
        numWidth = font.get_width()
        numHeight = font.get_height()
        for cells in self.selectedCells:
            pos = (cells[1] * cellSize + marginSize[0] + 2, cells[0] * cellSize + marginSize[1] - 8)
            window.blit(font, pos)

    def solve(self, board):
        print(board)
        empty = self.empty_pos(board)
        # Base case: Full board
        if not empty:
            return True
        # Sets row, col to empty row and column position given by empty_pos
        else: row, col = empty
        # Iterate from 0-9, sending paramaters to the is_valid function
        for i in range(1, 10):
            if self.is_valid(board, i, (row, col)):
                board[row][col] = i
                # If board is solved at any iteration, return True
                if self.solve(board):
                    return True
                # Backtrack by setting the previous position back to an empty slot (0)
                board[row][col] = 0  
        # Returns False if board is unsolvable
        return False              

    # Check if number at [y,x] is a valid possibility
    # board = board array, num = attempted number, pos = current row and column 
    def is_valid(self, board, num, pos):    
        # Check row
        for i in range(len(board[0])):
            if board[pos[0]][i]  == num and pos[1] != i:
                return False

        # Check col
        for i in range(len(board)):
            if board[i][pos[1]]  == num and pos[0] != i:
                return False

        # Check quadrants([0,0], [0,1], [0,2], [1,0], [1,1], [1,2], [2,1], [2,2], [2,3])
        row_pos = pos[1] // 3
        col_pos = pos[0] // 3

        for i in range(col_pos*3, col_pos*3 + 3): # from quadrant [x,0] -> [x,2]
            for j in range(row_pos*3, row_pos*3 + 3): # from quadrant [0,x] -> [2,x]
                if board[i][j] == num and (i,j) != pos:
                    return False
        return True

    def empty_pos(self, board):
        for i in range(len(board)): # num of rows
            for j in range(len(board[0])): # num of cols
                if board[i][j] == 0: # check if empty
                    return (i, j) # row, col
        return None # completed board

    # Highlights locked cells on board
    def highlight_locked_cells(self, window, lockedCells):
        for cell in lockedCells:
            pygame.draw.rect(window, LIGHTPURPLE, (cell[1]*cellSize + marginSize[0], cell[0]*cellSize + marginSize[1], cellSize, cellSize))
           
    # Highlights selected cell
    def highlight_selected_cells(self, window, highlightedCells):
        for cell in highlightedCells:
                pygame.draw.rect(window, LIGHTPINK, (cell[1]*cellSize + marginSize[0], cell[0]*cellSize + marginSize[1], cellSize, cellSize))  

    # Function to determine if mouse is within Sudoku board
    def mouse_position(self):
        # Returns the selected cell within the Sudoku board
        if self.mousePos[1] > marginSize[1] and self.mousePos[0] > marginSize[0] and self.mousePos[1] < marginSize[1]+boardSize and self.mousePos[0] < marginSize[0]+boardSize:
            return ((self.mousePos[1]-marginSize[1]) // 50, (self.mousePos[0]-marginSize[0]) // 50)
        
    # Function to load buttons onto board
    def load_buttons(self):
        self.in_game_buttons.append(Button(75, 600, 100, 40, ))
        self.in_game_buttons.append(Button(250, 600, 100, 40, ))
        self.in_game_buttons.append(Button(425, 600, 100, 40, ))

    # General function to load objects onto board
    def load(self):
        self.load_buttons()
        # Sets locked numbers on board
        for y, row in enumerate(self.board):
            for x, num in enumerate(row):
                if num != 0:
                    self.lockedCells.append((y, x))

    # Determines if input is an integer
    def check_input(self, input):
        try:
            int(input)
            return True
        except:
            return False