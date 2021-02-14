"""
Chapitre 19 : fichiers et sérialisation/désérialisation des objets
Lien : https://www.youtube.com/watch?v=gVOYPwjd_8c&list=PLrSOXFDHBtfHg8fWBd7sKPxEmahwyVBkC&index=19

Modes d'ouverture : r (lecture seule)
                    w (écriture avec remplacement)
                    a (écriture avec ajout en fin de fichier)
                    x (lecture et écriture) -> peu utilisé
                    r+ (lecture et écriture dans un même fichier) -> peu utilisé

Méthodes pour la lecture : read(), readline(), readlines()
Tout ce qui est récupéré, est une str. Et dans la méthode readlines() ce sont des listes de str qui sont récupérées.

Pour l'écriture, on ne peut écrire qu'au format str

Pour la sérialisation (= équivalent à l'écriture dans un fichier), au lieu de recourir au mode d'ouverture 'w', on a
recours au mode d'ouverture 'wb' dont 'b' veut dire 'binaire' -> écriture en binaire

Pour la désérialisation (= équivalent à la lecture d'un fichier), au lieu de recourir au mode d'ouverture 'r', on a
recours au mode d'ouverture 'rb' dont 'b' veut dire 'binaire' -> lecture en binaire

Éditeur : Laurent REYNAUD
Date : 16-10-2020
"""

import pickle

"""Lecture du fichier"""
with open('pieces/fichier.txt', 'r') as file:
    print(file.read())  # lecture de toutes les lignes du fichier

with open('pieces/fichier.txt', 'r') as file:
    print(file.readline())  # lecture de la 1ère ligne du fichier
    print(file.readline())  # lecture de la 2ème ligne du fichier

with open('pieces/fichier.txt', 'r') as file:
    print(file.readlines())  # lecture de toutes les lignes du fichier NON LUES sous la forme de listes

if file.closed:
    print('fichier fermé !')  # avec l'instruction with open... le fichier est automatiquement fermé
else:
    print('fichier encore ouvert !')

"""Ecriture dans un fichier (avec remplacement de ce qui a été saisi auparavant dans le fichier)"""
with open('pieces/fichier.txt', 'w') as file:
    file.write('Requin\n')
    file.write('Dauphin\n')
    file.write('Baleine\n')

"""Sérialisation et désérialisation des objets"""


class Player:

    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __str__(self):
        return f"{self.name} a un niveau de {self.level}"


p1 = Player('John', 50)
print(p1)
p2 = Player('Marcel', 10)
print(p2)

with open('pieces/fichier.txt', 'wb') as file:
    """Sérialisation des objets p1 et p2"""
    pickle.dump(p1, file)
    pickle.dump(p2, file)

with open('pieces/fichier.txt', 'rb') as file:
    """Sérialisation des objets p1 et p2"""
    pickle.load(file)
print(p1)
print(p2)
