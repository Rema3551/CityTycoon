from enum import Enum

class BuildingType(Enum):
    """
    détermine quel type est un batiment et son image associée
    """
    POUBELLE = "poubelle.png"
    ROUGE = "rouge.png"
    HELP = "help.png"
    ORANGE = "orange.png"
    HDV = "hdv.png"
    MAISONETTE = "maisonette.png"
    MAISON = "maison.png"
    TOURDEGUET = "tourDeGuet.png"
    CABANE = "cabane.png"
    ECURIE = "ecurie.png"