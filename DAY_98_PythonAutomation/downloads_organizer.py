import os
import shutil
import logging
import time

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
            print(f"Created '{category}' folder")  # Print a message to the console


# Function to delete incomplete .crdownload files
def delete_incomplete_crdownload_files():
    for file_name in os.listdir(DOWNLOADS_FOLDER):
        file_path = os.path.join(DOWNLOADS_FOLDER, file_name)

        # Check if the file is a .crdownload file
        if file_name.endswith(".crdownload"):
            try:
                os.remove(file_path)
                print(f"Deleted incomplete .crdownload file: {file_name}") # Print a message to the console
            except Exception as e:
                print(f"Failed to delete .crdownload file {file_name}") # Print a message to the console


# Function to wait until the file is fully downloaded
def wait_for_file_to_download(file_path, interval=1):
    """
    Waits for the file to stop growing, indicating that the download is complete.
    Args:
        file_path (str): The path to the file to check.
        interval (int): The interval between checks (in seconds).
    """
    last_size = -1

    while True:
        # Get the current size of the file
        current_size = os.path.getsize(file_path)

        # Check if the file size is no longer changing
        if current_size == last_size:
            print(f"File download complete: {file_path}")
            delete_incomplete_crdownload_files()  # Delete incomplete .crdownload files
            break

        # If the file is still being written to, wait and check again
        last_size = current_size

        time.sleep(interval)

# Function to organize a single file
def organize_file(file_path):
    file_name = os.path.basename(file_path)

    # Skip the log file to avoid modifying it
    if file_name == "downloads_organizer.log":
        print("Skipped organizing the log file.")  # Print a message to the console
        return

    # Handle .crdownload files by waiting for them to finish downloading
    if file_name.endswith(".crdownload"):
        logging.info(f"Detected .crdownload file: {file_name}")
        wait_for_file_to_download(file_path)  # Wait until the download is complete

    file_ext = os.path.splitext(file_name)[1].lower()
    moved = False
    for category, extensions in CATEGORIES.items():
        if file_ext in extensions:
            try:
                dest_path = os.path.join(DOWNLOADS_FOLDER, category, file_name)
                shutil.move(file_path, dest_path)
                print(f"Moved {file_name} to '{category}' folder")  # Print a message to the console
                moved = True
                break
            except Exception as e:
                logging.error(f"Failed to move {file_name}: {e}")  # Log the error
                print(f"Failed to move {file_name}")  # Print a message to the console
                return
    if not moved:  # If no category matched, move to "Others"
        try:
            dest_path = os.path.join(DOWNLOADS_FOLDER, "Others", file_name)
            shutil.move(file_path, dest_path)
            logging.info(f"Moved {file_name} to {dest_path}")  # Log the move
            print(f"Moved {file_name} to 'Others' folder")  # Print a message to the console
        except Exception as e:
            print(f"Failed to move {file_name}")  # Print a message to the console


# Function to list and organize files live in the Downloads folder
def live_organize_files():
    create_folders()  # Ensure category folders are created
    print(f"Live Organizing files in {DOWNLOADS_FOLDER}...")  # Print a message to the console

    while True:


        # List all files in the Downloads folder
        for file_name in os.listdir(DOWNLOADS_FOLDER):
            file_path = os.path.join(DOWNLOADS_FOLDER, file_name)
             


            # Skip directories
            if os.path.isdir(file_path):
                continue

            # Organize the file
            organize_file(file_path)

        # Sleep for a while before checking the folder again
        time.sleep(5)  # Check every 5 seconds

# Run the script
if __name__ == "__main__":
    logging.info("Starting Downloads Organizer script...")  # Log the start of the script
    print("Downloads Organizer started.")  # Print a message to the console
    live_organize_files()
