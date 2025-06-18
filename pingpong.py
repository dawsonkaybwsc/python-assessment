import random
import pygame
import time

WIDTH = 400
HEIGHT = 500

pygame.init()

#setup display for game with height and width
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Pingpong")

block_color = (255, 255, 255)
block_x = 5
block_y = 150
block_width = 150
block_height = 10

block1_x = 5
block1_y = 150
block1_width = 150
block1_height = 390

block2_x = 5
block2_y = 5
block2_width = 200
block2_height = 200



def process_input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def update(dt):
    #this updates the games variables
    pass
def render():
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, block_color, (block_height, block_width, block_x, block_y))
    pygame.draw.rect(screen, block_color, (block1_height, block1_width, block1_x, block1_y))
    pygame.draw.rect(screen, block_color, (block2_height, block2_width, block2_x, block2_y))
    pygame.display.flip()

running = True
last_frame_time = time.time()

#calculates the delta time
while running:
    current_time = time.time()
    dt = current_time - last_frame_time
    last_frame_time = current_time

    running = process_input() 
    update(dt)
    render()


running = False