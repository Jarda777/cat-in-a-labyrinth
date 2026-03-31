import random
import pygame
from datetime import datetime


pygame.init()

clock = pygame.time.Clock()

WIDTH, HEIGHT = 1856, 992
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("bludiste aka Schrödingerova kočka")

FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 128)
RED = (170, 0, 10)


souradnice = [[8*32, 15*32],[40*32, 1*32 ],[13*32, 29*32],[34*32, 29*32],[37*32, 19*32],[53*32, 29*32],[24*32, 4*32 ],[1*32, 17*32],[51*32, 17*32],[15*32, 9*32],[31*32, 19*32],[2*32, 26*32]]
random.shuffle(souradnice)

#print(souradnice[0][0])

myimage1 = pygame.image.load("floor_brick_mossy_d.png")
imagerect1 = myimage1.get_rect()

myimage0 = pygame.image.load("floor_darkgreen_c.png")
imagerect0 = myimage0.get_rect()

playerimage = pygame.image.load("monsters_cat_e_smaller.png")
playerimagerect = playerimage.get_rect()

tresure1 = pygame.image.load("features_sarcophagus_d.png")
tresure1rect = pygame.Rect(souradnice[1][0], souradnice[1][1] , 32, 32)

tresure2 = pygame.image.load("features_sarcophagus_e.png")
tresure2rect = pygame.Rect(souradnice[2][0], souradnice[2][1]  , 32, 32)

tresure3 = pygame.image.load("features_sarcophagus_f.png")
tresure3rect = pygame.Rect(souradnice[3][0], souradnice[3][1]  , 32, 32)

tresure4 = pygame.image.load("features_sarcophagus_a.png")
tresure4rect = pygame.Rect(souradnice[4][0], souradnice[4][1]  , 32, 32)

tresure5 = pygame.image.load("features_sarcophagus_b.png")
tresure5rect = pygame.Rect(souradnice[5][0] , souradnice[5][1] , 32, 32)

tresure6 = pygame.image.load("features_sarcophagus_c.png")
tresure6rect = pygame.Rect(souradnice[6][0], souradnice[6][1]  , 32, 32)


vision = pygame.image.load("barrier.png")
visionrect = pygame.Rect(souradnice[7][0], souradnice[7][1]  , 32, 32)

vision2 = pygame.image.load("barrier.png")
visionrect2 = pygame.Rect(souradnice[8][0], souradnice[8][1] , 32, 32)

vision3 = pygame.image.load("barrier.png")
visionrect3 = pygame.Rect(souradnice[9][0], souradnice[9][1] , 32, 32)

runn = pygame.image.load("haste.png")
runnrect = pygame.Rect(souradnice[0][0], souradnice[0][1] , 32, 32)

portal = pygame.image.load("summon_horizontal_resized.png")
portalrect = pygame.Rect(27*32, 19*32 , 64, 32) 

ghost = pygame.image.load("silent_spectre.png")
ghostrect = pygame.Rect(27*32, 19*32 , 32, 32) 


def draw_mask(win, player_x,player_y, radius):
    mask_surface = pygame.Surface((WIDTH,HEIGHT))
    mask_surface.fill(BLACK)


    pygame.draw.circle(mask_surface, WHITE, (player_x, player_y), radius)
    mask_surface.set_colorkey(WHITE)  

    win.blit(mask_surface, (0, 0))




class bludiste():
    def __init__(self,POLE,radky,sloupce):

        
        self.POLE = POLE
        self.radky = radky
        self.sloupce = sloupce 
        self.nenula = []
        self.bludiste_listy = []


    def create_map(self):
        self.bludiste_positions = []
        for i in range(self.radky):
            proces_listy = []
            for j in range(self.sloupce):
                rect = pygame.Rect(j*32, i*32 , 32, 32)
                if self.POLE[i][j] == 1:
                    rect1 = pygame.Rect(j*32, i*32 , 32, 32)
                    self.bludiste_positions.append([rect1,1])

                elif self.POLE[i][j] == 0:
                    rect0 = pygame.Rect(j*32, i*32 , 32, 32)
                    self.bludiste_positions.append([rect0,0])

                if self.POLE[i][j] != 0:
                    self.nenula.append(rect)
                proces_listy.append(rect)
            self.bludiste_listy.append(proces_listy)



                    
    def draw_bludiste(self,myimage0,myimage1,win):
        for i in self.bludiste_positions:
            if i[1] == 0:
                win.blit( myimage0,(i[0].x, i[0].y, 32, 32))
                
                
            if i[1] == 1:
                win.blit( myimage1,(i[0].x, i[0].y, 32, 32))
        if player.colision_tresure1 == False:
            win.blit( tresure1 ,(tresure1rect.x, tresure1rect.y, 32, 32))
        if player.colision_tresure2 == False:
            win.blit( tresure2 ,(tresure2rect.x, tresure2rect.y, 32, 32))
        if player.colision_tresure3 == False:
            win.blit( tresure3 ,(tresure3rect.x, tresure3rect.y, 32, 32))
        if player.colision_tresure4 == False:
            win.blit( tresure4 ,(tresure4rect.x, tresure4rect.y, 32, 32))
        if player.colision_tresure5 == False:
            win.blit( tresure5 ,(tresure5rect.x, tresure5rect.y, 32, 32))
        if player.colision_tresure6 == False:
            win.blit( tresure6 ,(tresure6rect.x, tresure6rect.y, 32, 32))
        if player.collision_vision == False:
            win.blit( vision ,(visionrect.x, visionrect.y, 32, 32))
        if player.collision_vision2 == False:
            win.blit( vision2 ,(visionrect2.x, visionrect2.y, 32, 32))
        if player.collision_vision3 == False:
            win.blit( vision3 ,(visionrect3.x, visionrect3.y, 32, 32))
        if player.collision_runn == False:
            win.blit( runn ,(runnrect.x, runnrect.y, 32, 32))
        if player.colision_portal == False:
            win.blit( portal ,(portalrect.x, portalrect.y, 32, 32))
        



class player:
    def __init__(self,x,y,width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.VEL = 5
        self.colision_tresure1 = False
        self.colision_tresure2 = False
        self.colision_tresure3 = False
        self.colision_tresure4 = False
        self.colision_tresure5 = False
        self.colision_tresure6 = False
        self.collision_vision = False
        self.collision_vision2 = False
        self.collision_vision3 = False
        self.collision_runn = False
        self.colision_portal = False
        self.colision_wallrect = False

        



        self.score = 0
        self.visionapply = 0


    def move(self,keys,win):

        
        


        self.keys = keys


        original_x = self.x
        original_y = self.y

        if keys[pygame.K_w]:
            self.y -= self.VEL
        if keys[pygame.K_s]:
            self.y += self.VEL
        if keys[pygame.K_a]:
            self.x -= self.VEL
        if keys[pygame.K_d]:
            self.x += self.VEL

        

        

        self.player_rect = pygame.Rect(self.x, self.y, 17, 17)




        

        
        if self.collision_runn == False and self.player_rect.colliderect(runnrect):
            self.collision_runn = True
            self.VEL = self.VEL + 3
            #print("Lrunn")

        
        if not self.collision_vision2 and self.player_rect.colliderect(visionrect2):
            self.collision_vision2 = True
            self.visionapply += 20

        if not self.collision_vision and self.player_rect.colliderect(visionrect):
            self.collision_vision = True
            self.visionapply += 20

        if not self.collision_vision3 and self.player_rect.colliderect(visionrect3):
            self.collision_vision3 = True
            self.visionapply += 20

        if not self.colision_tresure3 and self.player_rect.colliderect(tresure3rect):
            self.colision_tresure3 = True
            self.score += 1
            #print(self.score)

        if not self.colision_tresure1 and self.player_rect.colliderect(tresure1rect):
            self.colision_tresure1 = True
            self.score += 1
            #print(self.score)

        if not self.colision_tresure2 and self.player_rect.colliderect(tresure2rect):
            self.colision_tresure2 = True
            self.score += 1
            #print(self.score)

        if not self.colision_tresure4 and self.player_rect.colliderect(tresure4rect):
            self.colision_tresure4 = True
            self.score += 1
            #print(self.score)

        if not self.colision_tresure5 and self.player_rect.colliderect(tresure5rect):
            self.colision_tresure5 = True
            self.score += 1
            #print(self.score)

        if not self.colision_tresure6 and self.player_rect.colliderect(tresure6rect):
            self.colision_tresure6 = True
            self.score += 1
            #print(self.score)

        if not self.colision_portal and self.player_rect.colliderect(portalrect) and self.score == 6:
            self.colision_portal = True



        for i in Bludiste.nenula:
            if self.player_rect.colliderect(i):
                self.x = original_x
                self.y = original_y
                


    def draw(self,playerimage,win):
        win.blit( playerimage,(self.x, self.y, 32, 32))


class moving_ghost:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.velocity = 4  
        self.width = width
        self.height = height
        self.direction = None  
        self.colision_ghost = False

    def move(self, walls,POLE):
        if self.direction is None:
            # Inicializace počátečního směru v náhodném směru
            self.direction = random.choice([(1, 0), (0, 1), (-1, 0), (0, -1)])

        # Vypočítat novou pozici
        new_x = self.x + self.direction[0] * self.velocity
        new_y = self.y + self.direction[1] * self.velocity
        
    

        self.ghostrect = pygame.Rect(new_x, new_y, self.width, self.height)


        # Kontrola kolizí

        free = True
        for wall in walls:
            if self.ghostrect.colliderect(wall):
             
                
                free = False
                break

        if not free:
            self.direction = random.choice([(1, 0), (0, 1), (-1, 0), (0, -1)])  # Náhodně vybereme nový směr
            #self.move(walls)  # Pokusíme se o nový pohyb s novým směrem
        else:
            # Pokud je pohyb volný, aktualizujeme pozici
          

            self.x = new_x
            self.y = new_y

    def draw(self, win):
        win.blit( ghost ,(self.x, self.y, 32, 32))

       


radky = 31
sloupce = 58

POLE  = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,1,0,1,0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,1,0,1,1,1,1,1,0,0,0,1,1,0,1,1,1,0,0,0,1,0,1,1,0,1,1,1,0,1,1,1,1,1,1,0,0,0,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1],
            [1,0,1,0,0,0,0,0,1,0,1,0,1,0,0,1,0,1,0,1,0,0,0,1,1,0,1,0,1,0,1,0,0,0,0,0,0,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1],
            [1,0,1,0,1,1,1,0,1,0,1,0,1,0,1,0,0,0,0,1,0,1,0,1,0,0,1,0,1,0,0,0,1,1,1,1,0,1,0,1,0,1,0,0,1,1,1,0,1,1,1,1,1,1,1,1,0,1],
            [1,0,1,0,0,0,1,0,1,0,1,1,1,0,1,0,1,0,1,0,0,1,0,1,1,0,1,0,1,0,1,0,0,0,0,1,0,1,0,1,1,1,0,1,1,0,1,0,0,0,0,0,0,0,0,1,0,1],
            [1,0,1,1,1,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,1,0,0,0,0,0,1,0,1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,1,1,1,1,1,1,0,1],
            [1,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0,1,0,0,0,1,1,1,1,1,1,1,0,1,0,1,0,0,0,1,1,1,1,1,1,1,0,1,1,1,0,0,1,0,0,0,0,0,0,0,0,0,1],
            [1,1,1,1,1,0,1,0,1,0,1,0,1,1,1,1,1,0,0,0,1,0,0,0,0,0,0,0,1,0,1,0,1,1,1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,1,1,1,1,1,1,1,1,1],
            [1,0,0,0,0,0,1,0,0,0,1,0,0,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,0,1,0,0,0,1,0,1,0,1,1,1,1,0,0,1,0,0,1,0,0,0,0,0,0,0,1],
            [1,1,0,1,1,0,1,1,1,1,1,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,1,1,1,0,1,0,1,0,0,0,0,1,0,0,1,1,0,0,0,1,1,1,0,1],
            [1,0,0,0,0,0,1,0,0,0,0,0,1,0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,0,0,0,0,1,0,1,1,1,1,0,0,1,0,0,1,0,1,0,1,0,1],
            [1,0,1,0,1,1,1,0,1,1,1,1,1,0,1,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,1,1,1,0,0,1,0,0,1,0,1,0,0,1,1,0,0,0,1,0,1],
            [1,0,1,0,1,1,1,0,0,0,0,0,0,0,1,0,1,1,0,1,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,1,0,0,1,0,1,0,1],
            [1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,0,0,0,0,0,0,0,0,0,1,1,1,0,1,0,0,0,1,1,1,1,1,1,1,1,0,1,0,1,0,1,1,1,0,0,1,1,0,1,0,1],
            [1,0,1,0,1,1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,1,1,1,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,1],
            [1,0,1,0,0,0,0,0,0,0,1,0,1,1,1,1,1,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0,0,1,0,1,0,1],
            [1,0,1,0,1,1,1,1,1,1,1,0,1,0,0,0,1,1,1,1,1,0,0,1,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,1,0,1],
            [1,1,1,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0,1,0,0,0,0,1,1,1,1,0,0,1,1,1,1,1,0,0,0,1,1,1,1,1,0,1,0,0,1,0,1,0,1],
            [1,0,1,0,1,0,1,1,1,1,1,1,1,0,0,1,0,0,1,0,0,0,0,1,0,1,0,0,0,0,1,0,0,1,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1],
            [1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,0,1,0,1,0,0,0,0,1,0,0,0,1,0,1,0,0,1,0,0,0,1,0,0,0,0,1,1,0,1,0,1,0,0,0,1],
            [1,0,0,0,1,1,1,1,0,1,1,1,1,1,1,0,1,0,1,0,1,0,0,1,1,1,1,0,0,1,1,1,1,0,1,1,1,0,1,0,0,1,0,1,1,1,1,1,0,1,0,1,0,1,1,1,1,1],
            [1,0,1,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,1,1,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,1,0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,0,0,0,1,0,0,0,1,0,0,1,0,1,0,0,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1],
            [1,0,1,0,1,1,1,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,1,1,1,0,0,1,0,1,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,1,1,0,1,1,1,0,1,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,1,1,0,1,0,1,0,1,0,1],
            [1,0,0,1,0,0,1,0,1,1,1,0,1,1,1,1,1,0,0,1,0,0,0,0,1,0,0,1,0,1,0,0,1,1,1,1,1,1,1,1,0,1,1,1,0,1,0,1,0,0,0,1,0,1,0,1,0,1],
            [1,0,1,1,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,1,1,1,0,0,1,0,0,1,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,1,0,1,0,1],
            [1,0,1,1,1,0,1,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,0,0,1,0,1,1,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,1,1,1,0,1,0,1,0,1,0,1],
            [1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]




Bludiste = bludiste(POLE,radky,sloupce)
Bludiste.create_map()
player = player(32,32,32,32)
moving_ghost1 = moving_ghost(7*32,11*32,32,32)
moving_ghost2 = moving_ghost(1*32, 29*32, 32, 32)
moving_ghost3 = moving_ghost(25*32, 29*32, 32, 32)
moving_ghost4 = moving_ghost(45*32, 19*32, 32, 32)
moving_ghost5 = moving_ghost(45*32, 7*32, 32, 32)



puvodni_min = int(datetime.now().strftime('%M'))
puvodni_hodiny = int(datetime.now().strftime('%H'))

puvodni_minuty = puvodni_min * 60
puvodni_sekundy = int(datetime.now().strftime('%S'))
celkovy_puvodni_cas = puvodni_minuty + puvodni_sekundy + (puvodni_hodiny *60 *60)
#print(puvodni_min,puvodni_sekundy)


collide_rect_b = False


captions = "n"
run = True

while run:
    clock.tick(FPS)
    aktualni_min = int(datetime.now().strftime('%M'))
    aktualni_hodiny = int(datetime.now().strftime('%H'))
    aktualni_minuty = aktualni_min * 60
    aktualni_sekundy = int(datetime.now().strftime('%S'))
    celkovy_aktualni_cas = aktualni_minuty + aktualni_sekundy + (aktualni_hodiny *60 *60)
    stopky_v_s = celkovy_aktualni_cas - celkovy_puvodni_cas
    #print(stopky_v_s)

    
    previous_time = clock.get_time()
    fps = clock.get_fps()
    #print(previous_time)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
    keys = pygame.key.get_pressed()
    
    player.move(keys,WIN)
    moving_ghost1.move(Bludiste.nenula, POLE)
    moving_ghost2.move(Bludiste.nenula, POLE)
    moving_ghost3.move(Bludiste.nenula, POLE)
    moving_ghost4.move(Bludiste.nenula, POLE)
    moving_ghost5.move(Bludiste.nenula, POLE)



    WIN.fill(BLACK)

    Bludiste.draw_bludiste(myimage0,myimage1,WIN)

    player.draw(playerimage,WIN)

    moving_ghost1.draw(WIN)
    moving_ghost2.draw(WIN)
    moving_ghost3.draw(WIN)
    moving_ghost4.draw(WIN)
    moving_ghost5.draw(WIN)


    collide_blok = pygame.Rect(3*32, 18*32, 32, 15)
    append_blok = pygame.Rect(3*32, 19*32, 32, 32)


    if player.player_rect.colliderect(collide_blok):
        Bludiste.nenula.append(append_blok)
        WIN.blit( myimage1, append_blok)
        collide_rect_b = True
    if collide_rect_b == True:
        WIN.blit( myimage1, append_blok)


    draw_mask(WIN, player.x + 9, player.y + 9, 100 + player.visionapply)



    # TEXT

    font = pygame.font.Font('freesansbold.ttf', 32)
    player_score = "TREASURES:      " + str(player.score) + "/6"
    text = font.render(player_score, True, WHITE)
    textRect = text.get_rect()

    textRect.center = (WIDTH // 2 - 50, 16)

    WIN.blit(text, textRect)

    fonts = pygame.font.Font('freesansbold.ttf', 32)
    stopky_v_s = "TIME: " + str(stopky_v_s) 
    texts = fonts.render(stopky_v_s, True, WHITE)
    textsRect = texts.get_rect()

    textsRect.center = (WIDTH // 2+800, 16)

    WIN.blit(texts, textsRect)

    # konec textu

    
    if player.player_rect.colliderect(moving_ghost1.ghostrect) or player.player_rect.colliderect(moving_ghost2.ghostrect) or player.player_rect.colliderect(moving_ghost3.ghostrect) or player.player_rect.colliderect(moving_ghost4.ghostrect) or player.player_rect.colliderect(moving_ghost5.ghostrect):
            run = False
            captions = "RIP"
    
    if player.colision_portal == True:
        break

    

    pygame.display.update()

if captions == "RIP":
    run3 = True
    while run3:
        clock.tick(FPS)
        
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run3 = False
                break

        WIN.fill(RED)

        """
        proces = 0

        while proces < 50:

            x_ghost = random.randint(0,57*32)
            y_ghost = random.randint(0,30*32)

            WIN.blit( ghost ,(x_ghost,y_ghost , 32, 32))
            proces += 1
        pygame.time.wait(500)
        """

        font6 = pygame.font.Font('freesansbold.ttf', 120)
        cap = "RIP"
        text6 = font6.render(cap, True, BLACK)
        textRect6 = text6.get_rect()

        textRect6.center = (WIDTH // 2, HEIGHT // 2)

        WIN.blit(text6, textRect6)
        
        

        pygame.display.update()
    
else:

    if player.colision_portal == True:    
        run2 = True
        while run2:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run2 = False
                    break

            WIN.fill(BLACK)

            proces = 0

            while proces < 50:

                x_ghost = random.randint(0,57*32)
                y_ghost = random.randint(0,30*32)

                WIN.blit( tresure1 ,(x_ghost,y_ghost , 32, 32))
                proces += 1
                
            pygame.time.wait(500)


            font5 = pygame.font.Font('freesansbold.ttf', 120)
            won = "you won"
            text5 = font5.render(won, True, WHITE)
            textRect5 = text5.get_rect()

            textRect5.center = (WIDTH // 2, HEIGHT // 2)

            WIN.blit(text5, textRect5)


            
            pygame.display.update()


pygame.quit()