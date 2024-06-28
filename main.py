import os
import shutil
from decompresser import decompresser_archive
from extraire_fichiers import extraire_fichiers
from dechiffrer import dechiffrer_fichier
#on réalise les imports nécessaires

DOSSIER_SORTIE = 'dossier_final'        #on définit le dossier de sortie pour les fichiers que l'on extrait

def traiter_fichiers(fichiers_entree, cle=None):
    """ 
    Cette fonction traite une liste de fichiers en les: decompressant, dechiffrant et extrayant,
    puis en regroupant les fichiers extraits dans un dossier de sortie.
    
    Arguments:
    - fichiers_entree: une liste de chemins vers les fichiers à traiter
    - cle: clé de déchiffrement si nécessaire 
    """
    dossier_temp = 'dossier_temp'           #dossier temporaire pour stocker les fichiers que l'on a décompressés/déchiffrés
    
    
    if not os.path.exists(dossier_temp):    #ici on crée le dossier temporaire s'il n'existe pas 
        os.makedirs(dossier_temp)
    
    for fichier in fichiers_entree:                     #on parcourt les fichiers dans la liste des fichiers d'entrées 
        if fichier.endswith('.zip'):                    #si le fichier est un fichier zip
            decompresser_archive(fichier, dossier_temp) #on décompresse
        elif cle and fichier.endswith('.enc'):          # on déchiffre les fichiers chiffrés (.enc) si une clé est fournie
            chemin_dechiffre = os.path.join(dossier_temp, os.path.basename(fichier).replace('.enc', ''))
            dechiffrer_fichier(fichier, chemin_dechiffre, cle)
        else:
            print(f"Type de fichier non supporté ou clé non fournie pour déchiffrement : {fichier}")    # si le type de fichier n'est pas supporté ou si la clé de déchiffrement est absente on affiche un message

    print("Extraction des fichiers...")                 #print de test 
    extraire_fichiers(dossier_temp, DOSSIER_SORTIE)     #on extrait dans le dossier de sortie 
    
    print("Nettoyage du dossier temporaire...")         #print de test
    shutil.rmtree(dossier_temp)                         #on supprime le dossier temporaire

if __name__ == "__main__":
    fichiers_entree = ['exemples/fichier_exemple.zip']  #ici la liste des fichiers d'entrée à traiter 
    cle = None                                          #clé de déchiffrement (mettre la clé réelle si nécessaire)
    traiter_fichiers(fichiers_entree, cle)              #on appelle la fonction principale afin de traiter les fichiers