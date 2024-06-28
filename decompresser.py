import zipfile
import os
import shutil
#on réalise les imports nécessaires

def decompresser_archive(chemin_archive, dossier_sortie):
    """
    Cette fonction décompresse une archive dans un dossier de sortie spécifié.
    
    Arguments:
    - chemin_archive: le chemin vers le fichier d'archive à décompresser
    - dossier_sortie: le chemin vers le dossier où extraire les fichiers
    """

    if chemin_archive.endswith('.zip'):                         #on vérifie si le fichier est une archive zip 
        with zipfile.ZipFile(chemin_archive, 'r') as archive:   #on ouvre le fichier en mode lecture 
            archive.extractall(dossier_sortie)                  #on extrait le contenu de l'achive dans le dossier de sortie
    else:
        print(f"Format d'archive non supporté : {chemin_archive}") #on affiche un message si le format de l'archie n'est pas supporté ici

   


