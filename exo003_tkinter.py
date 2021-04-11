"""
Deux joueurs avec chacun un pseudo
Chaque joueur à 250 points de vie au début du jeu
Deux combats pour chaque joueur : le joueur1 attaque le joueur2 puis au tour du joueur2 puis au tour du joueur1 et au joueur2
Lors du combat : le joueur qui attaque peut râter son attaque ou infliger des points de vie entre 0 et 100
Désignation du gagnant fin de combats : celui qui lui reste le plus de points de vie

Recours à l'interface graphique tkinter

Éditeur : Laurent REYNAUD
Date : 10-04-2021
"""

import random
import tkinter
from tkinter import Tk


class Execute_game:

	def __init__(self, root, player1, player2, life_points_p1, life_points_p2):
		self.root = root
		new_window = tkinter.Toplevel()
		self.my_text = tkinter.Listbox(new_window, justify='center', width=100, height=20)
		self.my_text.pack()
		self.player1 = player1
		self.player2 = player2
		self.life_points_p1 = life_points_p1
		self.life_points_p2 = life_points_p2
		n = 1
		while n < 5 :			
			self.my_text.insert('end', f"\nCOMBAT N° {n} !\n")
			self.attack_player1()
			self.my_text.insert('end', "\n")
			n += 1
			self.my_text.insert('end', f"\nCOMBAT N° {n} !\n")
			self.attack_player2()
			self.my_text.insert('end', "\n")
			n += 1
		self.result()

	def attack_player1(self):
		random_attack = random.randint(0, 1)
		random_damage = random.randint(1, 100)
		if random_attack == 1:
			self.my_text.insert('end', f"{self.player1} a infligé {random_damage} points de vie à {self.player2}\n")
			self.life_points_p2 = self.life_points_p2 - random_damage
			self.my_text.insert('end', f"Nombre de points de vie restant à {self.player2} : {self.life_points_p2}\n\n")
		else:
			self.my_text.insert('end', f"{self.player1} a râté son attaque !\n\n")

	def attack_player2(self):
		random_attack = random.randint(0, 1)
		random_damage = random.randint(1, 100)
		if random_attack == 1:
			self.my_text.insert('end', f"{self.player2} a infligé {random_damage} points de vie à {self.player1}\n")
			self.life_points_p1 = self.life_points_p1 - random_damage
			self.my_text.insert('end', f"Nombre de points de vie restant à {self.player1} : {self.life_points_p1}\n\n")
		else:
			self.my_text.insert('end', f"{self.player2} a râté son attaque !\n\n")

	def result(self):
		self.my_text.insert('end', "RESULTAT FINAL\n")
		if self.life_points_p1 > self.life_points_p2:
			self.my_text.insert('end', f"{self.player1} a gagné les combats avec {self.life_points_p1} points de vie restant\n")
		if self.life_points_p2 > self.life_points_p1:
			self.my_text.insert('end', f"{self.player2} a gagné les combats avec {self.life_points_p2} points de vie restant\n")
		if self.life_points_p2 == self.life_points_p1:
			self.my_text.insert('end', "Égalité !!!\n")


class GUI:

	def __init__(self, root):
		# configuration de la fenêtre principale
		self.root = root
		self.root.resizable(False, False)
		self.root.title('Le combat des titans !')
		self.widgets()

	def execute_game(self):
		# méthode instanciant la classe Execute_game ci-dessus
		execute = Execute_game(self.root, self.entry_player1.get(), self.entry_player2.get(),250, 250)

	def widgets(self):
		# configuration des widgets de la fenêtre principale
		my_frame = tkinter.Frame(self.root)
		my_frame.pack(pady=30)
		label_player1 = tkinter.Label(my_frame, text='Nom du joueur n° 1 :')
		label_player1.grid(row=0, column=0, padx=5, pady=5)
		self.entry_player1 = tkinter.Entry(my_frame, justify='center')
		self.entry_player1.grid(row=0, column=1, padx=5, pady=5)
		label_player2 = tkinter.Label(my_frame, text='Nom du joueur n° 2 :')
		label_player2.grid(row=1, column=0, padx=5, pady=5)
		self.entry_player2 = tkinter.Entry(my_frame, justify='center')
		self.entry_player2.grid(row=1, column=1, padx=5, pady=5)
		button_execute = tkinter.Button(my_frame, text='Exécuter !', command=self.execute_game)
		button_execute.grid(row=2, column=0, columnspan=2, padx=5, pady=10)


if __name__ == '__main__':

	root = tkinter.Tk()	
	gui = GUI(root)
	root.mainloop()