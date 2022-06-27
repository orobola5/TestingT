class Board:
    def __init__(self):
        self.Board=['*'] *9

    def display_board(self):
        for index,cell in enumerate(self.board):
            if index!=0 and index%3 ==0:
                print()

            if index %3 == 0:
                print("|",end)
            print(f"{cell:^3}",end="") 

    @staticmethod 
    def is_position_allowed(self,position) :
        if  position not in range (1,10):
            raise BoardException("invalid cell position")


    def is_cell_empty(self,position)-> bool:
        self.is_position(position)
        return self.board[position-1] ==' '

    def is_board_full(self):
        return all(self.board)  

    def fill_cell(argsself,position,sign):
        self.is_position(position)
        if self.is_cell_empty(position):
           self.board[position-1] = sign
        else:
            raise BoardException(f"cell position {position} is not empty")
                   

if __name__=='__main__':   
    board = Board()
    print(board.board)  
    board.board[2] = 'x'  

board.display_board()
print(board.is_cell_empty(3))
print(board.is_board_full())