import requests
import time

TOKEN = "GANTI_DENGAN_TOKEN_BARU"
CHAT_ID = "303839054"

URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

def send(msg):
    requests.post(URL, data={
        "chat_id": CHAT_ID,
        "text": msg
    })

send("🤖 BOT ONLINE 24 JAM (SERVER)")

while True:
    send("⏱ Bot masih hidup (server)")
    time.sleep(3600)  # 1 jam