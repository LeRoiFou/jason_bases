from dataclasses import dataclass

@dataclass
class TConfig:
    
    # Titre de la fenêtre de l'application
    window_title = "FormationVidéo - exercice Python n° 12"
    
    # Dimensions de la fenêtre (largeur + hauteur)
    window_width = 600
    window_height = 200
    
    # Texte du bouton du minuteur (à l'arrêt + en marche)
    button_text_when_off = "Démarrer le minuteur"
    button_text_when_on = "Stopper le minuteur"
    
    # Paramètres d'affichage du minuteur
    timer_font_family = "Ubuntu"
    timer_font_size = 100
