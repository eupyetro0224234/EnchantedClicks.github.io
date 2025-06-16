import pygame
import sys
from button import Button
from background import draw_background
import storage  # módulo para salvar/carregar dados criptografados

pygame.init()
screen = pygame.display.set_mode((500, 600))
pygame.display.set_caption("Enchanted Clicks")
clock = pygame.time.Clock()

font = pygame.font.SysFont("arial", 32)
small_font = pygame.font.SysFont("arial", 20)

score, click_power, upgrade_cost = storage.load_data()  # carrega score, upgrades e custo

upgrade_button = pygame.Rect(150, 450, 200, 50)

button = Button(center=(250, 300))

middle_pressed = False  # flag para controle do clique do meio

running = True
while running:
    dt = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 2 and button.rect.collidepoint(event.pos):
                score += click_power
                storage.save_data(score, click_power, upgrade_cost)
                button.start_click_animation()
                middle_pressed = True

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 2:
                middle_pressed = False

            elif button.rect.collidepoint(event.pos):
                if event.button in (1, 3):
                    score += click_power
                    storage.save_data(score, click_power, upgrade_cost)
                button.start_click_animation()

            elif upgrade_button.collidepoint(event.pos):
                if score >= upgrade_cost:
                    score -= upgrade_cost
                    click_power += 1
                    upgrade_cost = int(upgrade_cost * 1.5)
                    storage.save_data(score, click_power, upgrade_cost)

        elif event.type == pygame.MOUSEWHEEL:
            if event.y > 0:
                score += event.y * click_power
                storage.save_data(score, click_power, upgrade_cost)

    button.update(dt)

    draw_background(screen)

    score_text = font.render(f"Pontos: {score}", True, (0, 0, 0))
    screen.blit(score_text, (250 - score_text.get_width() // 2, 100))

    button.draw(screen)

    pygame.draw.rect(screen, (0, 100, 200), upgrade_button, border_radius=10)
    upgrade_txt = small_font.render(f"Upgrade ({upgrade_cost})", True, (255, 255, 255))
    screen.blit(upgrade_txt, (upgrade_button.x + 35, upgrade_button.y + 15))

    pygame.display.flip()

pygame.quit()
sys.exit()
