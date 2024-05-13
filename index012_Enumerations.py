"""
Lien : https://www.youtube.com/watch?v=HJI5ETooMso
Cours : Tutoriel Python - énumérations

Autre doc : https://connect.ed-diamond.com/gnu-linux-magazine/glmfhs-115/utilisez-les-enumerations-en-python

Les valeurs sont prédéfinies avec une énumération, et sont immuables

Date : 13-05-24
"""
import enum

# Une première façon de définir une énumération
# OrderStatus = enum.Enum("OderStatus",  ["NOTHING", "PENDING", "PAID", "CANCELLED"])

# Une autre façon de définir une énumération (héritant la librairie Enum),
# mais ce n'est pas à proprement à parler d'une classe car on ne peut pas
# instancier cette classe
class OrderStatus(enum.Enum):
    NONE = enum.auto() # valeur = 1
    PENDING = enum.auto() # valeur = 2
    PAID = enum.auto() # valeur = 3
    CANCELLED = enum.auto() # valeur = 4

# Affichage de la valeur et du nom de la variable ==========================
order_status = OrderStatus.NONE
order_status = OrderStatus.PAID

print(order_status.value) 
print(order_status.name)
print(order_status.value) 
print(order_status.name)
print("*"*70)

# Toutes les valeurs sont immuables ===========================================
ods = OrderStatus.PENDING
print(id(ods))

ods = OrderStatus.PAID
print(id(ods))
print("*"*70)

# Affichage de la valeur en str ==============================================
class NewStatus(enum.StrEnum):
    NONE = "Vide"
    PENDING = "En attente de paiement"
    PAID = "Payée"
    CANCELLED = "Annulée"

new_statuts = NewStatus.PENDING
print(new_statuts)

new_statuts = NewStatus.CANCELLED
print(new_statuts)
print("*"*70)

# Identifiant unique ===========================================================
# @enum.verify(enum.UNIQUE)
# class NewStatus2(enum.Enum):
#     NONE = 1
#     PENDING = 2
#     PAID = 1
#     CANCELLED = 3

# new_statuts2 = NewStatus2.PENDING
# print(new_statuts2) # Erreur : la variable NONE est la même valeur que PAID

# Valeurs continues ====================================================
# @enum.verify(enum.CONTINUOUS)
# class NewStatus3(enum.Enum):
#     NONE = 1
#     PENDING = 2
#     PAID = 3
#     CANCELLED = 6

# new_statuts3 = NewStatus3.PENDING
# print(new_statuts3) # Erreur : la variable NONE est la même valeur que PAID
