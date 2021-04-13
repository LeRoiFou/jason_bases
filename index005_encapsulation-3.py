#coding:utf-8
"""
Cours : Python #13 - propriétés d'encapsulation
Lien : https://www.youtube.com/watch?v=Fs6XsN6masA&list=PLrSOXFDHBtfHg8fWBd7sKPxEmahwyVBkC&index=13

Principe d'encapsulation vu notamment dans le langage Java :
Tout attribut lié à une classe ne peut pas soit être lue, soit être modifiée depuis l'extérieur de la classe

Dans l'exemple ci-dessous, on a recours à l'encapsulation setter qui interdit la modification de la valeur d'attribut
d'une classe
Il faut obligatoirement passer par un getter pour mettre un setter.
Par contre les valeurs déclarées en argument lors de l'instanciation de la classe, n'ont aucun effet sur l'encapsulation...

Éditeur : Laurent REYNAUD
Date : 12-04-2021
"""

class Human:

	def __init__(self, name="Marcel", age=23):
		print("Création d'un être humain...")
		self.name = name
		self._age = age

	def _getage(self):
		return self._age

	def _setage(self, age):
		if age < 0:
			print("Age négatif refusé !")
			self._age = 0
		else:
			self._age = age

	age = property(_getage, _setage)



h1 = Human()
print(h1.age)
h1.age = -10
print(h1.age)
h2 = Human('John', -5)
print(h2.age)
