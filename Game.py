from .Board import Board
from .player import player


class Game:
    def __init__(self) -> None:
        self.game_board = Board()
        self.player1 = None
        self.player2 = None
        pass


    def create_player_one(self,name,sign):
        self.player1 = player(name,sign)

    def create_player_one(self,name,sign):
        self.player1 = player(name,sign)
    
    def play(self,player:player,position:int):
        print(f"{player.name}'s turn")
        self.game_board.fill_cell(position,player.sign)

    def determine_winner(self):
        pass
        

