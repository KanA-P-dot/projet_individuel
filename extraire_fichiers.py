import os
import shutil
#on réalise les imports nécessaires

def extraire_fichiers(dossier_entree, dossier_sortie):
    """
    Cette fonction extrait tous les fichiers .bin et .sig d'un dossier d'entrée
    et les copie dans un dossier de sortie spécifié.
    
    Arguments:
    - dossier_entree: le chemin vers le dossier contenant les fichiers à extraire
    - dossier_sortie: le chemin vers le dossier où copier les fichiers extraits
    """
    if not os.path.exists(dossier_sortie):                      #on vérifie si le dossier n'existe pas 
        os.makedirs(dossier_sortie)                             #on le crée si nécessaire

    for root, _, files in os.walk(dossier_entree):              #on parcourt le dossier d'entrée
        for file in files:
            if file.endswith('.bin') or file.endswith('.sig'):  #on vérifie si le fichier a l'extension .bin ou .sig
                chemin_fichier = os.path.join(root, file)       #on construit le chemin complet du fichier
                shutil.copy(chemin_fichier, dossier_sortie)     #on copie le fichier dans le dossier de sortie 

