##CE FICHIER EST UN FICHIER UTILISER POUR LES TESTS 

import os
import zipfile

os.makedirs('exemples', exist_ok=True)

# Crée un fichier binaire exemple avec des bytes nuls
with open('exemples/exemple.bin', 'wb') as f:
    f.write(bytes([0]))

# Crée un fichier de signature exemple
with open('exemples/exemple.sig', 'w') as f:
    f.write('Signature')

print("Fichiers d'exemple créés avec succès.")

# Crée une archive zip contenant les fichiers binaires et de signature
with zipfile.ZipFile('exemples/fichier_exemple.zip', 'w') as zipf:
    zipf.write('exemples/exemple.bin', arcname='exemple.bin')
    zipf.write('exemples/exemple.sig', arcname='exemple.sig')

print("Archive zip créée avec succès.")
