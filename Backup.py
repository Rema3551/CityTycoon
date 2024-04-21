import pickle
import Game

class Backup():

    def save(self,game: Game):
        # Données à sauvegarder
        data = {
            'player' : {
                'dollars': game.player.getDollars(),
                'diamonds': game.player.getDiamonds(),
                'position_x' : game.player.position[0],
                'position_y' : game.player.position[1]
            },
            'listBuildingsPlayer': game.player.getListBuilding(),
            'map' : game.getMapStep()
        }
        

        # Sauvegarde des données
        with open('data.pickle', 'wb') as file:
            pickle.dump(data, file)
            file.close()
    
    def load(self, game: Game):
        # Restauration des données
        with open('data.pickle', 'rb') as f:
            try: 
                restored_data = pickle.load(f)
                game.restoreData(restored_data)
            except EOFError:
                print("fichier vide")

    def loadMap(self,game : Game):
        # Restauration de la map
        with open('data.pickle', 'rb') as f:
            try: 
                restored_data = pickle.load(f)
                game.restoreMapData(restored_data)
            except EOFError:
                print("fichier vide")