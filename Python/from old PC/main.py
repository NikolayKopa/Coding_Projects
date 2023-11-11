"""
- Starts the game and displays the home screen
- Contains buttons to navigate to the tetris and minesweeper games
"""

import pygame
from buttonClass import Button, Text, pygame_exit
from Minesweeper import minesweeper_main
from Tetris import tetris_main

# Starts the game and creates the window 
pygame.init()
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))

# Defines welcome text
title = Text("Welcome to Our Game!", (255, 255, 255), "comicsans", 100)

# Defines the buttons to navigate to the tetris and minesweeper games
button_width = display_width/3
tetris_button = Button((50,50,225), display_width/4 - button_width/2, 250, button_width, 100, tetris_main.main,"Tetris", 0, None, 'comicsans', 60, (255,255,255), (40,40,150))
minesweeper_button = Button((255,50,50), display_width/4 - button_width/2 + display_width/2, 250, button_width, 100, minesweeper_main.main,"Minesweeper", 0, None, 'comicsans', 60, (255,255,255), (150,40,40))
button_list = [tetris_button, minesweeper_button]

# Game Loop
gameExit = False
while not gameExit:
    # Ends the game loop if the user tries to closes the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
            break
    
    # Draws background
    pygame.draw.rect(gameDisplay, (255,50,50), (pygame.Rect(0,0,display_width/2,display_height)))
    pygame.draw.rect(gameDisplay, (50,50,225), (pygame.Rect(display_width/2,0,display_width/2,display_height)))

    # Draws buttons
    for button in button_list:
        button.draw(gameDisplay)

    # Displays welcome text
    title.display_text(gameDisplay, display_width/2 - title.text.get_width()/2, 50)

    #updates the window
    pygame.display.update()

# closes the window when the game loop ends
pygame_exit()
