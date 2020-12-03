import sys
import pygame
from pygame.locals import *
from src.astro_war.client.states.base_state import BaseState

#needed to use pygame
pygame.init()
pygame.display.set_caption('game base')

#initialize display window
screen = pygame.display.set_mode((500, 500), 0, 32) #better use same values as in config, daclare it as global

#print(pygame.font.get_fonts())      # to get all fonts
font = pygame.font.SysFont("Arial", 20)

#click says if we clicked
click = False


def draw_text(text, font, color, surface, x, y):
    """
    print the text given a text, a font, a color, a surface and coord
    """
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def main_menu():
    """
    let us configure a menu
    """
    while True:

        #base display
        screen.fill((0, 0, 0))
        draw_text('main menu', font, (255, 255, 255), screen, 20, 20)

        #mouse pos
        mx, my = pygame.mouse.get_pos()

        #button + click test
        button_1 = pygame.Rect(50, 100, 200, 50)
        button_2 = pygame.Rect(50, 200, 200, 50)
        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                options()
        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)

        #return click to false if not clicked
        click = False

        #check events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()


def game():
    running = True
    while running:
        screen.fill((0, 0, 0))

        draw_text('game', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()


def options():
    running = True
    while running:
        screen.fill((0, 0, 0))

        draw_text('options', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()



class Menu(BaseState):

    # ----- Constructor -----

    def __init__(self, game):
        super().__init__("Menu", game)
        main_menu()

