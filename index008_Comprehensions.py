"""
Cours :  Tutoriel Python - liste en compréhension
Lien : https://www.youtube.com/watch?v=Vf9Wwa1CGgk

Dans ce programme on apprend à utiliser des compréhensions de liste
établis sous le format suivant :

[<expression> for <value> in <list> if <condition 1> if <condition...>]

Éditeur : Laurent REYNAUD
Date : 30-11-2021
"""
    
li = [1, 2, 3, 4, 5, 6, 7, 8, 9]

"1er exemple"

for el in li:
    print(el)
    
# Équivaut à ça :
[print(el) for el in li]


"2ème exemple"

nli = []

for el in li:
    nli.append(el)
print(nli)
    
# Équivaut à ça :
nli = [el for el in li]
print(nli)

# Et une incrémentation de 1 :
nli_bis = [el + 1 for el in li]
print(nli_bis)

# Avec uniquement les chiffres pairs à partir de 4 :
nli_ter = [el for el in li if el % 2 == 0 if el >= 4]
print(nli_ter)

# En recourant aux booléens pour vrai si pair et faux si impair :
nli_quater = [True if el % 2 == 0 else False for el in li]
print(nli_quater)


"3ème exemple"

dli = [
    [1, 2, 3, 4],
    [10, 20, 30, 40],
    [100, 200, 300, 400]]
print(dli)

ndli = []

for subli in dli:
    for el in subli:
        ndli.append(el)
print(ndli)

# Équivaut à ça :
ndli = [el for subli in dli for el in subli]
print(ndli)
