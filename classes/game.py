import os      # Import OS
import sys     # Import SYS
import pygame  # Import PyGame

sys.path.append(os.getcwd() + "/classes")  # Ajout du chemin pour éviter les bugs Windows
from mainmenu import MainMenu  # Import de la class MainMenu
from niveau import Niveau      # Import de la class Niveau

sys.path.append(os.getcwd() + "/classes/maps")  # Ajout du chemin pour éviter les bugs Windows
from kamehouse import Kamehouse      # Import de la class Kamehouse
from kamehousein import KamehouseIn  # Import de la class KamehouseIn
from worldtown import WorldTown  # Import de la class WorldTown
from worldtownin import WorldTownIn  # Import de la class WorldTownIn


class Game:
    """ Gestion des variables et import des différentes map du jeu """

    def __init__(self, width, height):
        self.width = width      # Largeur de la fenêtre de jeu
        self.height = height    # Hauteur de la fenêtre du jeu
        self.favicon = 'ressources/favicon.png'  # Chemin du favicon
        self.fps = 24  # FPS limités
        self.avancer = 8.0  # Échelle de déplacement

    def main(self):
        """ Lancement du jeu """
        pygame.init()  # Lance de Pygame
        screen = pygame.display.set_mode((self.width, self.height))  # Crée la fenêtre
        pygame.display.set_caption('PyDragon v0.4')  # Donne un nom à la fenêtre
        pygame.display.set_icon(pygame.image.load(self.favicon))  # Favicon du jeu
        self.son = pygame.mixer.Sound("ressources/sounds/DBZFighter.wav")  # Défini le son du jeu
        self.son.set_volume(0.3)  # Permet de diminuer le son par défaut du jeu

        clock = pygame.time.Clock()  # Calcule le temps de départ pour les FPS

        while Niveau.WHILE_GAME:  # Boucle principale qui sert aux importations de maps
            if Niveau.LVL == 'while_main_menu':  # Nom défini qui orchestre tous les imports liés
                main_menu = MainMenu(screen, clock, self.fps, self.son)  # Instancie la class qui affiche le menu de départ
                main_menu.while_menu()  # Boucle sur le menu
            elif Niveau.LVL == 'while_map_kamehouse':
                map_kamehouse = Kamehouse(self.width, self.height, screen, clock, self.fps, self.avancer)
                map_kamehouse.while_kamehouse()  # Boucle sur la map
            elif Niveau.LVL == 'while_map_kamehouse_in':
                map_kamehouse_in = KamehouseIn(self.width, self.height, screen, clock, self.fps, self.avancer)
                map_kamehouse_in.while_kamehouse_in()  # Boucle sur la map
            elif Niveau.LVL == 'while_map_town':
                map_world = WorldTown(self.width, self.height, screen, clock, self.fps, self.avancer)
                map_world.while_town()  # Boucle sur la map
            elif Niveau.LVL == 'while_map_town_in':
                map_world = WorldTownIn(self.width, self.height, screen, clock, self.fps, self.avancer)
                map_world.while_town_in()  # Boucle sur la map

        pygame.quit()  # Arrête le processus de PyGame
