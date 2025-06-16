import pygame
import sys
import random

from button import Button
from background import draw_background
import storage
import assets

pygame.init()
screen = pygame.display.set_mode((500, 600))
pygame.display.set_caption("Enchanted Clicks")
clock = pygame.time.Clock()

font = pygame.font.SysFont("arial", 32)
small_font = pygame.font.SysFont("arial", 20)

lazuli_icon = assets.get_lazuli_icon()

score, click_power, upgrade_cost, lazuli = storage.load_data()

upgrade_button = pygame.Rect(150, 450, 200, 50)
button = Button(center=(250, 300))

mouse_buttons_pressed = set()

# Variável para controle de escolha de pagamento (None = não em escolha)
choose_payment = None  # pode ser "points" ou "lazuli"
pending_upgrade = False

def draw_payment_choice():
    # Fundo semitransparente
    s = pygame.Surface((500, 600))
    s.set_alpha(200)
    s.fill((200, 200, 200))
    screen.blit(s, (0, 0))
    # Caixa
    box_rect = pygame.Rect(100, 200, 300, 200)
    pygame.draw.rect(screen, (50, 50, 50), box_rect, border_radius=10)
    pygame.draw.rect(screen, (255, 255, 255), box_rect, 3, border_radius=10)

    text1 = font.render("Escolha o recurso para pagar:", True, (255, 255, 255))
    screen.blit(text1, (120, 220))

    # Botões de escolha
    points_rect = pygame.Rect(130, 320, 100, 50)
    lazuli_rect = pygame.Rect(270, 320, 100, 50)
    pygame.draw.rect(screen, (0, 100, 200), points_rect, border_radius=8)
    pygame.draw.rect(screen, (0, 150, 100), lazuli_rect, border_radius=8)

    text_points = small_font.render(f"Pontos ({upgrade_cost})", True, (255, 255, 255))
    text_lazuli = small_font.render(f"Lápis ({10 * (click_power)})", True, (255, 255, 255))

    screen.blit(text_points, (points_rect.x + 5, points_rect.y + 15))
    screen.blit(text_lazuli, (lazuli_rect.x + 10, lazuli_rect.y + 15))

    return points_rect, lazuli_rect

running = True
while running:
    dt = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if choose_payment is None:
            # Não está no prompt de escolha
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_buttons_pressed.add(event.button)

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button in mouse_buttons_pressed:
                    mouse_buttons_pressed.remove(event.button)

                buttons_held = mouse_buttons_pressed | {event.button}

                if button.rect.collidepoint(event.pos):
                    points = 0
                    if 1 in buttons_held and 3 in buttons_held:
                        points = 2 * click_power
                    elif any(b in buttons_held for b in (1, 2, 3)):
                        points = 1 * click_power

                    if points > 0:
                        score += points
                        if random.random() < 0.25:
                            lazuli += 1
                        storage.save_data(score, click_power, upgrade_cost, lazuli)
                        button.start()

                elif upgrade_button.collidepoint(event.pos):
                    lazuli_cost = 10 * (click_power)  # upgrade 1 custa 10 lápis, upgrade 2 custa 20, etc

                    # Verifica recursos disponíveis
                    has_points = score >= upgrade_cost
                    has_lazuli = lazuli >= lazuli_cost

                    if has_points and has_lazuli:
                        # Pedir escolha para o jogador
                        choose_payment = True
                        pending_upgrade = True

                    elif has_points:
                        # Compra automática com pontos
                        score -= upgrade_cost
                        click_power += 1
                        upgrade_cost = 1000 * (click_power)  # próximo upgrade
                        storage.save_data(score, click_power, upgrade_cost, lazuli)

                    elif has_lazuli:
                        # Compra automática com lápis
                        lazuli -= lazuli_cost
                        click_power += 1
                        upgrade_cost = 1000 * (click_power)
                        storage.save_data(score, click_power, upgrade_cost, lazuli)

                elif event.type == pygame.MOUSEWHEEL:
                    if event.y > 0:
                        score += event.y * click_power
                        storage.save_data(score, click_power, upgrade_cost, lazuli)

        else:
            # Está na tela de escolha de pagamento
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_buttons_pressed.add(event.button)

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button in mouse_buttons_pressed:
                    mouse_buttons_pressed.remove(event.button)

                if event.button == 1:  # clique esquerdo para escolher
                    mouse_pos = event.pos
                    points_rect, lazuli_rect = draw_payment_choice()

                    if points_rect.collidepoint(mouse_pos):
                        # Usar pontos
                        score -= upgrade_cost
                        click_power += 1
                        upgrade_cost = 1000 * (click_power)
                        storage.save_data(score, click_power, upgrade_cost, lazuli)
                        choose_payment = None
                        pending_upgrade = False

                    elif lazuli_rect.collidepoint(mouse_pos):
                        # Usar lápis
                        lazuli_cost = 10 * (click_power)
                        lazuli -= lazuli_cost
                        click_power += 1
                        upgrade_cost = 1000 * (click_power)
                        storage.save_data(score, click_power, upgrade_cost, lazuli)
                        choose_payment = None
                        pending_upgrade = False

    draw_background(screen)

    text_score = font.render(f"Pontos: {score}", True, (0, 0, 0))
    screen.blit(text_score, ((500 - text_score.get_width()) // 2, 20))

    button.update(dt)
    button.draw(screen)

    lazuli_cost = 10 * (click_power)

    pygame.draw.rect(screen, (0, 100, 200), upgrade_button, border_radius=10)
    text_encantar = small_font.render("Encantar", True, (255, 255, 255))
    screen.blit(text_encantar, (upgrade_button.x + 55, upgrade_button.y + 10))

    requisito_text = f"Requer: {upgrade_cost} pontos ou {lazuli_cost} lápis-lazúli"
    text_requisito = small_font.render(requisito_text, True, (0, 0, 0))
    screen.blit(text_requisito, (upgrade_button.x, upgrade_button.y + 50))

    text_fortuna = small_font.render(f"Atual: Fortuna {click_power}", True, (0, 0, 0))
    screen.blit(text_fortuna, (upgrade_button.x, upgrade_button.y + 70))

    lazuli_icon_scaled = pygame.transform.smoothscale(lazuli_icon, (32, 32))
    screen.blit(lazuli_icon_scaled, (450, 10))
    count_text = small_font.render(f"{lazuli}", True, (0, 0, 0))
    screen.blit(count_text, (450 - count_text.get_width(), 50))

    if choose_payment:
        draw_payment_choice()

    pygame.display.flip()

pygame.quit()
sys.exit()
