import os
import urllib.request
from PIL import Image, ImageSequence

ASSETS_DIR = os.path.join(os.getenv('LOCALAPPDATA'), "assets.enchantedclicks")
os.makedirs(ASSETS_DIR, exist_ok=True)

BOTAO_GIF_URL = "https://s14.gifyu.com/images/bHSgv.gif"
BOTAO_GIF_PATH = os.path.join(ASSETS_DIR, "botao.gif")

def download_botao_gif():
    if not os.path.exists(BOTAO_GIF_PATH):
        print("Baixando gif do botão...")
        urllib.request.urlretrieve(BOTAO_GIF_URL, BOTAO_GIF_PATH)
        print("Download concluído.")
        extract_frames_from_gif(BOTAO_GIF_PATH)

def extract_frames_from_gif(gif_path):
    print("Extraindo frames do gif...")
    gif = Image.open(gif_path)
    for i, frame in enumerate(ImageSequence.Iterator(gif)):
        frame = frame.convert("RGBA")
        frame_path = os.path.join(ASSETS_DIR, f"botao_{i}.png")
        frame.save(frame_path)
    print("Frames extraídos.")

def get_lazuli_icon():
    icon_path = os.path.join(ASSETS_DIR, "lazuli.png")
    if not os.path.exists(icon_path):
        url = "https://i.postimg.cc/NMvTm37Y/image.png"
        print("Baixando ícone do lápis-lazúli...")
        urllib.request.urlretrieve(url, icon_path)
        print("Download ícone concluído.")
    import pygame
    return pygame.image.load(icon_path).convert_alpha()

# Chamada inicial para garantir que o gif do botão está baixado e frames criados
download_botao_gif()
