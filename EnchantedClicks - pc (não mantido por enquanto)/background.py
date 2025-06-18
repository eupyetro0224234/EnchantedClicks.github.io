import pygame
import math

# Cores base para o degradê animado
colors = [
    (0, 255, 255),      # Ciano
    (255, 255, 255),    # Branco
    (144, 238, 144),    # Verde claro
    (173, 216, 230)     # Azul claro
]

tile_size = 40  # tamanho dos quadradinhos

def lerp_color(color1, color2, t):
    """Interpola duas cores com base em t (0 a 1)."""
    return tuple(
        int(c1 + (c2 - c1) * t)
        for c1, c2 in zip(color1, color2)
    )

def draw_background(surface):
    width, height = surface.get_size()
    time = pygame.time.get_ticks() / 1000  # segundos

    for y in range(0, height, tile_size):
        for x in range(0, width, tile_size):
            index = ((x + y) // tile_size) % len(colors)
            color1 = colors[index]
            color2 = colors[(index + 1) % len(colors)]

            # t oscilando de 0 a 1 com o tempo, deslocado por posição
            t = (math.sin(time + (x + y) * 0.05) + 1) / 2
            color = lerp_color(color1, color2, t)

            pygame.draw.rect(surface, color, (x, y, tile_size, tile_size))
