import pygame
import sys

pygame.init()
game_size = (1400, 800)

Player_Color = [0,255,0]
Player_X = 100
Player_Y = 100
Player_Size = 50
speed = 4
acceleration = 4
VelocityX = 0
VelocityY = 0
screen = pygame.display.set_mode(game_size)

InputX =0
InputY =0

game_over = False
pygame.key.set_repeat(5,10)
clock = pygame.time.Clock()

overlay = pygame.surface.Surface((1400,800))
# Make a 2D array with tuples for xy and xy2.
# For loop draw all the lines draw them

outsideBarrier = [[[50,50],[1000,50]],[[1000,50],[1300,200]],[[1300,200],[1380,350]],[[1380,350],[1390,450]],[[1390,450],[1360,550]],[[1360,550],[1300,600]] 
,[[1300,600],[1200,650]],[[1200,650],[1100,700]],[[1100,700],[50,750]],[[50,750],[50,50]]]

insideBarrier = [[[200,200],[1000,200]],[[1000,200],[1200,300]],[[1200,300],[1200,475]],[[1200,475],[1100,550]],[[1100,550],[200,625]],[[200,625],[200,200]] ]

for outsideWall in outsideBarrier :
     pygame.draw.line(overlay, (255,255,255), outsideWall[0] , outsideWall[1], 3)
for insideWall in insideBarrier :
     pygame.draw.line(overlay, (255,255,255), insideWall[0] , insideWall[1], 3)


pygame.display.update()
#16ms = about 60 fps ( to get formula is 1 / fps amount * 1000)
pygame.time.set_timer(1, 16)

def lerp (starting, destination, tic_time):
    return (float(1) - tic_time) * starting + tic_time * destination

def reset() :
    global Player_X 
    global Player_Y 
    global InputX 
    global InputY

    InputX = 0
    InputY = 0
    Player_X = 100
    Player_Y = 100


def update():
    clock.tick()
    fps = clock.get_fps() +1
    delta = 1 / fps
    global InputX
    global InputY
    global Player_X
    global Player_Y

    

    keys = pygame.key.get_pressed()

    if event.type == pygame.QUIT:
        sys.exit()

    if keys[pygame.K_LEFT]:
        InputX -= 1
    if keys[pygame.K_RIGHT]:
        InputX += 1 
    if keys[pygame.K_UP]:
        InputY -= 1 
    if keys[pygame.K_DOWN]:
        InputY += 1

    VelocityX = InputX
    VelocityY = InputY

    

    Player_X += VelocityX * speed * delta
    Player_Y += VelocityY * speed * delta
    screen.fill((0,0,0))
    screen.blit(overlay, (0,0))
    player = pygame.draw.rect(screen, Player_Color, (int(Player_X), int(Player_Y), Player_Size, Player_Size))

    for outsideWall in outsideBarrier :
        if player.clipline(outsideWall[0], outsideWall[1]):
            reset()

    for insideWall in insideBarrier :
        if player.clipline(insideWall[0], insideWall[1]):
            reset()



    pygame.display.update()



while not game_over:
    for event in pygame.event.get():
        if event.type == 1:
            update()
        if event.type == pygame.QUIT:
            sys.exit()
      
        

