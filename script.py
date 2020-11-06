import pygame

#Classe de la map
class Map:

    #Initialisation des variables
    def __init__(self):
        #Carte positions
        self.image = pygame.image.load("decor/map.png")
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

        #Liste des batiments
        self.bats = []

        #Variable des ressources
        self.money = 0

    #Deplacement gauche
    def move_left(self):
        if self.rect.x < 0:
            self.rect.x += 10
            for i in self.bats:
                i.MajPosition(10,0)

    #Deplacement droite
    def move_right(self):
        if self.rect.x > -self.rect[2] + 1080:
            self.rect.x -= 10
            for i in self.bats:
                i.MajPosition(-10,0)

    #Deplacement haut
    def move_up(self):
        if self.rect.y < 0:
            self.rect.y += 10
            for i in self.bats:
                i.MajPosition(0,10)

    #Deplacement bas
    def move_down(self):
        if self.rect.y > -self.rect[3] + 1080:
            self.rect.y -= 10
            for i in self.bats:
                i.MajPosition(0,-10)

    #Ajout d'un batiment
    def add_new_bat(self, mouse):
        self.bats.append(Batiment(mouse))

    #Augmentation de l'argent
    def AddRessource(self, ressource):
        if(ressource == "money"):
            self.money += 1

    #Affichage dans la fenetre
    def affichage(self, window):
        #Affichage carte
        window.blit(self.image, self.rect)

        #Affichage batiments
        for i in self.bats:
            i.Affichage()
            i.Production(self)

        #Affichage money 
        font = pygame.font.SysFont('Lato',40,True)
        message = font.render("Money : " + str(self.money),True,(255,255,255))
        window.blit(message, (20,10,100,50))


#Classe des batiments
class Batiment:

    #Initialisation des varaibles
    def __init__(self, mouse):
        #Position du batiment
        self.image = pygame.image.load("decor/batiment.png")
        self.rect = self.image.get_rect()
        self.rect.x = mouse[0]+10
        self.rect.y = mouse[1]+10

        #Production du batiment
        self.production = 1;
        self.tempsProd = 50; #en nombre d'image par sec
        self.temps = 0;

    #Affichage du batiment
    def Affichage(self):
        window.blit(self.image, self.rect)

    #Mise a jour de la position du batiment
    def MajPosition(self, x, y):
        self.rect.x += x
        self.rect.y += y

    #production de l'argent
    def Production(self,map):
        self.temps += 1
        if(self.temps == self.tempsProd):
            self.temps = 0
            map.AddRessource("money")


#Initialisation de la fenetre
pygame.init()
window = pygame.display.set_mode((1080, 720))
clock = pygame.time.Clock()

#Creation de la map
map = Map()

game = True

while game:

    clock.tick(20)

    window.fill((0, 0, 0))
    mouse_pos = ((pygame.mouse.get_pos()[0] // 40) * 40 + (map.rect.x % 40), (pygame.mouse.get_pos()[1] // 40 * 40) + (map.rect.y % 40))

    #Quand on appuie sur une touche
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            #Fermer la fenetre quand on appuis sur echap
            if event.key == pygame.K_ESCAPE:
                game = False

        #Creer un batiment quand on clique 
        if event.type == pygame.MOUSEBUTTONDOWN:
            map.add_new_bat(mouse_pos)

    #Deplacement de la camera
    key_move = pygame.key.get_pressed()
    if key_move[pygame.K_LEFT]:
        map.move_left()
    elif key_move[pygame.K_RIGHT]:
        map.move_right()
    if key_move[pygame.K_UP]:
        map.move_up()
    elif key_move[pygame.K_DOWN]:
        map.move_down()

    #Affichage dans la fenetre
    map.affichage(window)
    pygame.draw.rect(window, (255, 255, 255), (mouse_pos[0], mouse_pos[1], 40, 40))
    pygame.display.flip()

pygame.quit()
exit()