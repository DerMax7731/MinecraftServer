import subprocess
import os
import time

def run_cmd(cmd):
    subprocess.run(cmd, check=True)

def git_pull():
    print("🔄 Git pull...")
    run_cmd(["git", "pull"])

def git_push():
    print("📤 Git push...")
    try:
        run_cmd(["git", "add", "."])
        run_cmd(["git", "commit", "-m", "📦 Automatischer Upload"])
        run_cmd(["git", "push"])
        print("✅ Spielstand erfolgreich hochgeladen.")
    except subprocess.CalledProcessError:
        print("⚠️ Keine Änderungen zum Commit.")

def start_minecraft_server():
    print("🚀 Starte Minecraft-Server...")
    try:
        run_cmd(["java", "-Xmx2G", "-Xms2G", "-jar", "server.jar", "nogui"])
    except subprocess.CalledProcessError:
        print("❌ Fehler beim Starten des Servers.")

def main():
    name = input("👤 Dein Name: ")
    git_pull()
    start_minecraft_server()
    git_push()
    input("Drücke Enter zum Beenden...")

if __name__ == "__main__":
    main()
