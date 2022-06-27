# class player:
#     def __init__(self, name:str,sign:str)-> None:
#         self.name = name
#         self.sign = sign
from dataclasses import dataclass

@dataclass(frozen=True)
class player:
    name:str
    sign:str

if __name__ =='__main__':
    player


        
