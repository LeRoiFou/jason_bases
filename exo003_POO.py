"""
Deux joueurs avec chacun un pseudo
Chaque joueur à 250 points de vie au début du jeu
Deux combats pour chaque joueur : le joueur1 attaque le joueur2 puis au tour du joueur2 puis au tour du joueur1 et au joueur2
Lors du combat : le joueur qui attaque peut râter son attaque ou infliger des points de vie entre 0 et 100
Désignation du gagnant fin de combats : celui qui lui reste le plus de points de vie

Recours à la POO

Éditeur : Laurent REYNAUD
Date : 10-04-2021
"""

import random


class Game:

	def __init__(self, player1, player2, life_points_p1, life_points_p2):
		self.player1 = player1
		self.player2 = player2
		self.life_points_p1 = life_points_p1
		self.life_points_p2 = life_points_p2

	def attack_player1(self):
		random_attack = random.randint(0, 1)
		random_damage = random.randint(0, 100)
		if random_attack == 1:
			print(f"{self.player1} a infligé {random_damage} points de vie à {self.player2}")
			self.life_points_p2 = self.life_points_p2 - random_damage
			print(f"Nombre de points de vie restant à {self.player2} : {self.life_points_p2}")
		else:
			print(f"{self.player1} a râté son attaque !")

	def attack_player2(self):
		random_attack = random.randint(0, 1)
		random_damage = random.randint(0, 100)
		if random_attack == 1:
			print(f"{self.player2} a infligé {random_damage} points de vie à {self.player1}")
			self.life_points_p1 = self.life_points_p1 - random_damage
			print(f"Nombre de points de vie restant à {self.player1} : {self.life_points_p1}")
		else:
			print(f"{self.player2} a râté son attaque !")

	def result(self):
		print("\nRESULTAT FINAL\n")
		if self.life_points_p1 > self.life_points_p2:
			print(f"{self.player1} a gagné les combats avec {self.life_points_p1} points de vie restant")
		if self.life_points_p2 > self.life_points_p1:
			print(f"{self.player2} a gagné les combats avec {self.life_points_p2} points de vie restant")
		if self.life_points_p2 == self.life_points_p1:
			print("Égalité !!!")


if __name__ == '__main__':
	
	name_player1 = input('Nom du joueur n° 1 : ')
	name_player2 = input('Nom du joueur n° 2 : ')
	player = Game(name_player1, name_player2, 250, 250)

	n = 1
	while n < 5 :
		print(f"\nCOMBAT N° {n} !\n")
		n +=1
		player.attack_player1()
		print(f"\nCOMBAT N° {n} !\n")
		player.attack_player2()
		n +=1

	player.result()