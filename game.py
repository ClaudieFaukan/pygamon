import pygame
import pytmx
import pyscroll

from player import Player


class Game:
    def __init__(self):

        # creer la fenetre du jeu
        self.screen = pygame.display.set_mode((800, 600))
        #nom du jeu
        pygame.display.set_caption("Pygamon by Pierre-Alain Petrel")
        #chargement de la carte
        tmx_data = pytmx.util_pygame.load_pygame('carte.tmx')
        #on le passe a pyscroll
        map_data = pyscroll.data.TiledMapData(tmx_data)
        #tout les layers de la map
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        #zoom sur la carte
        map_layer.zoom = 2
        #on recupere le point de spawn defini sur la carte au prealable sur tiled
        player_position = tmx_data.get_object_by_name("player")
        #Generer un joueur
        self.player = Player(player_position.x, player_position.y)

        #dessiner le groupe de calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=3)
        #ajout du joeur dans la map
        self.group.add(self.player)

    #recupere les input joueur
    def handle_input(self):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_ESCAPE]:
            self.running = False
        elif pressed[pygame.K_UP]:
            self.player.move_player("up")
        elif pressed[pygame.K_DOWN]:
            self.player.move_player("down")
        elif pressed[pygame.K_RIGHT]:
            self.player.move_player("right")
        elif pressed[pygame.K_LEFT]:
            self.player.move_player("left")


    def run(self):

        # boucle du jeu
        running = True

        while running:
            #on cherche l'input avant d'enclencher tout les elements
            self.handle.input()
            #on actualise le group avant de draw
            self.group.update()
            #on initialise la camera sur le joueur
            self.group.center(self.player.rect.center)
            #dessine les calques dans l'ecran
            self.group.draw(self.screen)
            #pour actualiser a chaquer tour de boucle
            pygame.display.flip()
            # ecoute les events
            for event in pygame.event.get():
                # si clique sur quit
                if event.type == pygame.QUIT:
                    running = False

        pygame.quit()
