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
TTScore = "0"
InputX =0
InputY =0

font = pygame.font.SysFont(None, 24)


Total = font.render("Total Score:", True, (255,255,255)) 
TotalScore = font.render(TTScore, True, (255,255,255)) 



game_over = False
pygame.key.set_repeat(5,10)
clock = pygame.time.Clock()

overlay = pygame.surface.Surface((1400,800))
# Make a 2D array with tuples for xy and xy2.
# For loop draw all the lines draw them

outsideBarrier = [[[50,50],[1000,50]],[[1000,50],[1300,200]],[[1300,200],[1380,350]],[[1380,350],[1390,450]],[[1390,450],[1360,550]],[[1360,550],[1300,600]] 
,[[1300,600],[1200,650]],[[1200,650],[1100,700]],[[1100,700],[50,750]],[[50,750],[50,50]]]

insideBarrier = [[[200,200],[1000,200]],[[1000,200],[1200,300]],[[1200,300],[1200,475]],[[1200,475],[1100,550]],[[1100,550],[200,625]],[[200,625],[200,200]] ]

goalLines = [[[200,200],[200,50]],[[400,200],[400,50]],[[600,200],[600,50]],[[800,200],[800,50]],[[1000,200],[1000,50]],[[1200,300],[1200,150]],[[1200,400],[1385,400]]
,[[1100,550],[1360,550]],[[900,570],[900,710]],[[700,585],[700,720]],[[500,600],[500,730]],[[300,620],[300,740]],[[200,625],[50,750]],[[200,550],[50,550]],[[200,350],[50,350]] ]

def drawGoalLines():
    for line in goalLines :
        pygame.draw.line(overlay, (0,255,0), line[0] , line[1], 3)
    pygame.draw.line(overlay, (255,150,0), (200,200) , (50,200))


def drawTrack():
    for outsideWall in outsideBarrier :
        pygame.draw.line(overlay, (255,255,255), outsideWall[0] , outsideWall[1], 3)
    for insideWall in insideBarrier :
        pygame.draw.line(overlay, (255,255,255), insideWall[0] , insideWall[1], 3)


drawGoalLines()
drawTrack()
#16ms = about 60 fps ( to get formula is 1 / fps amount * 1000)
pygame.time.set_timer(1, 16)
pygame.time.set_timer(2, 1000)

def lerp (starting, destination, tic_time):
    return (float(1) - tic_time) * starting + tic_time * destination

def reset() :
    global Player_X 
    global Player_Y 
    global InputX 
    global InputY
    global goalLines
    global TTScore

    goalLines = [[[200,200],[200,50]],[[400,200],[400,50]],[[600,200],[600,50]],[[800,200],[800,50]],[[1000,200],[1000,50]],[[1200,300],[1200,150]],[[1200,400],[1385,400]]
,[[1100,550],[1360,550]],[[900,570],[900,710]],[[700,585],[700,720]],[[500,600],[500,730]],[[300,620],[300,740]],[[200,625],[50,750]],[[200,550],[50,550]],[[200,350],[50,350]] ]
    
    InputX = 0
    InputY = 0
    TTScore = "0"
    Player_X = 100
    Player_Y = 100
    drawGoalLines()

def update():
    clock.tick()
    fps = clock.get_fps() +1
    delta = 1 / fps
    global InputX
    global InputY
    global Player_X
    global Player_Y
    global TTScore
    

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

    TotalScore = font.render(TTScore, True, (255,255,255)) 

    Player_X += VelocityX * speed * delta
    Player_Y += VelocityY * speed * delta
    screen.fill((0,0,0))
    screen.blit(overlay, (0,0))
    screen.blit(Total , (1100,50))
    screen.blit(TotalScore, (1250,50))

    player = pygame.draw.rect(screen, Player_Color, (int(Player_X), int(Player_Y), Player_Size, Player_Size))

    for line in goalLines :
        if player.clipline(line[0], line[1]):
            del goalLines[0]
            overlay.fill((0,0,0))
            TTScore = str(int(TTScore) + 30)
            drawGoalLines()
            drawTrack()

    for outsideWall in outsideBarrier :
        if player.clipline(outsideWall[0], outsideWall[1]):
            reset()

    for insideWall in insideBarrier :
        if player.clipline(insideWall[0], insideWall[1]):
            reset()

    if player.clipline((200,200) , (50,200)) :
        if goalLines.count == 0 :
            reset()
        else :
            reset()


    pygame.display.update()


while not game_over:
    for event in pygame.event.get():
        if event.type == 1:
            update()
        if event.type == 2:
             TTScore = str(int(TTScore) - 10)
        if event.type == pygame.QUIT:
            sys.exit()
      
        

