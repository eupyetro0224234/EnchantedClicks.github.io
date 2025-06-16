import pygame
import os
import urllib.request
from PIL import Image, ImageSequence

class Button:
    def __init__(self, center):
        self.center = center
        self.anim_duration = 200  # ms animação clique
        self.anim_time = 0
        self.animating = False

        # Pasta e arquivo para salvar gif
        appdata = os.getenv('LOCALAPPDATA')
        asset_folder = os.path.join(appdata, "assets.enchantedclicks")
        os.makedirs(asset_folder, exist_ok=True)
        self.image_path = os.path.join(asset_folder, "botao.gif")

        gif_url = "https://s14.gifyu.com/images/bHSgv.gif"
        if not os.path.exists(self.image_path):
            with urllib.request.urlopen(gif_url) as response:
                gif_data = response.read()
                with open(self.image_path, 'wb') as f:
                    f.write(gif_data)

        self.frames = []
        self.durations = []

        pil_image = Image.open(self.image_path)
        for frame in ImageSequence.Iterator(pil_image):
            frame = frame.convert("RGBA")
            mode = frame.mode
            size = frame.size
            data = frame.tobytes()
            surface = pygame.image.fromstring(data, size, mode)
            self.frames.append(surface)
            self.durations.append(frame.info.get("duration", 100))

        self.current_frame = 0
        self.frame_time = 0

        self.scale_min = 0.9

        self.rect = self.frames[0].get_rect(center=self.center)

    def update(self, dt):
        self.frame_time += dt
        if self.frame_time >= self.durations[self.current_frame]:
            self.frame_time = 0
            self.current_frame = (self.current_frame + 1) % len(self.frames)

        if self.animating:
            self.anim_time += dt
            if self.anim_time >= self.anim_duration:
                self.animating = False

    def start_click_animation(self):
        self.animating = True
        self.anim_time = 0

    def draw(self, surface):
        frame_surf = self.frames[self.current_frame]

        if self.animating:
            progress = self.anim_time / self.anim_duration
            if progress > 1:
                progress = 1

            # Animação suave: diminui até scale_min, depois volta ao normal
            if progress <= 0.5:
                scale = 1 - (1 - self.scale_min) * (progress / 0.5)
            else:
                scale = self.scale_min + (1 - self.scale_min) * ((progress - 0.5) / 0.5)

            w, h = frame_surf.get_size()
            scaled_w = int(w * scale)
            scaled_h = int(h * scale)
            scaled_surf = pygame.transform.smoothscale(frame_surf, (scaled_w, scaled_h))
            rect = scaled_surf.get_rect(center=self.center)
            surface.blit(scaled_surf, rect)
        else:
            surface.blit(frame_surf, self.rect)
