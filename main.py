import pygame
import time
import random

WIDTH, HEIGHT = 1000,800 #size of the screen
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) #Setting window height
pygame.display.set_caption("Snaker") #Name of the window

def main():
    run = True # this ensures the games always running

    while run:
        for event in pygame.event.get(): #This is when a button/click happens
            if event.type == pygame.QUIT: #If someone wants ot quit the game
                run = False # Ends the game
                break #Clears the screen
    pygame.quit() #quits the game after the while loop

if __name__ == "__main__": #If the file is called it makes sure that the loop for the game isn't started
    main()