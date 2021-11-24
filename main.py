import pygame
import time
import random
#Iniciamos el juego
pygame.init()

#Altura y anchura de la pantalla
display_width = 800
display_height = 600

#colores utilizados
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (150, 450, 100)
bright_green = (150, 350, 100)
block_color = (53, 115, 255)
color_light = (170, 170, 170)
color_dark=(100, 100, 100)

#Definicion de tipo de letra
small_font = pygame.font.SysFont('Corbel', 35)

#iniciamos la pantalla
startScreen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()

salir = small_font.render('Salir', True, white)
jugar = small_font.render('Jugar',True, white)
# carImg = pygame.image.load('racecar.png')

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

                # fills the screen with a color
    startScreen.fill((60, 25, 60))

    # stores the (x,y) coordinates into
    # the variable as a tuple
    mouse = pygame.mouse.get_pos()

    # if mouse is hovered on a button it
    # changes to lighter shade
    if display_width / 2 <= mouse[0] <= display_width / 2 + 140 and display_height / 2 <= mouse[1] <= display_height / 2 + 40:
        pygame.draw.rect(startScreen, color_light, [display_width / 2, display_height / 2, 140, 40])

    else:
        pygame.draw.rect(startScreen, color_dark, [display_width / 2, display_height / 2, 140, 40])

        # superimposing the text onto our button
    startScreen.blit(salir, (display_width / 2 + 50, display_height / 2))

    # updates the frames of the game
    pygame.display.update()
'''
def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: " + str(count), True, black)
    startScreen.blit(text, (0, 0))


def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(startScreen, color, [thingx, thingy, thingw, thingh])


# def car(x, y):
#    gameDisplay.blit(carImg, (x, y))


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    startScreen.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    # game_loop()


def crash():
    message_display('You Crashed')


def button(msg, x, y, w, ic, ac, action=None):  # button("GO!", 150, 450, 100, 50, green, bright_green, print('Go'))
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x + w > mouse[0] > x and y  > mouse[1] > y:
        pygame.draw.rect(startScreen, ac, (x, y, w))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(startScreen, ic, (x, y, w))

    smallText = pygame.font.SysFont("comicsansms", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y +  2))
    startScreen.blit(textSurf, textRect)


def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        startScreen.fill(white)
        largeText = pygame.font.SysFont("comicsansms", 115)
        TextSurf, TextRect = text_objects("A bit Racey", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        startScreen.blit(TextSurf, TextRect)

        button("GO!", 150, 450, 100, green, bright_green, print('Go'))
        button("Quit", 550, 450, 100,  red, green, print('Quit'))


'''
'''
def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 4
    thing_width = 100
    thing_height = 100

    thingCount = 1

    dodged = 0

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        gameDisplay.fill(white)

        things(thing_startx, thing_starty, thing_width, thing_height, block_color)

        thing_starty += thing_speed
        car(x, y)
        things_dodged(dodged)

        if x > display_width - car_width or x < 0:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            dodged += 1
            thing_speed += 1
            thing_width += (dodged * 1.2)

        if y < thing_starty + thing_height:
            print('y crossover')

            if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
                print('x crossover')
                crash()

        pygame.display.update()
        clock.tick(60)

game_intro()
# game_loop()
pygame.quit()
quit()
'''