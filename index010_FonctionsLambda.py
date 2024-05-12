"""
Lien : https://www.youtube.com/watch?v=uWZfob-a1jY
Cours : Tutoriel Python - fonction lambda

Fonction lambda : fonction anonyme qui ne sera pas appelée plusieurs fois, ou
lorsque c'est une fonction dans une autre fonction

Syntaxe :
lambda [parametres] : [expression]

Date : 12-05-24
"""

# 1er exemple : appel simplifié d'une fonction lambda
power = lambda n : n ** n
print(power(3))

# 2ème exemple : fonction filtrant uniquement les nombres positifs...
def if_positive(n):
    return n > 0
result = filter(if_positive, [-3, 1, 2, -22, 136, -5])
print(list(result))

# ...En recourant à une fonction lambda
result = filter(lambda n : n > 0, [-3, 1, 2, -22, 136, -5])
print(list(result))

# 3ème exemple avec tkinter

import tkinter as tk

def print_message(message):
    print(f"L'utilisateur a envoyé : {message}")

app = tk.Tk()
app.title("Fonction lambda sur un bouton")
app.geometry("300x200")

btn = tk.Button(
    app, text="Cliquez ici", 
    command=lambda : print_message("Bonjour"))
btn.pack()

app.mainloop()