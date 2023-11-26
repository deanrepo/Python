from pathlib import Path
from datetime import datetime

# Get the current year and month
current_date = datetime.now()
year_month_folder_name = current_date.strftime("%Y%m")
base_path = Path(r"C:\Users\Minghui Zhang\Pictures\Test\History")
folder_path = base_path / year_month_folder_name

if not folder_path.exists():
    folder_path.mkdir(parents=True, exist_ok=True)
    print("The folder exists, has been created")
else:
    print("The folder exist")