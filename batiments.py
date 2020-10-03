import pygame

class Batiment():

    def __init__(self):
        self.image = pygame.image.load("decor/batiment.png")
        self.rect = self.image.get_rect();
        self.posX = pygame.mouse.get_pos()[0] // 20 * 20
        self.posY = pygame.mouse.get_pos()[1] // 20 * 20
        

#Creation d'une fenetre de 1080x720
window = pygame.display.set_mode((1080, 720))

game = True
batiments = [];

while game:
    #Efface tout l'ecran (noir)
    window.fill((0, 0, 0))

    #Quand touche espace appuyé ferme la fenetre
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game = False

        #Quand on clique souris affiche un batiment a l'emplacement de la souris
        if event.type == pygame.MOUSEBUTTONDOWN:
            batiments.append(Batiment())

    #Afficher chaque batiment
    for batiment in batiments:
        window.blit(batiment.image, (batiment.posX, batiment.posY))

    pygame.display.flip()

pygame.quit()
exit()