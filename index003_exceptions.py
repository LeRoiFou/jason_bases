"""
Chapitre 9 : la gestion des erreurs (les exceptions)
Lien : https://www.youtube.com/watch?v=1IqnpaQy8LM&list=PLrSOXFDHBtfHg8fWBd7sKPxEmahwyVBkC&index=9

L'instruction raise est utilisée lorsque le programmeur considère qu'il y a une erreur selon la valeur déclarée alors
que le programme Python ne détecte aucune erreur.
Mais comme il a été vu dans le cours TDN, cette instruction raise fait 'sauter' le programme. Pour éviter que le
programme s'arrête, il suffit de mettre en dehors du bloc d'instruction raise, les fonctions try/except comme dans
l'exemple ci-après.

Idem avec l'instruction assert qui est plus présentable que l'instruction raise, mais pour recourir aux fonctions
try/except, il faut mentionner l'erreur AssertionError après l'instruction except, pour que le programme ne puisse pas
sauter.

Éditeur : Laurent REYNAUD
Date : 15-10-2020
"""

# Recours à l'instruction raise :
try:
    age = int(input('Age : '))
    if age >= 18:
        print('Tu peux rentrer !')
    else:
        raise ValueError()
except ValueError:
    print('Age non admis !')
print('Fin du programme')

# Recours à l'instryction assert :
try:
    chiffre = (int(input('Donner un chiffre entre 1 et 10 : ')))
    assert 1 <= chiffre <= 10
except AssertionError:
    print("J'ai demandé un chiffre entre 1 et 10 !!! Tu sais compter ?")
else:
    print('Chiffre saisi :', chiffre)
