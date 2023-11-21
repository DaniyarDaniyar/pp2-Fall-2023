import pygame
import sys
from datetime import datetime

pygame.init()

width, height = 1000, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mickey Clock")

mickey_body = pygame.image.load("main-clock.png")  
mickey_hand_left = pygame.image.load("left-hand.png")  
mickey_hand_right = pygame.image.load("right-hand.png")  

clock = pygame.time.Clock()
running = True

def draw_clock(seconds_angle, minutes_angle):
    screen.fill((255, 255, 255))

    
    screen.blit(mickey_body, (width // 2 - mickey_body.get_width() // 2, height // 2 - mickey_body.get_height() // 2))

    
    hand_left_rotated = pygame.transform.rotate(mickey_hand_left, seconds_angle)
    hand_right_rotated = pygame.transform.rotate(mickey_hand_right, minutes_angle)

    screen.blit(hand_left_rotated, (width // 2 - hand_left_rotated.get_width() // 2, height // 2 - hand_left_rotated.get_height() // 2))
    screen.blit(hand_right_rotated, (width // 2 - hand_right_rotated.get_width() // 2, height // 2 - hand_right_rotated.get_height() // 2))

    pygame.display.flip()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    current_time = datetime.now().time()
    seconds = current_time.second
    minutes = current_time.minute

    
    seconds_angle = -seconds * 6  
    minutes_angle = -minutes * 6  

    draw_clock(seconds_angle, minutes_angle)

    clock.tick(1)  

pygame.quit()
sys.exit()
