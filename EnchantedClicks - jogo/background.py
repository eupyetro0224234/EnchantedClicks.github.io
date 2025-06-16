import pygame

def draw_background(screen):
    tile_size = 15
    colors = [
        (0, 255, 255),      # ciano
        (255, 255, 255),    # branco
        (144, 238, 144),    # verde claro
        (173, 216, 230)     # azul claro
    ]
    for y in range(0, screen.get_height(), tile_size):
        for x in range(0, screen.get_width(), tile_size):
            color_index = ((x // tile_size) + (y // tile_size)) % len(colors)
            pygame.draw.rect(screen, colors[color_index], (x, y, tile_size, tile_size))
