import pygame
import time
import random
#Iniciamos el juego
import inicio
from var import *

pygame.init()
pygame.init()
#Altura y anchura de la pantalla


#Definicion de tipo de letra
small_font = pygame.font.SysFont('Corbel', 35)

#iniciamos la pantalla

startScreen = pygame.display.set_mode((display_width, display_height))
startScreen.fill((60, 25, 60))
pygame.display.set_caption('Prueba 1 - 26-11-2021')
clock = pygame.time.Clock()

salir = small_font.render('Salir', True, white)
jugar = small_font.render('Jugar', True, white)

while True:

    for ev in pygame.event.get():

        if ev.type == pygame.QUIT:
            pygame.quit()

            # checks if a mouse is clicked
        if ev.type == pygame.MOUSEBUTTONDOWN:

            # if the mouse is clicked on the
            # button the game is terminated
            if display_width / 2 <= mouse[0] <= display_width / 2 + 140 and display_height / 2 <= mouse[1] <= display_width / 2 + 40:
                pygame.quit()
            if display_width / 2 -175 <= mouse[0] <= display_width / 2 + 140 and display_height / 2 <= mouse[1] <= display_width / 2 + 40:
                print('ha seleccionado jugar')

                inicio.Inicio.inicio()


    # (x,y)
    # La variable es una tupla
    mouse = pygame.mouse.get_pos()


    #Cambia a un color mas claro si lo pasas por encima ---> Salir
    if display_width / 2 <= mouse[0] <= display_width / 2 + 140 and display_height / 2 <= mouse[1] <= display_height / 2 + 40:
        rect1 = pygame.draw.rect(startScreen, color_light, [display_width / 2, display_height / 2, 140, 40])
    #Vuelve al color original
    else:
        rect1 =pygame.draw.rect(startScreen, color_dark, [display_width / 2, display_height / 2, 140, 40])
        rect2 =pygame.draw.rect(startScreen, color_dark, [display_width / 2  -175, display_height / 2, 140, 40])
    # Cambia a un color mas claro si lo pasas por encima ---> Jugar
    if display_width / 2 - 175 <= mouse[0] <= display_width / 2 + 140 and display_height / 2 <= mouse[1] <= display_height / 2 + 40:
        rect2 =pygame.draw.rect(startScreen, color_light, [display_width / 2 - 175, display_height / 2, 140, 40])

    # Vuelve al color original
    else:
        rect1 =pygame.draw.rect(startScreen, color_dark, [display_width / 2, display_height / 2, 140, 40])
        rect2 =pygame.draw.rect(startScreen, color_dark, [display_width / 2  -175, display_height / 2, 140, 40])

        # superimposing the text onto our button
    startScreen.blit(salir, (display_width / 2 + 50, display_height / 2))
    startScreen.blit(jugar, (display_width / 2 -150, display_height / 2))
    # updates the frames of the game
    pygame.display.update()
