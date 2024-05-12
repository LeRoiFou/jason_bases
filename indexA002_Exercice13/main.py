"""
Lien : https://www.youtube.com/watch?v=bvj4pgIHQlc
Cours : Exo Python #13 - dans une époque lointaine
[Révision : gestion des dates]

Écrire un convertisseur de date en durée relative (textuelle), comme on peut le
retrouver sur certains sites et/ou réseaux sociaux pour afficher la date de
publication d'un contenu.

-> Si nous sommes le 15 janvier 2024 et que l'utilisateur saisit le 10/01/2024, 
le programme affichera "Il y a 5 jours"
-> Si nous sommes le 15 janvier 2024 et que l'utilisateur saisit le 14/01/2024,
le programme affichera "Hier"

Indications :

- le convertisseur sera sous forme de fonction qui prendra en paramètre une date
au format "JJ/MM/AAAA" et retournera un echaîne de caractères avec une durée
relative ('Aujourd'hui', 'Hier', 'Il y a ...')

- respectez les formats suivants selon l'ancienneté de la date spécifiée :
    > "Aujourd'hui"             : si moins de 24 heures
    > "Hier"                    : si 24 heures ou plus et moins de 48 heures
    > "Avant-hier"              : si 48 heures ou plus et moins de 72 heures
    > "Il y a x jours"          : si 72 heures ou plus et moins d'une semaine
    > "Il y a x semaines"       : si une semaine ou plus et moins d'un mois
    > "Il y a x mois"           : si un mois ou plus et moins d'un an +
    > "Il y a X ans"            : si un an ou plus

- vous pouvez utiliser les attributs/méthodes vues dans le cours, ou bien
envisager une autre approche en vous intéressant à la classe timedelta
(du module datetime)

- gérer le pluriel des termes "jour", "semaine" et "an"

- gérez les cas d'erreur :
    > si la date saisie n'est pas au bon format
    > si la date saisie est plus récente que la date actuelle

Date : 12-05-24
"""

from datetime import datetime, timedelta

# Erreur en cas de saisie d'une date postérieure la date actuelle
class TooRecentDateError(ValueError):
    pass

def get_duration_text_from_date(input_date):
    
    # Instanciation du format d'heure saisie
    user_date = datetime.strptime(input_date, "%d/%m/%Y")
    
    # Récupération de la date actuelle
    current_date = datetime.now()
    
    # Différence entre la date actuelle et la date saisie
    delta_date = current_date - user_date
    
    # Si la date saisie est postérieure à la date actuelle...
    if delta_date.total_seconds() < 0:
        raise TooRecentDateError(
            "La date saisie est plus récente que la date actuelle")
    
    # Si l'écart ci-avant est < à 24 heures...
    if delta_date < timedelta(hours = 24):
        return "Aujourd'hui"
    
    # Si l'écart est inférieur à 2 jours...
    if delta_date < timedelta(days = 2):
        return "Hier"
    
    # Si l'écart est inférieur à 3 jours...
    if delta_date < timedelta(days = 3):
        return "Avant-hier"
    
    # Si l'écart est inférieur à 1 semaine...
    if delta_date < timedelta(weeks= 1):
        return f"Il y a {delta_date.days} jours"

    # Si l'écart est inférieur à 4 semaines...
    if delta_date < timedelta(weeks= 4):
        return f"Il y a {delta_date.days // 7} {
            "semaine" if (delta_date.days // 7) == 1 else "semaines"}"
            
    # Si l'écart est inférieur à 365 jours...
    if delta_date < timedelta(days = 365):
        return f"Il y a {delta_date.days // 30} mois"
    
    # Si l'écart est d'au moins 1 an...
    else:
        return f"Il y a {delta_date.days // 365} {
            "an" if (delta_date.days // 365) == 1 else "ans"}"
    
try:
    input_date = input("Saisir une date (jj/mm/aaaa) : ")
    print(get_duration_text_from_date(input_date))
    
# La date saisie est postérieure à la date actuelle
except TooRecentDateError as e:
    print(e)
    
# Le format saisie n'est pas respecté
except ValueError:
    print("La date saisie est dans un format incorrect")
