import os
import subprocess
from datetime import datetime

# Nutzername hier eintragen oder beim Start abfragen
username = input("👤 Dein Name: ")

def run_cmd(cmd):
    subprocess.run(cmd, check=True)

def sync_from_git():
    print("🔄 Git pull...")
    run_cmd(["git", "pull"])

def start_minecraft_server():
    print("🚀 Starte Minecraft-Server...")
    run_cmd(["java", "-Xmx2G", "-Xms2G", "-jar", "server.jar", "nogui"])

def sync_to_git():
    print("💾 Speichere und lade Änderungen hoch...")
    run_cmd(["git", "add", "."])
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    run_cmd(["git", "commit", "-m", f"Welt-Update von {username} am {now}"])
    run_cmd(["git", "push"])

def main():
    sync_from_git()
    start_minecraft_server()
    sync_to_git()
    print("✅ Fertig!")

if __name__ == "__main__":
    main()
