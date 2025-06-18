"""
Um único arquivo 'clicker.key' faz o serviço completo:
{
  "key": "<base64 Fernet>",
  "cipher": "<base64 score criptografado>"
}
"""

import json
from pathlib import Path
from cryptography.fernet import Fernet, InvalidToken

BASE_DIR = Path("/storage/emulated/0/Documents/.assets")
FILE     = BASE_DIR / "clicker.key"


# ──────────────────────────────────────────────────────────────
# helpers
# ──────────────────────────────────────────────────────────────
def _ensure_dir():
    BASE_DIR.mkdir(parents=True, exist_ok=True)


def _new_record(score:int=0) -> dict:
    key    = Fernet.generate_key().decode()         # str base64
    cipher = Fernet(key.encode()).encrypt(str(score).encode()).decode()
    return {"key": key, "cipher": cipher}


def _load_record() -> dict:
    if not FILE.exists():
        return _new_record()
    try:
        return json.loads(FILE.read_text())
    except json.JSONDecodeError:
        return _new_record()                        # corrompido


def _save_record(rec:dict):
    _ensure_dir()
    tmp = FILE.with_suffix('.tmp')
    tmp.write_text(json.dumps(rec))
    tmp.replace(FILE)


# ──────────────────────────────────────────────────────────────
# API
# ──────────────────────────────────────────────────────────────
def load_score() -> int:
    rec = _load_record()
    try:
        score = Fernet(rec["key"].encode()).decrypt(rec["cipher"].encode())
        return int(score.decode())
    except (InvalidToken, ValueError, KeyError):
        # chave ou cipher inválidos → zera tudo
        rec = _new_record(0)
        _save_record(rec)
        return 0


def save_score(score:int):
    rec          = _load_record()
    f            = Fernet(rec["key"].encode())
    rec["cipher"] = f.encrypt(str(score).encode()).decode()
    _save_record(rec)


def inc_score(delta:int=1) -> int:
    new_val = load_score() + delta
    save_score(new_val)
    return new_val