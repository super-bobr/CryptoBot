import json
from pathlib import Path

DB_PATH = Path("subscribers.json")

def _load() -> set:
    if DB_PATH.exists():
        return set(json.loads(DB_PATH.read_text())) #часть которая создает и обновляет файл json с подписчиками, вместо бд
    return set()

def _save(users: set):
    DB_PATH.write_text(json.dumps(list(users)))

def subscribe(chat_id: int):
    subs = _load()
    subs.add(chat_id)
    _save(subs)

def unsubscribe(chat_id: int):
    subs = _load()
    subs.discard(chat_id)
    _save(subs)

def get_all() -> list:
    return list(_load())
