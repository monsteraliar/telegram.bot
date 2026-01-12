import requests
import time

TOKEN = 7432590124:AAE2WaUxe-xjkQ7a9Biwk1YWkGU_pFSCj24"
CHAT_ID = "303839054"

URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

def send(msg):
    requests.post(URL, data={
        "chat_id": CHAT_ID,
        "text": msg
    })

send("🤖 BOT ONLINE 24 JAM (RAILWAY)")

while True:
    time.sleep(3600)
