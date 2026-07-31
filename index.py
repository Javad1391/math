import requests
import time

# ⚠️ حتماً توکن جدید خود را اینجا بگذارید
TOKEN = "1366377639:2mCDHBKQeuvHxMOKXxsQtW4kW2jWTIeINxg" 
BASE_URL = f"https://tapi.bale.ai/bot{TOKEN}/"

# ✅ لینک جدید: https://javad1391.github.io/game/
INLINE_KB = {
    "inline_keyboard": [
        [{"text": "🎮 ورود به بازی", "url": "https://javad1391.github.io/game/"}]
    ]
}

def send_msg(cid, text, reply_markup=None):
    payload = {"chat_id": int(cid), "text": text}
    if reply_markup:
        payload["reply_markup"] = reply_markup
    response = requests.post(BASE_URL + "sendMessage", json=payload).json()
    return response.get("ok", False)

def get_updates(offset):
    return requests.post(BASE_URL + "getUpdates", json={"offset": offset, "timeout": 30}).json()

def main():
    print("✅ ربات با لینک جدید اجرا شد: https://javad1391.github.io/game/")
    offset = 0
    
    while True:
        try:
            updates = get_updates(offset)
            if "result" in updates:
                for update in updates["result"]:
                    offset = update["update_id"] + 1
                    if "message" in update:
                        cid = update["message"]["chat"]["id"]
                        send_msg(
                            cid, 
                            "سلام! 👋\nبرای شروع بازی روی دکمه زیر کلیک کنید:", 
                            reply_markup=INLINE_KB
                        )
        except Exception as e:
            print(f"❌ خطا: {e}")
            time.sleep(5)

if __name__ == "__main__":
    main()
