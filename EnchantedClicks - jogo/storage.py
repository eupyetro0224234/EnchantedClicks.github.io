import os

appdata = os.getenv('LOCALAPPDATA')
asset_folder = os.path.join(appdata, "assets.enchantedclicks")
os.makedirs(asset_folder, exist_ok=True)

score_file = os.path.join(asset_folder, "score.dat")

_key = 0x5A  # Chave XOR simples

def encrypt_decrypt(data: bytes) -> bytes:
    return bytes([b ^ _key for b in data])

def save_data(score: int, click_power: int, upgrade_cost: int):
    try:
        combined = f"{score}|{click_power}|{upgrade_cost}"
        data = combined.encode('utf-8')
        encrypted = encrypt_decrypt(data)
        with open(score_file, 'wb') as f:
            f.write(encrypted)
    except Exception as e:
        print("Erro ao salvar dados:", e)

def load_data() -> tuple[int, int, int]:
    if not os.path.exists(score_file):
        return 0, 1, 50  # padrões score=0, click_power=1, upgrade_cost=50
    try:
        with open(score_file, 'rb') as f:
            encrypted = f.read()
        decrypted = encrypt_decrypt(encrypted)
        decoded = decrypted.decode('utf-8')
        parts = decoded.split('|')
        score = int(parts[0]) if len(parts) > 0 else 0
        click_power = int(parts[1]) if len(parts) > 1 else 1
        upgrade_cost = int(parts[2]) if len(parts) > 2 else 50
        return score, click_power, upgrade_cost
    except Exception as e:
        print("Erro ao carregar dados:", e)
        return 0, 1, 50
