import pygame

pygame.init()
WIDTH, HEIGHT = 1024, 768
BALL_RADIUS = 25
BALL_SPEED = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")

ball_x, ball_y = WIDTH // 2, HEIGHT // 2
running = True
clock = pygame.time.Clock()

while running:
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (ball_x, ball_y), BALL_RADIUS)
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and ball_y - BALL_RADIUS - BALL_SPEED >= 0:
        ball_y -= BALL_SPEED
    if keys[pygame.K_DOWN] and ball_y + BALL_RADIUS + BALL_SPEED <= HEIGHT:
        ball_y += BALL_SPEED
    if keys[pygame.K_LEFT] and ball_x - BALL_RADIUS - BALL_SPEED >= 0:
        ball_x -= BALL_SPEED
    if keys[pygame.K_RIGHT] and ball_x + BALL_RADIUS + BALL_SPEED <= WIDTH:
        ball_x += BALL_SPEED
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.update()
    clock.tick(30)
pygame.quit()
