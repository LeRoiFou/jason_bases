#coding:utf-8
"""
Cours : Python #13 - propriétés d'encapsulation
Lien : https://www.youtube.com/watch?v=Fs6XsN6masA&list=PLrSOXFDHBtfHg8fWBd7sKPxEmahwyVBkC&index=13

Principe d'encapsulation vu notamment dans le langage Java :
Tout attribut lié à une classe ne peut pas soit être lue, soit être modifiée depuis l'extérieur de la classe

Dans l'exemple ci-dessous, on a pas recours à l'encapsulation et par conséquent l'utilisateur pourra accéder, modifier 
les valeurs déclarées dans les attributs de la classe

Éditeur : Laurent REYNAUD
Date : 12-04-2021
"""

class Humain:

	def __init__(self, name='Marcel', age=17):
		print("Création d'un être humain...")
		self.name = name
		self.age = age
		self.display()

	def display(self):
		print(f"Nom : {self.name}, âge : {self.age}")


# instanciation de la classe humain en objet h1, EN REPRENANT les valeurs déclarées dans les attributs de cette classe
h1 = Humain()
h1 # résultat d'affichage -> Nom : Marcel, âge : 17
# instanciation de la classe humain en objet h1, EN MODIFIANT les valeurs déclarées dans les attributs de cette classe
h2 = Humain('John', 43)
h2 # résultat d'affichage -> Nom : John, âge : 43 -> on a pu modifier les valeurs des attributs de la classe Humain