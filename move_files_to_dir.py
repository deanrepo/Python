import os
import shutil
from datetime import datetime, timedelta
from pathlib import Path

def move_files_except_folders(source_folder, destination_folder):
    # Create a new folder with yesterday's date
    yesterday_date = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
    new_folder_path = os.path.join(destination_folder, yesterday_date)
    os.makedirs(new_folder_path, exist_ok=True)

    # Move files from the source folder to the new folder
    for filename in os.listdir(source_folder):
        source_path = os.path.join(source_folder, filename)
        if os.path.isfile(source_path):
            shutil.move(source_path, new_folder_path)

if __name__ == "__main__":
    # Replace 'source_folder' and 'destination_folder' with your actual folder paths
    source_folder = r'C:\Users\Minghui Zhang\Pictures'  # Use 'r' to indicate a raw string for Windows paths

    # Check destination folder exists or not, if not create a new one.
    # Get the current year and month
    current_date = datetime.now()
    year_month_folder_name = current_date.strftime("%Y%m")
    destination_base_path = Path(r"C:\Users\Minghui Zhang\Pictures\History")
    destination_folder_path = destination_base_path / year_month_folder_name

    if not destination_folder_path.exists():
        destination_folder_path.mkdir(parents=True, exist_ok=True)

    move_files_except_folders(source_folder, destination_folder_path)
