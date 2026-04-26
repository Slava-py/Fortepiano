import pygame
from settings import BLACK

def draw_key_effect(screen, rect, is_pressed=False, press_anim=0.0):

    normal_color = pygame.Color(220, 220, 220)
    pressed_color = pygame.Color(170, 220, 255)

    color = normal_color.lerp(pressed_color, press_anim)

    offset_y = int(press_anim * 4)
    animated_rect = rect.move(0, offset_y)

    shadow_rect = rect.move(0, 4)
    pygame.draw.rect(screen, (180, 180, 180), shadow_rect, border_radius=8)

    pygame.draw.rect(screen, color, animated_rect, border_radius=8)

    pygame.draw.rect(screen, BLACK, animated_rect, 2, border_radius=8)