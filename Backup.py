import shutil
import os

def backup(source, destination):
    try:
        shutil.copytree(source, destination)
        print("Sauvegarde réussie !")
    except shutil.Error as e:
        print(f"Erreur lors de la sauvegarde : {e}")
    except Exception as e:
        print(f"Erreur inattendue : {e}")

# Exemple d'utilisation :
source = '/chemin/vers/le/dossier/source'
destination = '/chemin/vers/le/dossier/de/sauvegarde'

backup(source, destination)
