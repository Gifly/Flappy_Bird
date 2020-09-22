import pygame, sys

def draw_floor():
    screen.blit(floor_surface, (floor_x_pos,700))
    screen.blit(floor_surface, (floor_x_pos + 576, 700))

pygame.init()
screen = pygame.display.set_mode((576,800)) #Display Surface
clock = pygame.time.Clock()

bg_surface = pygame.image.load('flappy-bird-assets/sprites/background-day.png').convert()
bg_surface = pygame.transform.scale2x(bg_surface)

floor_surface = pygame.image.load('flappy-bird-assets/sprites/base.png').convert()
floor_surface = pygame.transform.scale2x(floor_surface)
floor_x_pos = 0

#Main Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(bg_surface,(0,0))
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= -576:
        floor_x_pos = 0
    screen.blit(floor_surface,(floor_x_pos,700))

    pygame.display.update()
    clock.tick(120)

pygame.quit()