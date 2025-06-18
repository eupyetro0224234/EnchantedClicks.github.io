import os

appdata = os.getenv('LOCALAPPDATA')
asset_folder = os.path.join(appdata, "assets.enchantedclicks")
os.makedirs(asset_folder, exist_ok=True)

data_file = os.path.join(asset_folder, "score.dat")

_key = 0x5A  # chave XOR simples

def encrypt_decrypt(data: bytes) -> bytes:
    return bytes([b ^ _key for b in data])

def save_data(score: int, click_power: int, upgrade_cost: int, lazuli: int):
    try:
        combined = f"{score}|{click_power}|{upgrade_cost}|{lazuli}"
        encrypted = encrypt_decrypt(combined.encode('utf-8'))
        with open(data_file, 'wb') as f:
            f.write(encrypted)
    except Exception as e:
        print("Erro ao salvar dados:", e)

def load_data() -> tuple[int,int,int,int]:
    if not os.path.exists(data_file):
        return 0, 1, 50, 0
    try:
        encrypted = open(data_file, 'rb').read()
        decoded = encrypt_decrypt(encrypted).decode('utf-8')
        parts = decoded.split('|')
        return (
            int(parts[0] or 0),
            int(parts[1] or 1),
            int(parts[2] or 50),
            int(parts[3] or 0)
        )
    except Exception as e:
        print("Erro ao carregar dados:", e)
        return 0, 1, 50, 0
