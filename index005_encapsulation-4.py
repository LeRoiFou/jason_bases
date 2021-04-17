#coding:utf-8
"""
Cours : Python #13 - propriétés d'encapsulation
Lien : https://www.youtube.com/watch?v=Fs6XsN6masA&list=PLrSOXFDHBtfHg8fWBd7sKPxEmahwyVBkC&index=13

Principe d'encapsulation vu notamment dans le langage Java :
Tout attribut lié à une classe ne peut pas soit être lue, soit être modifiée depuis l'extérieur de la classe

Dans l'exemple ci-dessous, on a recours au décorateur @property

Éditeur : Laurent REYNAUD
Date : 12-04-2021
"""

class Human:

	def __init__(self, name="Marcel", age=23):
		print("Création d'un être humain...")
		self.name = name
		self.age = age

	@property
	def age(self):  # le nom de la méthode = nom de l'attribut pour lequel une condition va être imposée
		if self._age <=1:
			return f"{self._age} an"  # toujours l'instruction return pour un getter
		else:
			return f"{self._age} ans"

	@age.setter  # @property pour le setter : nomAttribut.setter
	def age(self, age):  # le nom de la méthode = nom de l'attribut pour lequel une condition va être imposée
		if age < 0:
			print("Age négatif refusé !")
			print(f"Par conséquent je considère que l'âge est de 0")
		else:
			self._age = age


h1 = Human()
print(h1.age)
h1.age = 1
print(h1.age)
h1.age = -10
h2 = Human('John', -5)
