import pygame
import sys

pygame.init()
game_size = (1400, 800)

Player_Color = [0,255,0]
Player_X = 400
Player_Y = 400
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

#16ms = about 60 fps ( to get formula is 1 / fps amount * 1000)
pygame.time.set_timer(1, 16)

def lerp (starting, destination, tic_time):
    return (float(1) - tic_time) * starting + tic_time * destination

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
    print(clock.get_fps())
    screen.fill((0,0,0))
    pygame.draw.rect(screen, Player_Color, (int(Player_X), int(Player_Y), Player_Size, Player_Size))
    pygame.display.update()



while not game_over:
    for event in pygame.event.get():
        if event.type == 1:
            update()
        if event.type == pygame.QUIT:
            sys.exit()
      
        

