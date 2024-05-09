from enum import Enum

class GameStep(Enum):
    """
    détermine l'étape du jeu
    """
    IDLE = 0
    BUTTONVIDEO = 1
    CHANGEMENTMAP = 2