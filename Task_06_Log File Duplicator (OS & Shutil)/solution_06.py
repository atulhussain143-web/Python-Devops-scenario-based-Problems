import os
import shutil

source_file = "app.log"

if os.path.exists(source_file):
    for i in range(1, 6):
        destination_file = f"app_{i}.log"
        shutil.copy(source_file, destination_file)
    print("Log files duplicated successfully")
else:
    print("app.log file not found")
