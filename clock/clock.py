import pygame
import datetime

pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")
clock = pygame.time.Clock()

clock_bg = pygame.image.load("back.png")
minute_hand = pygame.image.load("min_hand.png")
second_hand = pygame.image.load("sec_hand.png")

clock_rect = clock_bg.get_rect(center=(WIDTH//2, HEIGHT//2))
minute_origin = (WIDTH//2, HEIGHT//2)
second_origin = (WIDTH//2, HEIGHT//2)

running = True
while running:
    screen.fill((255, 255, 255))
    now = datetime.datetime.now()
    minutes_angle = -(now.minute * 6 + now.second * 0.1)
    seconds_angle = -(now.second * 6)
    screen.blit(clock_bg, clock_rect)
    rotated_minute = pygame.transform.rotate(minute_hand, minutes_angle)
    rotated_second = pygame.transform.rotate(second_hand, seconds_angle)
    minute_rect = rotated_minute.get_rect(center=minute_origin)
    second_rect = rotated_second.get_rect(center=second_origin)
    screen.blit(rotated_minute, minute_rect)
    screen.blit(rotated_second, second_rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
