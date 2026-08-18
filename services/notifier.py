import requests
from config import API_KEY

def notify_task_created(title):
    payload = {"event": "task.created", "title": title, "key": API_KEY}
    try:
        requests.post("https://hooks.example.com/notify", json=payload, timeout=5)
    except Exception:
        pass