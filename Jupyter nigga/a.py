import pygame 
import time
import math

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
pygame.display.set_caption("Mickeyclock")
left = pygame.image.load("left.png")
right = pygame.image.load("right.png")
mainclock = pygame.transform.scale(pygame.image.load("mickeyclock.png"), (800, 600))
while 1>0: 
    current_time = time.localtime()
    min = current_time.tm_min
    sec = current_time.tm_sec
    
    minute_angle=min* 6+(sec/ 60)*6   
    second_angle=sec* 6
    screen.blit(mainclock, (0,0))
    
    rotated_rightarm = pygame.transform.rotate(pygame.transform.scale(right, (800, 600)), -minute_angle)
    rightarmrect = rotated_rightarm.get_rect(center=(800 // 2, 600 // 2 + 12))
    screen.blit(rotated_rightarm, rightarmrect)
    rotated_leftarm = pygame.transform.rotate(pygame.transform.scale(left, (40.95, 682.5)), -second_angle)
    leftarmrect = rotated_leftarm.get_rect(center=(800 // 2, 600 // 2 + 10))
    screen.blit(rotated_leftarm, leftarmrect)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()