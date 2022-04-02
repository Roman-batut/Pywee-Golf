"""Imports"""


import pygame

import math



"""Main"""


def main() :

    #Initialisation
    pygame.init()
    clock = pygame.time.Clock()
    
    #Title and Icon 
    pygame.display.set_caption("Pywee-Golf")
    pygame.display.set_icon(pygame.image.load("assets/icon.png"))
    
    #Screen
    l, L = 512, 512
    display = pygame.display.set_mode((l, L), pygame.RESIZABLE)

    #Background
    background = pygame.image.load("assets/background.png")
    

    #Ball
    ballpng = pygame.image.load("assets/ball.png")
    ballx, bally = 256, 256
    
    def ball(x, y) :
        display.blit(ballpng, (x, y)) 

    #Club
    club = False
    force = 1
    clubpng = pygame.image.load("assets/club.png")
    cursor = pygame.mouse.get_cursor()

    
    #Functions
    def dist(x1, x2, y1, y2) :
        distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
        return(distance)

    
    #Game Loop
    while True :
        
        #Background Color and Image
        display.fill((255,255,255))
        display.blit(background, (0,0))

        #Events
        for event in pygame.event.get() :
            #Exit Game
            if event.type == pygame.QUIT : 
                pygame.quit()
            #Curseur
            if event.type == pygame.MOUSEBUTTONDOWN :
                if event.button == 1 :
                    club = True
                    pygame.mouse.set_pos((ballx + 8, bally + 64))
                    pygame.mouse.set_cursor((16, 16), clubpng)
                    pygame.mouse.set_visible(True)

                
                elif event.button == 3 :
                    #curseur qui dessine ?
                    club = False
                    pygame.mouse.set_visible(False)
            
            
            if event.type == pygame.MOUSEWHEEL :
                force += event.y
                pygame.mouse.set_pos(((ballx + 8) + force * 8, bally + 64))





    


        #Ball
        ball(ballx, bally)



        #Finalization
        pygame.display.update()
        clock.tick(60)


main()







            


