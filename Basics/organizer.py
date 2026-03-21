from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pathlib import Path
import shutil
import time

downloads = Path.home() / "Downloads"

folders = {
    "Images": [".png", ".jpg", ".jpeg", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar"]
}

class DownloadHandler(FileSystemEventHandler):

    def on_created(self, event):
        path = Path(event.src_path)

        if path.is_file():
            ext = path.suffix.lower()

            for folder, extensions in folders.items():
                if ext in extensions:
                    target = downloads / folder
                    target.mkdir(exist_ok=True)

                    time.sleep(1)  # espera a que termine la descarga
                    shutil.move(str(path), str(target / path.name))
                    print(f"Movido {path.name} -> {folder}")
                    break


observer = Observer()
observer.schedule(DownloadHandler(), str(downloads), recursive=False)
observer.start()

print("Organizador de descargas activo...")

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()

observer.join()