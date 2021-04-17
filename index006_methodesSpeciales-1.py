"""
Cours : Tutoriel Python - méthodes spéciales
Lien : https://www.youtube.com/watch?v=XxUasK8f-s0&list=PLOjJPxPKiEjupPvKkwRV0yOIQxHyCLQas&index=2

Exemple du recours de la méthode spéciale __repr__() utilisée pour les classes qui permet d'afficher les attributs
de la classe

Tableau des méthodes spéciales : https://nsa39.casimages.com/img/2017/10/16/171016051550274310.png

Éditeur : Laurent REYNAUD
Date : 17-04-2021
"""

class Lapin:

	def __init__(self, name, weight):
		self.name = name
		self.weight = weight
		self.hello()

	def hello(self):
		print("En recourant à une méthode personnelle")
		if self.weight >= 10 :
			print(f"Hello lapin {self.name} tu pèses {self.weight} kg et je te trouve très gros !")
		else:
			print(f"Hello lapin {self.name} tu pèses {self.weight} kg... il ne fallait pas le dire ?!?")

	def __repr__(self):
		print("En recourant à la méthode spéciale __repr__")
		if self.weight >= 10 :
			return f"Hello lapin {self.name} tu pèses {self.weight} kg et je te trouve très gros !"
		else:
			return f"Hello lapin {self.name} tu pèses {self.weight} kg... il ne fallait pas le dire ?!?"

lp1 = Lapin('Coco', 5)  # pour exécuter la méthode personnelle hello()
print(lp1)  # exécution automatique de la méthode spéciale __repr__()