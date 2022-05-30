import pygame
from enum import Enum
from pygame.examples.aliens import Player

CELL_SIZE = 50
class Cell(Enum):
    VOID = 0
    CROSS = 1
    ZERO = 2

class GameField:
    pass


class GameFieldView:

    def __init__(self, field):
        self._field = field
        self._height = field.height * CELL_SIZE
        self._width = field.width * CELL_SIZE
    def draw(self):
        pass


    def check_coords_correct(self):
        return True



    def check_coords_correct(self):
        return (0, 0)


class Player:
    """
    Класс игрока, содержащий тип значков и имя
    """
    def __init__(self, name, cell_type):
        self.name = name
        self.cell_type = cell_type


class GameRoundManager:
    """
    Менеджер игры
    """
    def __init__(self, player1: Player, player2: Player):
        self.players = [player1, player2]
        self._current_player = 0
        self._field = GameField()

    def handle_click(self):
        player = self.players[self._current_player]


class GameWindow:
    def __init__(self):
        self._field_widget = GameFieldView()
        player1 = Player("Max", Cell.CROSS)
        player2 = Player("Olga", Cell.ZERO)
        self._game_manager = GameRoundManager(player1,player2)

    def main_loop(self):
        finished = False
        while not finished:
            for event in pygame.get_events():
                if event.type == pygame.QUIT:
                    finished = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x,y = event.x, event.y
                    if self._field_widjet.check_coords_correct(x,y):
                        i,j = self._field_widjet.get_coords(x,y)
                        self._game_manager.handle_click(i, j)

