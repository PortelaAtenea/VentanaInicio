import pygame

from main import startScreen
from var import *


class Inicio:
    def inicio():
        del startScreen
        pantalla2 = pygame.display.set_mode((display_width, display_height))
        pygame.display.update()
        pantalla2.fill(black)