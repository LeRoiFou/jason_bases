"""
Cours : Tutoriel Python - itérateurs
Lien : https://www.youtube.com/watch?v=H9FIOc-bIHU

Tout élément séquentiel est un itérable : str, tuple, liste, ensemble...

Un itérateur ne porte pas forcément sur un objet itérable : 
Un itérateur permet justement de rendre itérable un objet 
qui peut ne pas être itérable (un entier, un objet créé...)
Pour cela on a recours aux méthodes spéciales d'un itérateur :
iter() et next()

Éditeur : Laurent REYNAUD
Date : 31-08-21
"""

# Exemple d'un objet itérable (str ici)
word = "Hello"
for letter in word:
    # La boucle for va faire appel aux méthodes spéciales iter()/ next()
    print(letter)
    
# Autre exemple d'un objet itérable (liste ici)
li = [1, 2, 3, 4, 5]
iterator = iter(li)
# Affichage une à une des composants dans la liste
while True:
    try:
            print(next(iterator)) 
    except StopIteration:
        break # S'arrête avec l'instruction StopIteration

"Exemple 1 sur l'usage d'un itérateur"
class R:    
    
    def __init__(self, end):  
        if end <= 0:
            raise ValueError("Point d'arrêt de l'intervalle invalide")
        self.current = 0
        self.end = end
        
    def __iter__(self):      
        # Retour uniquement de 'self' car current est un objet non itérable  
        return self
    
    def __next__(self):
        # Objet de cette méthode : que veut-on comme résultat ?
        self.current += 1
        if self.current > self.end:
            raise StopIteration   
        return self.current - 1
 
ran = R(10)
# L'objet ran n'est pas itérable mais en recourant à un itérateur...
for v in ran:
    print(v)
    
"Exemple 2 sur l'usage d'un itérateur"
class Inventory:
    
    def __init__(self, name):     
        self.name = name
        self.content = []
        
    def __iter__(self):
        # Retour de l'attribut d'instance content car c'est un objet itérable
        return iter(self.content)

    def __next__(self):
        # Objet de cette méthode : que veut-on comme résultat ?
        return next(self.content)

    def add(self, item):
        self.content.append(item)
        
chest = Inventory("Large Malle")
chest.add("Épée en bois")
chest.add("Potion de soins mineurs")
chest.add("Marque d'honneur")

# L'objet chest n'est pas itérable mais en recourant à un itérateur...
for item in chest:
    print(item)
