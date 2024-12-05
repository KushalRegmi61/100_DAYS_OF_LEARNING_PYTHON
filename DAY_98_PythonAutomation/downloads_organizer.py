import os
import shutil
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Define your Downloads folder and categories
DOWNLOADS_FOLDER = os.path.expanduser("~/Downloads")
CATEGORIES = {
    "PDFs": [".pdf"],
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mkv", ".mov"],
    "Documents": [".docx", ".txt", ".xlsx"],
    "Executables": [".exe", ".msi", ".dmg"],
    "Others": []
}

# Configure logging to save the log file in the Downloads folder
log_file_path = os.path.join(DOWNLOADS_FOLDER, "downloads_organizer.log")

logging.basicConfig(
    filename=log_file_path,  # Log file path in Downloads folder
    level=logging.INFO,  # Log level
    format="%(asctime)s - %(levelname)s - %(message)s",  # Log format
    datefmt="%Y-%m-%d %H:%M:%S"  # Date format
)

# Function to create category folders
def create_folders():
    for category in CATEGORIES:
        folder_path = os.path.join(DOWNLOADS_FOLDER, category)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            logging.info(f"Created folder: {folder_path}")

# Function to organize a single file
def organize_file(file_path):
    file_name = os.path.basename(file_path)
    file_ext = os.path.splitext(file_name)[1].lower()
    moved = False
    for category, extensions in CATEGORIES.items():
        if file_ext in extensions:
            try:
                dest_path = os.path.join(DOWNLOADS_FOLDER, category, file_name)
                shutil.move(file_path, dest_path)
                logging.info(f"Moved {file_name} to {dest_path}")
                moved = True
                break
            except Exception as e:
                logging.error(f"Failed to move {file_name}: {e}")
                return
    if not moved:  # If no category matched, move to "Others"
        try:
            dest_path = os.path.join(DOWNLOADS_FOLDER, "Others", file_name)
            shutil.move(file_path, dest_path)
            logging.info(f"Moved {file_name} to {dest_path}")
        except Exception as e:
            logging.error(f"Failed to move {file_name}: {e}")

# Custom event handler for Watchdog
class DownloadsEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:  # Ignore directory events
            logging.info(f"Detected new file: {event.src_path}")
            organize_file(event.src_path)

# Main function to monitor folder
def monitor_folder():
    create_folders()  # Ensure category folders are created
    event_handler = DownloadsEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path=DOWNLOADS_FOLDER, recursive=False)
    observer.start()
    logging.info(f"Started monitoring {DOWNLOADS_FOLDER}")
    try:
        while True:
            pass  # Keep the script running
    except KeyboardInterrupt:
        observer.stop()
        logging.info("Stopped monitoring.")
    observer.join()

# Run the script
if __name__ == "__main__":
    logging.info("Starting Downloads Organizer script...")
    monitor_folder()
