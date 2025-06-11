import random
import pygame
import time

WIDTH = 400
HEIGHT = 500

pygame.init()

#setup display for game with height and width
screen = pygame.display.set_mode((WIDTH,HEIGHT))

def process_input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def update(dt):
    #this updates the games variables
    pass
def render():
    #this renders the game on screen
    pass

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