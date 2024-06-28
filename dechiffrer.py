from cryptography.fernet import Fernet  
#on réalise les imports nécessaires

def dechiffrer_fichier(chemin_fichier_chiffre, chemin_fichier_dechiffre, cle):  # on crée l'objet Fernet avec la clé de chiffrement
    fernet = Fernet(cle)
    with open(chemin_fichier_chiffre, 'rb') as fichier_chiffre: # on ouvre le fichier chiffré en mode lecture binaire
        donnees_chiffrees = fichier_chiffre.read()              #on lit le contenu chiffré du fichier

    donnees_dechiffrees = fernet.decrypt(donnees_chiffrees)     #on déchiffre les données lues

    with open(chemin_fichier_dechiffre, 'wb') as fichier_dechiffre: #on ouvre le fichier sortie cette fois ci en écriture binaire
        fichier_dechiffre.write(donnees_dechiffrees)                #on écrit les données déchiffrées dans le fichier de sortie



# Exemple d'utilisation :
# clé = b'votre_clé_de_32_bytes_ici'
# dechiffrer_fichier('chemin/vers/fichier_chiffre', 'chemin/vers/fichier_dechiffre', clé)
