"""
Chapitre 8 : la modularité
Lien : https://www.youtube.com/watch?v=A2aD4eQP0qU&list=PLrSOXFDHBtfHg8fWBd7sKPxEmahwyVBkC&index=8

Importation du fichier Player.py qui devient un module lorsqu'on l'importe dans un autre fichier .Py à condition que le
fichier importé se trouve dans le même répertoire que le fichier où on l'importe

La modularité est notamment utile lorsqu'on a recours à des fonctions (et non des méthodes incluses dans des classes)
assez longues et qu'elles sont appelées en tant que module (comme le module math, le module random...) pour obtenir une
meilleure visibilité des programmes

Éditeur : Laurent REYNAUD
Date : 15-10-2020
"""
import main

main.au_revoir()
print(main.parler('John', 'Hello !'))
