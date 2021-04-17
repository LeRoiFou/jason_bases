#coding:utf-8
"""
Cours : Python #13 - propriétés d'encapsulation
Lien : https://www.youtube.com/watch?v=Fs6XsN6masA&list=PLrSOXFDHBtfHg8fWBd7sKPxEmahwyVBkC&index=13

Principe d'encapsulation vu notamment dans le langage Java :
Tout attribut lié à une classe ne peut pas soit être lue, soit être modifiée depuis l'extérieur de la classe

Dans l'exemple ci-dessous, on a recours à l'encapsulation getter qui interdit d'accéder à la valeur d'attribut
d'une classe

Éditeur : Laurent REYNAUD
Date : 12-04-2021
"""

class Humain:

	def __init__(self, name='Marcel', age=17):
		print("Création d'un être humain...")
		self.name = name
		self._age = age

	def _getage(self):
		if self._age <= 1:
			return str(self._age) + " an"
		else:
			return str(self._age) + " ans"

	age = property(_getage)



h1 = Humain()
print(f"{h1.name} a {h1.age}")

h2 = Humain('John', 1)
print(f"{h2.name} a {h2.age}")
