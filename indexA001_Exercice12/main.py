"""
Lien : https://www.youtube.com/watch?v=er4eJLmY2CU
Cours : Exo Python #12 - avec le temps va tout s'en va

Mis en place d'un GUI sur un minuteur qui reprend le temps écoulé après mis
en pause et recours de la superbe méthode dataclasses pour affecter des 
attributs du GUI dans une autre classe

Date : 05-05-24
"""

import tkinter as tk
import time
from tconfig import TConfig

class TimerGUI(tk.Tk):
    
    def __init__(self):
        
        # Configuration de la fenêtre principale
        super().__init__()
        self.title(TConfig.window_title)
        self.geometry(f"{TConfig.window_width}x{TConfig.window_height}")
        
        # Assignation d'un booléen pour le minuteur
        self.running = False
        
        # Assignation d'un nombre entier pour le temps démarré
        self.start_time = 0
        
        # Assignation d'un nombre entier pour le temps écoulé
        self.elapsed_time = 0
        
        # Appel de la méthode ci-après
        self.init_widgets()
        
    def init_widgets(self):
        
        # Configuration du texte
        self.timer_label = tk.Label(
            self, 
            text="00:00:00", 
            font=(TConfig.timer_font_family, TConfig.timer_font_size))
        self.timer_label.pack()
        
        # Configuration du bouton
        self.timer_button = tk.Button(
            self, 
            text=TConfig.button_text_when_off,
            command=self.handle_timer)
        self.timer_button.pack()
    
    # Fonctionnalité du bouton d'exécution
    def handle_timer(self):
        
        # Si le minuteur est False
        if self.running:
            self.stop_timer() # Arrêt du minuteur
        else:
            self.start_timer() # Démarrage du minuteur
            self.update_timer() # MAJ du minuteur
     
    # Arrêt du minuteur
    def stop_timer(self):
        
        # Si le minuteur est lancé
        if self.running:
            
            # Changement du texte du bouton d'exécution
            self.timer_button.config(text=TConfig.button_text_when_off)
            
            # Booléen attribué au minuteur
            self.running = False
            
    
    # Démarrage du minuteur
    def start_timer(self):
        
        # Si le minuteur n'est pas lancé
        if not self.running:
            
            # Changement du texte du bouton d'exécution
            self.timer_button.config(text=TConfig.button_text_when_on)
            
            # Démarrage du compteur
            self.start_time = time.time()
            
            # Booléen attribué au minuteur
            self.running = True
    
    # MAJ du minuteur
    def update_timer(self):
        
        # Si le minuteur est lancé
        if self.running:
            
            # Récupération du temps actuel
            current_time = time.time()
            
            # Temps écoulé = temps actuel - temps de départ
            self.elapsed_time += current_time - self.start_time
            
            # MAJ du texte selon le format défini à la méthode ci-après
            self.timer_label.config(text=self.format_time(self.elapsed_time))
            
            # MAJ du temps qui s'écoule dans la variable start_time
            self.start_time = current_time
            
            # MAJ dans le GUI
            self.after(1_000, self.update_timer)
    
    # Format du temps à afficher
    def format_time(self, seconds):
        
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        
        return "{:02d}:{:02d}:{:02d}".format(
            int(hours), int(minutes), int(seconds))


if __name__ == '__main__':
    app = TimerGUI()
    app.mainloop()
