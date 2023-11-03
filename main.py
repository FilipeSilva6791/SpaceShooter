import pygame
from pygame import Surface, Rect

WINDOW_WIDTH = 576
WINDOW_HEIGHT = 324

# Initialize PyGame module
pygame.init()

# Create a new window
window: Surface = pygame.display.set_mode(size=(WINDOW_WIDTH, WINDOW_HEIGHT))

# Load images
bg_surf: Surface = pygame.image.load('Images/Background.png').convert_alpha()
player1_surf: Surface = pygame.image.load('./Images/Player1.png').convert_alpha()

# Get rectangles of surfaces
bg_rect: Rect = bg_surf.get_rect(left=0, top=0)
player1_rect: Rect = player1_surf.get_rect(left=100, top=100)

# Draw images
window.blit(source=bg_surf, dest=bg_rect)
window.blit(source=player1_surf, dest=player1_rect)

# Update window
pygame.display.flip()

#
clock = pygame.time.Clock()

#
pygame.mixer_music.load('Sounds/Phase1.mp3')
pygame.mixer_music.play(-1)
pygame.mixer_music.set_volume(0.5)

while True:
    clock.tick(180)

    window.blit(source=bg_surf, dest=bg_rect)
    window.blit(source=player1_surf, dest=player1_rect)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            pygame.quit()
            quit()

    pressed_key = pygame.key.get_pressed()

    if pressed_key[pygame.K_w]:
        player1_rect.centery -= 1
    if pressed_key[pygame.K_s]:
        player1_rect.centery += 1
    if pressed_key[pygame.K_a]:
        player1_rect.centerx -= 1
    if pressed_key[pygame.K_d]:
        player1_rect.centerx += 1
