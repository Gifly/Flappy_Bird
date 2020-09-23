import pygame, sys, random

def draw_floor():
    screen.blit(floor_surface, (floor_x_pos,700))
    screen.blit(floor_surface, (floor_x_pos + 576, 700))

def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop = ( 700, random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midbottom = ( 700, random_pipe_pos - 300))
    return bottom_pipe, top_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes

def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 700:
            screen.blit(pipe_surface,pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface,False, True)
            screen.blit(flip_pipe, pipe)
pygame.init()
screen = pygame.display.set_mode((576,800)) #Display Surface
clock = pygame.time.Clock()

# Game Variables
gravity = 0.25
bird_movement = 0


bg_surface = pygame.image.load('flappy-bird-assets/sprites/background-day.png').convert()
bg_surface = pygame.transform.scale2x(bg_surface)

floor_surface = pygame.image.load('flappy-bird-assets/sprites/base.png').convert()
floor_surface = pygame.transform.scale2x(floor_surface)
floor_x_pos = 0

bird_surface = pygame.image.load('flappy-bird-assets/sprites/bluebird-midflap.png').convert()
bird_surface = pygame.transform.scale2x(bird_surface)
bird_rect = bird_surface.get_rect(center = (100,350))

pipe_surface = pygame.image.load('flappy-bird-assets/sprites/pipe-green.png').convert()
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)
pipe_height = [350,450,600]

#Main Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key ==pygame.K_SPACE:
                bird_movement = 0
                bird_movement -= 12
        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())
            
    screen.blit(bg_surface,(0,0))

    #Bird 
    bird_movement += gravity
    bird_rect.centery += bird_movement
    screen.blit(bird_surface,bird_rect)

    #Pipes
    pipe_list = move_pipes(pipe_list)
    draw_pipes(pipe_list)

    #Floor
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= -576:
        floor_x_pos = 0
    screen.blit(floor_surface,(floor_x_pos,700))

    pygame.display.update()
    clock.tick(120)

pygame.quit()