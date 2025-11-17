import requests

TELEGRAM_BOT_TOKEN = "اینجا توکن ربات تلگرام"
CHAT_ID = "اینجا آی‌دی عددی چت"

def send_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text
    }
    requests.post(url, json=payload)

if __name__ == "__main__":
    send_message("ربات با موفقیت به تلگرام وصل شد 🎯")
