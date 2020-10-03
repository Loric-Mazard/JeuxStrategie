import pygame

class Batiment:
    image = pygame.image.load("decor/batiment.png")
    rect = image.get_rect()
    posX,posY = 0, 0

window = pygame.display.set_mode((1080, 720))

background = pygame.image.load("decor/map.png")
map_rect = background.get_rect()
x_map, y_map = 0, 0

game = True

while game:
    window.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game = False
           
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("click")

    key_move  = pygame.key.get_pressed()
    if key_move[pygame.K_LEFT] and x_map < 0:
        x_map += 10
    elif key_move[pygame.K_RIGHT] and x_map > -map_rect[2]+1080:
        x_map -= 10
    if key_move[pygame.K_UP] and y_map < 0:
        y_map += 10
    elif key_move[pygame.K_DOWN] and y_map > -map_rect[3]+720:
        y_map -= 10

    
    window.blit(background, (x_map, y_map))
    pygame.display.flip()

pygame.quit()
exit()