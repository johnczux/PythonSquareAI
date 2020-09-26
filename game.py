import pygame
import sys

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

game_over = False
pygame.key.set_repeat(5,10)
clock = pygame.time.Clock()

def lerp (starting, destination, tic_time):
    return (tic_time * starting) + ((float(1) - tic_time) * destination)


while not game_over:
    
    for event in pygame.event.get():
        clock.tick()
      
        fps = clock.get_fps() +1
        delta = 1 / fps
        

        keys = pygame.key.get_pressed()

        if event.type == pygame.QUIT:
            sys.exit()

        if keys[pygame.K_LEFT]:
            Player_X -= 1
        if keys[pygame.K_RIGHT]:
            Player_X += 1 
        if keys[pygame.K_UP]:
           Player_Y -= 1 
        if keys[pygame.K_DOWN]:
            Player_Y += 1

        VelocityX = lerp( VelocityX, Player_X, acceleration * delta)
        VelocityY = lerp( VelocityY, Player_Y, acceleration * delta)

        Player_X += VelocityX * speed * delta
        Player_Y += VelocityY * speed * delta
     
        print(Player_Y)
 
    screen.fill((0,0,0))
    pygame.draw.rect(screen, Player_Color, (int(Player_X), int(Player_Y), Player_Size, Player_Size))
    pygame.display.update()

