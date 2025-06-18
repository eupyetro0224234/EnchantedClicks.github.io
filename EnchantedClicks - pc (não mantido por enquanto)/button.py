import pygame
import os

class Button:
    def __init__(self, center):
        self.frames = []
        self.load_frames()
        self.current_frame = 0
        self.rect = self.frames[0].get_rect(center=center)
        self.animating = False
        self.animation_speed = 0.1  # segundos por frame
        self.time_accumulator = 0
        self.scale = 1.0
        self.shrink_scale = 0.9
        self.shrink_duration = 200
        self.shrink_elapsed = 0
        self.shrinking = False

    def load_frames(self):
        assets_dir = os.path.join(os.getenv('LOCALAPPDATA'), "assets.enchantedclicks")
        i = 0
        while True:
            path = os.path.join(assets_dir, f"botao_{i}.png")
            if not os.path.exists(path):
                break
            image = pygame.image.load(path).convert_alpha()
            self.frames.append(image)
            i += 1
        
        if not self.frames:
            surf = pygame.Surface((150, 150), pygame.SRCALPHA)
            pygame.draw.rect(surf, (0, 200, 0), surf.get_rect(), border_radius=20)
            self.frames = [surf]

    def start(self):
        self.animating = True
        self.current_frame = 0
        self.time_accumulator = 0
        self.shrinking = True
        self.shrink_elapsed = 0

    def update(self, dt):
        if self.animating:
            self.time_accumulator += dt / 1000
            if self.time_accumulator >= self.animation_speed:
                self.time_accumulator = 0
                self.current_frame += 1
                if self.current_frame >= len(self.frames):
                    self.current_frame = 0
                    self.animating = False

        if self.shrinking:
            self.shrink_elapsed += dt
            if self.shrink_elapsed <= self.shrink_duration:
                progress = self.shrink_elapsed / self.shrink_duration
                if progress <= 0.5:
                    self.scale = 1.0 - (1.0 - self.shrink_scale) * (progress / 0.5)
                else:
                    self.scale = self.shrink_scale + (1.0 - self.shrink_scale) * ((progress - 0.5) / 0.5)
            else:
                self.scale = 1.0
                self.shrinking = False

    def draw(self, surface):
        image = self.frames[self.current_frame]
        size = image.get_size()
        scaled_size = (int(size[0] * self.scale), int(size[1] * self.scale))
        scaled_image = pygame.transform.smoothscale(image, scaled_size)
        rect = scaled_image.get_rect(center=self.rect.center)
        surface.blit(scaled_image, rect)
