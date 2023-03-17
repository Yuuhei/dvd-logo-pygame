import pygame
import random

pygame.init()
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Bouncing DVD Logo to trigger your anxiety')

dvd_logo_orig = pygame.image.load('dvd.png')
dvd_logo = pygame.transform.scale(dvd_logo_orig, (128, 73))
dvd_logo_rect = dvd_logo.get_rect()
dvd_logo_pos = [WINDOW_WIDTH // 2 - dvd_logo_rect.width // 2, WINDOW_HEIGHT // 2 - dvd_logo_rect.height // 2]
dvd_logo_speed = [2, 2]
dvd_logo_color = (255, 255, 255)

clock = pygame.time.Clock()

while True:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    dvd_logo_pos[0] += dvd_logo_speed[0]
    dvd_logo_pos[1] += dvd_logo_speed[1]

    if dvd_logo_pos[0] + dvd_logo_rect.width >= WINDOW_WIDTH or dvd_logo_pos[0] <= 0:
        dvd_logo_speed[0] = -dvd_logo_speed[0]
        dvd_logo_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    if dvd_logo_pos[1] + dvd_logo_rect.height >= WINDOW_HEIGHT or dvd_logo_pos[1] <= 0:
        dvd_logo_speed[1] = -dvd_logo_speed[1]
        dvd_logo_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    window.fill((0, 0, 0))

    dvd_logo_surface = dvd_logo.copy()
    dvd_logo_surface.fill(dvd_logo_color, special_flags=pygame.BLEND_RGB_MULT)
    window.blit(dvd_logo_surface, dvd_logo_pos)

    pygame.display.update()

    clock.tick(60)
