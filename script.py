import pygame

#Classe de la map
class Map:

    def __init__(self):
        self.image = pygame.image.load("decor/map.png")
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

        self.bats = []

        self.money = 0

    def move_left(self):
        if self.rect.x < 0:
            self.rect.x += 10
            for i in self.bats:
                i.MajPos(10,0)

    def move_right(self):
        if self.rect.x > -self.rect[2] + 1080:
            self.rect.x -= 10
            for i in self.bats:
                i.MajPos(-10,0)

    def move_up(self):
        if self.rect.y < 0:
            self.rect.y += 10
            for i in self.bats:
                i.MajPos(0,10)

    def move_down(self):
        if self.rect.y > -self.rect[3] + 1080:
            self.rect.y -= 10
            for i in self.bats:
                i.MajPos(0,-10)

    def add_new_bat(self, mouse):
        self.bats.append(Batiment(mouse))

    def get_nb_bats(self):
        return len(self.bats)

    def affichage(self, window):
        window.blit(self.image, self.rect)
        for i in self.bats:
            i.Affichage()
        

#Classe des batiments
class Batiment:

    def __init__(self, mouse):
        self.image = pygame.image.load("decor/batiment.png")
        self.rect = self.image.get_rect()
        self.rect.x = mouse[0]+10
        self.rect.y = mouse[1]+10

    def Affichage(self):
        window.blit(self.image, self.rect)

    def MajPos(self, x, y):
        self.rect.x += x
        self.rect.y += y


window = pygame.display.set_mode((1080, 720))

#Creation de la map
map = Map()

game = True

while game:
    window.fill((0, 0, 0))
    mouse_pos = ((pygame.mouse.get_pos()[0] // 40) * 40, (pygame.mouse.get_pos()[1] // 40 * 40))

    #Quand on appuie sur une touche
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            #Fermer la fenetre quand on appuis sur echap
            if event.key == pygame.K_ESCAPE:
                game = False
            elif event.key == pygame.K_RETURN:
                print(map.get_nb_bats())

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