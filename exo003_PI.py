"""
Deux joueurs avec chacun un pseudo
Chaque joueur à 250 points de vie au début du jeu
Deux combats pour chaque joueur : le joueur1 attaque le joueur2 puis au tour du joueur2 puis au tour du joueur1 et au joueur2
Lors du combat : le joueur qui attaque peut râter son attaque ou infliger des points de vie entre 0 et 100
Désignation du gagnant fin de combats : celui qui lui reste le plus de points de vie

Recours à la programmation impérative

Éditeur : Laurent REYNAUD
Date : 10-04-2021
"""

import random

# random_attack = True  # l'attaque a réussi
# random_damage = 0  # dégâts infligés

life_point_player1 = 250
life_point_player2 = 250

player1 = input("Nom du joueur 1 : ")
player2 = input("Nom du joueur 2 : ")

#1ère attaque
print("\nLE COMBAT COMMENCE !\n")

random_attack = random.randint(0, 1)
if random_attack == 1:
	random_damage = random.randint(0, 100)
	life_point_player2 = life_point_player2 - random_damage
	print(f"{player1} a infligé {random_damage} points de vie à {player2}\nNombre de points de vie restant à {player2} : {life_point_player2}")

else:
	print(f"Attaque râtée de {player1} !")

#2ème attaque
print("\nDEUXIEME COMBAT !\n")

random_attack = random.randint(0, 1)
if random_attack == 1:
	random_damage = random.randint(0, 100)
	life_point_player1 = life_point_player1 - random_damage
	print(f"{player2} a infligé {random_damage} points de vie à {player1}\nNombre de points de vie restant à {player1} : {life_point_player1}")

else:
	print(f"Attaque râtée de {player2} !")

#3ème attaque
print("\nTROISIEME COMBAT !\n")

random_attack = random.randint(0, 1)
if random_attack == 1:
	random_damage = random.randint(0, 100)
	life_point_player2 = life_point_player2 - random_damage
	print(f"{player1} a infligé {random_damage} points de vie à {player2}\nNombre de points de vie restant à {player2} : {life_point_player2}")

else:
	print(f"Attaque râtée de {player1} !")

#4ème attaque
print("\nQUATRIEME COMBAT !\n")

random_attack = random.randint(0, 1)
if random_attack == 1:
	random_damage = random.randint(0, 100)
	life_point_player1 = life_point_player1 - random_damage
	print(f"{player2} a infligé {random_damage} points de vie à {player1}\nNombre de points de vie restant à {player1} : {life_point_player1}")

else:
	print(f"Attaque râtée de {player2} !")

#résultat
print("\nRESULTAT DES COMBATS\n")

if life_point_player1 > life_point_player2:
	print(f"Vainqueur : {player1} avec {life_point_player1} points de vie restant")
if life_point_player2 > life_point_player1:
	print(f"Vainqueur : {player2} avec {life_point_player2} points de vie restant")
if life_point_player2 == life_point_player1:
	print("Égalité !")