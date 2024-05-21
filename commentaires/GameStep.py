from enum import Enum

class GameStep(Enum):
    """
    détermine l'étape du jeu
    """
    IDLE = 0 #jeu normal
    BUTTONVIDEO = 1 #pancarte video, c'est à dire quand il a appuyé sur le diamant en haut à droite
    CHANGEMENTMAP = 2 #pancarte de changement de map avec les boutons correspondant