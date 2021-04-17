"""
Cours : Tutoriel Python - méthodes spéciales
Lien : https://www.youtube.com/watch?v=XxUasK8f-s0&list=PLOjJPxPKiEjupPvKkwRV0yOIQxHyCLQas&index=2

Exemple du recours de la méthode spéciale __eq__ pour comparer deux objets avec des attributs identiques

Tableau des méthodes spéciales : https://nsa39.casimages.com/img/2017/10/16/171016051550274310.png

Éditeur : Laurent REYNAUD
Date : 17-04-2021
"""

class Lapin:

	def __init__(self, name, weight):
		self.name = name
		self.weight = weight

	def __eq__(self, other):
		return self.weight == other.weight


lp1 = Lapin('Coco', 5)

lp2 = Lapin('Titi', 7)
if lp1 == lp2:
	print("Ceux sont les mêmes lapins")
else:
	print("Ils sont différents")

lp3 = Lapin('Coco', 5)
if lp1 == lp3:
	print("Ceux sont les mêmes lapins")
else:
	print("Ils sont différents")