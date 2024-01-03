import sys,random
import pygame

class Jeu:
    def __init__(self):
        self.ecran =pygame.display.set_mode((800,600))
        pygame.display.set_caption('Jeu snake')
        self.jeu_encours= True

        self.serpent_position_x=300
        self.serpent_position_y=300
        self.serpent_direction_x=0
        self.serpent_direction_y=0
        self.serpent_corps = 10

        self.pomme_position_x = random.randrange(110,690,10)
        self.pomme_position_y = random.randrange(110,590,10)
        self.pomme = 10

        self.clock =pygame.time.Clock()

        self.position_serpent = []

        self.taille_du_serpent = 0


        self.ecran_du_debut = True

        self.image = pygame.image.load('Snake-logo.jpg')
        self.image_titre = pygame.transform.scale(self.image,(200,100))

        self.score = 0

        self.vitesse=20
        

    def fonction_principal(self):

        while self.ecran_du_debut:
            for evenement in pygame.event.get():
                if evenement.type==pygame.QUIT:
                    sys.exit()

                if evenement.type == pygame.KEYDOWN:
                    if evenement.key == pygame.K_RETURN:
                        self.ecran_du_debut = False
                
                self.ecran.fill((0,0,0))

                self.ecran.blit(self.image_titre,(300,50,100,50))
                self.crreer_message('petite','le but du jeux est de développer le serpent',
                                    (250,200,200,5),(240,240,240))
                self.crreer_message('petite','pour cela il a beosin de manger le plus de pommes possible',
                                    (190,220,200,5),(240,240,240))
                self.crreer_message('moyenne','appuyez sur entrée pour continuer !',
                                    (250,450,200,5),(255,255,255))

                pygame.display.flip()
        
        while self.jeu_encours:
            for evenement in pygame.event.get():

                if evenement.type==pygame.QUIT:
                    sys.exit()

                if evenement.type == pygame.KEYDOWN:
                    if evenement.key == pygame.K_RIGHT and self.serpent_direction_x != -10:
                        self.serpent_direction_x = 10
                        self.serpent_direction_y = 0
                    elif evenement.key == pygame.K_LEFT and self.serpent_direction_x != 10:
                        self.serpent_direction_x = -10
                        self.serpent_direction_y = 0
                    elif evenement.key == pygame.K_DOWN and self.serpent_direction_y != -10:
                        self.serpent_direction_x = 0
                        self.serpent_direction_y = 10
                    elif evenement.key == pygame.K_UP and self.serpent_direction_y != 10:
                        self.serpent_direction_x = 0
                        self.serpent_direction_y = -10

            self.serpent_position_x += self.serpent_direction_x
            self.serpent_position_y += self.serpent_direction_y

            if self.pomme_position_y == self.serpent_position_y and self.serpent_position_x == self.pomme_position_x:
                self.pomme_position_x = random.randrange(110,690,10)
                self.pomme_position_y = random.randrange(110,590,10)
                self.taille_du_serpent +=1
                self.score +=1
                self.vitesse +=1




            la_tete_du_serpent = []
            la_tete_du_serpent.append(self.serpent_position_x)
            la_tete_du_serpent.append(self.serpent_position_y)

            if len(self.position_serpent) > self.taille_du_serpent:
                self.position_serpent.pop(0)

            self.position_serpent.append(la_tete_du_serpent)

            if self.serpent_position_x<=100 or self.serpent_position_x >=700 or self.serpent_position_y<=100 or self.serpent_position_y >=600:
                sys.exit()




            self.ecran.fill((0,0,0))

            pygame.draw.rect(self.ecran,(0,255,0),(self.serpent_position_x,self.serpent_position_y,self.serpent_corps,self.serpent_corps))

            pygame.draw.rect(self.ecran,(255,0,0),(self.pomme_position_x,self.pomme_position_y,self.pomme,self.pomme))


            for partie_du_serpent in self.position_serpent:
                pygame.draw.rect(self.ecran,(0,255,50),(partie_du_serpent[0],partie_du_serpent[1],self.serpent_corps,self.serpent_corps))

            for partie_du_serpent in self.position_serpent[:-1]:
                if la_tete_du_serpent == partie_du_serpent:
                    sys.exit()

            self.crreer_message('grande','Snake game',(320,10,100,50),(255,255,255),)
            self.crreer_message('grande',format(str(self.score)),(375,50,50,50),(255,255,255),)

            self.creer_limites()
            self.clock.tick(self.vitesse)

            pygame.display.flip()

    def creer_limites(self):

        pygame.draw.rect(self.ecran,(255,255,255),(100,100,600,500),3)

    def crreer_message(self,font,message,message_rectangle,couleur):
        if font == 'petite':
            font = pygame.font.SysFont('Lato',20,False)
        
        elif font == 'moyenne':
            font = pygame.font.SysFont('Lato',30,False)

        elif font == 'grande':
            font = pygame.font.SysFont('Lato',40,True)

        message = font.render(message, True,couleur)

        self.ecran.blit(message, message_rectangle)



if __name__ == '__main__':
    pygame.init()
    Jeu().fonction_principal()
    pygame.quit()
