import pygame
import time
import random



WIDTH, HEIGHT = 1000,800 #size of the screen
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) #Setting window height
pygame.display.set_caption("Snaker") #Name of the window

BG = pygame.transform.scale(pygame.image.load("Background.jpg"), (WIDTH, HEIGHT))
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
PLAYER_VEL = 5
def draw(player):
    WIN.blit(BG,(0, 0))
    pygame.draw.rect(WIN, "red", player)
    pygame.display.update()
def main():
    run = True # this ensures the games always running

    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    clock = pygame.time.Clock()
    while run:
        clock.tick(144)
        for event in pygame.event.get(): #This is when a button/click happens
            if event.type == pygame.QUIT: #If someone wants ot quit the game
                run = False # Ends the game
                break #Clears the screen
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            player.x -= PLAYER_VEL
        if keys[pygame.K_d]:
            player.x += PLAYER_VEL
        if keys[pygame.K_s]:
            player.y += PLAYER_VEL
        if keys[pygame.K_w]:
            player.y -= PLAYER_VEL
        draw(player)
    pygame.quit() #quits the game after the while loop

if __name__ == "__main__": #If the file is called it makes sure that the loop for the game isn't started
    main()