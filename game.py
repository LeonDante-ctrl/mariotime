import pygame
from pygame.locals import *
#Initializing game instance
pygame.init()
fps = 60

clock = pygame.time.Clock()

screen_width = 1000
screen_height = 700
# Creating game window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Platformer")

#game variables
tile_size= 50
#Loading Images
# Image for background
background = pygame.image.load('images/background.png')

#Drawing Tile Grid
def draw_grid():
    for line in range(0,20):
        pygame.draw.line(screen, (255,255,255), (0, line*tile_size),(screen_width,line*tile_size))
        pygame.draw.line(screen, (255,255,255), (line*tile_size,0),(line*tile_size,screen_height))
class Player():
    def __init__(self,x,y):
        img=pygame.image.load('images/mainChar.png')
        self.image = pygame.transform.scale(img, (180,150))
        self.rect = self.image.get_rect()
        self.rect.x=x
        self.rect.y =y
        self.vel_y =0
        self.jumped= False

    def update(self):

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.x -= 5
        if key[pygame.K_RIGHT]:
            self.rect.x += 5
        if key[pygame.K_UP] and self.jumped == False:
            self.vel_y = -20
            self.jumped =True
        if key[pygame.K_UP] == False:
            self.jumped= False


        self.vel_y += 3

        if self.vel_y > 10:
            self.vel_y =10

        self.rect.y += self.vel_y
        
        #check for collision at coordinates
        

        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height




        screen.blit(self.image, self.rect)


class World():
    
    def __init__(self,data):
        self.tile_list =[]
        ground = pygame.image.load('images/ground.png')
        l_edge = pygame.image.load('images/eLeft.png')
        r_edge = pygame.image.load('images/edgeRight.png')
        f_middle = pygame.image.load('images/f_middle.png')
        g_middle = pygame.image.load('images/lr_grass.png')
        g_left = pygame.image.load('images/l_grass.png')
        g_right = pygame.image.load('images/r_grass.png')

        rows = 0
        for row in data:
            cols = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(ground, (tile_size, tile_size))
                    #Giveng images coordinates
                    g_rect = img.get_rect()
                    g_rect.x= cols * tile_size
                    g_rect.y= rows * tile_size
                    tile = (img, g_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(l_edge, (tile_size, tile_size))
                    #Giveng images coordinates
                    g_rect = img.get_rect()
                    g_rect.x= cols * tile_size
                    g_rect.y= rows * tile_size
                    tile = (img, g_rect)
                    self.tile_list.append(tile)
                if tile == 3:
                    img = pygame.transform.scale(r_edge, (tile_size, tile_size))
                    #Giveng images coordinates
                    g_rect = img.get_rect()
                    g_rect.x= cols * tile_size
                    g_rect.y= rows * tile_size
                    tile = (img, g_rect)
                    self.tile_list.append(tile)
                if tile == 4:
                    img = pygame.transform.scale(f_middle, (tile_size, tile_size))
                    #Giveng images coordinates
                    g_rect = img.get_rect()
                    g_rect.x= cols * tile_size
                    g_rect.y= rows * tile_size
                    tile = (img, g_rect)
                    self.tile_list.append(tile)
                if tile == 5:
                    img = pygame.transform.scale(g_left, (tile_size, tile_size))
                    #Giveng images coordinates
                    g_rect = img.get_rect()
                    g_rect.x= cols * tile_size
                    g_rect.y= rows * tile_size
                    tile = (img, g_rect)
                    self.tile_list.append(tile)
                if tile == 6:
                    img = pygame.transform.scale(g_middle, (tile_size, tile_size))
                    #Giveng images coordinates
                    g_rect = img.get_rect()
                    g_rect.x= cols * tile_size
                    g_rect.y= rows * tile_size
                    tile = (img, g_rect)
                    self.tile_list.append(tile)
                if tile == 7:
                    img = pygame.transform.scale(g_right, (tile_size, tile_size))
                    #Giveng images coordinates
                    g_rect = img.get_rect()
                    g_rect.x= cols * tile_size
                    g_rect.y= rows * tile_size
                    tile = (img, g_rect)
                    self.tile_list.append(tile)
                
                
                cols += 1
            rows += 1
    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])

world_data = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,2,4,4,4,4,4,4,4,4,3],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,2,4,4,3,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,2,4,4,4,4,3,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0],
    [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3],
]
player = Player(100, screen_height - 180)
world = World(world_data)
#Loop for runnig game.
run = True
while run == True:

    clock.tick(fps)
    #Placing variable on display
    screen.blit(background,(0, 0))
    world.draw()

    player.update()
    
    #draw_grid()
    #ADDING WAY TO CLOSE GAME
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()
pygame.quit()