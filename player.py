import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        #on initialise la super classe sinon pas prise en compte par le jeu
        super().__init__()
        self.sprite_sheet = pygame.image.load('personnage.png')
        #on recupere l'iamge 
        self.image = self.get_image(0, 0)
        #on enleve le background
        self.image.set_colorkey([0, 0, 0])
        #quand on initialise un sprite on doit aussi lui donner un rectangle pour definir sa position
        self.rect = self.image.get_rect()
        #on recupere la position du joeur
        self.position = [x, y]

    #remet a jour la position du joueur automatiquement
    def update(self):
        self.rect.topleft = self.position

    #permet de recuperer les coordoonnes en x et en y
    def get_image(self, x, y):
        #on donne la taille du personnage de l'image
        image = pygame.Surface([32, 32])
        #on extrait un morceau de l'image
        image.blit(self.sprite_sheet, (0, 0), (x, y, 32, 32))
        return image