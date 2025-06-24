import random
import pygame
import time

WIDTH = 400
HEIGHT = 500

pygame.init()

#setup display for game with height and width
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Pingpong")

#left bar
block_width = 10
block_height = 100
block_x = 20
block_y = HEIGHT // 2 - block_height // 2
block_speed = 0.15

#right bar
block1_width = 10
block1_height = 100
block1_x = WIDTH - 30
block1_y = HEIGHT // 2 - block1_height // 2
block1_speed = 0.15

#ball in the middle
block2_size = 15
block2_x = WIDTH // 2
block2_y = HEIGHT // 2
block2_vel_x = 0.08
block2_vel_y = 0.08



def process_input():
    global block_y, block1_y, running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        block_y -= block_speed
    if keys[pygame.K_s]:
        block_y += block_speed
    if keys[pygame.K_i]:
        block1_y -= block1_speed
    if keys[pygame.K_k]:
        block1_y += block1_speed
        

def update(dt):
    #this updates the games variables
    global block2_x, block2_y, block2_vel_x, block2_vel_y

    #moving the ball
    block2_x += block2_vel_x
    block2_y += block2_vel_y

    #makes it so it bounces and doesnt go off screen
    if block2_y <= 0 or block2_y + block2_size >= HEIGHT:
       block2_vel_y *= -1.1

    #bounce off left bar
    if (block_x < block2_x < block_x + block_width) and (block_y < block2_y < block_y + block_height):
        block2_vel_x *= -1.1

    #bounce of right bar
    if (block1_x < block2_x + block2_size < block1_x + block1_width) and (block1_y < block2_y < block1_y + block1_height):
        block2_vel_x *= -1.1

    #resets ball if misses bar and goes off screen and ball size
    if block2_x < 0 or block2_x > WIDTH:
       block2_x = WIDTH // 2
       block2_y = HEIGHT // 2




def render():
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), (block_x, block_y, block_width, block_height))
    pygame.draw.rect(screen, (255, 255, 255), (block1_x, block1_y, block1_width, block1_height))
    pygame.draw.rect(screen, (255, 255, 255), (block2_x, block2_y, block2_size, block2_size))
    pygame.display.flip()

running = True
last_frame_time = time.time()

#calculates the delta time
while running:
    current_time = time.time()
    dt = current_time - last_frame_time
    last_frame_time = current_time

    process_input() 
    update(dt)
    render()


pygame.quit()