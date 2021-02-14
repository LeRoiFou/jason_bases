"""
Chapitre 8 : la modularité
Lien : https://www.youtube.com/watch?v=A2aD4eQP0qU&list=PLrSOXFDHBtfHg8fWBd7sKPxEmahwyVBkC&index=8

Création d'un module qui va être importé dans un autre fichier : les explications sur la modularité sont explicités au
fichier suivant

Éditeur : Laurent REYNAUD
Date : 15-10-2020
"""


def parler(personnage, message):
    return f"{personnage} : {message}"


def au_revoir():
    print('Au revoir !')


"""La fonction spéciale ci-après permet de tester la viabilité de ce fichier alors qu'on peut s'apercevoir que les 
instructions ci-avant ne comprennent que des fonctions qui ne sont pas appelées par le programmeur utilisateur"""
if __name__ == "__main__":
    parler("Gerald", "Test !")
    au_revoir()
