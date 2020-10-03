import pygame

#Creation d'une fenetre de 1080x720
window = pygame.display.set_mode((1080, 720))

#importation de l'image de fond et creation de son rectangle
background = pygame.image.load("decor/map.png")
map_rect = background.get_rect()
x_map, y_map = 0, 0

game = True

while game:
    #Efface tout l'ecran (noir)
    window.fill((0, 0, 0))

    #Quand touche espace appuyé ferme la fenetre
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game = False

    #Bouge le fond en fonction de la touche appuyé
    key_move  = pygame.key.get_pressed()
    if key_move[pygame.K_LEFT] and x_map < 0:
        x_map += 10
    elif key_move[pygame.K_RIGHT] and x_map > -map_rect[2]+1080:
        x_map -= 10
    if key_move[pygame.K_UP] and y_map < 0:
        y_map += 10
    elif key_move[pygame.K_DOWN] and y_map > -map_rect[3]+720:
        y_map -= 10

    #Affiche l'image de fond
    window.blit(background, (x_map, y_map))
    pygame.display.flip()

pygame.quit()
exit()