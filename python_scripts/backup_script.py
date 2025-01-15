#This Script will take the backup of the dir path given as input in tar.gz format
#also you can specify backup dir path or it will create a default backup dir in the home dir


import os
import tarfile
import datetime

def create_backup():
    source_directory = input("Enter the source directory path: ")
    backup_directory = input("Enter the backup directory path (leave empty for default): ")

    # Check if the source directory exists
    if not os.path.isdir(source_directory):
        print(f"Error: Source directory '{source_directory}' does not exist.")
        return

    # Set default backup directory if not provided
    if backup_directory == "":
        backup_directory = os.path.expanduser("~/backup")

    # Create backup directory if it doesn't exist
    os.makedirs(backup_directory, exist_ok=True)

    # Generate timestamp for backup filename
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

    #Takeing only the dir name from the source path
    arcname=os.path.split(source_directory.rstrip(os.sep))[-1]
    print(arcname)

    # Create backup filename with timestamp
    backup_filename = f"{arcname}_{timestamp}.tar.gz"
    backup_path = os.path.join(backup_directory, backup_filename)

    # Create tarball of the source directory
    with tarfile.open(backup_path, "w:gz") as tar:
        tar.add(source_directory, arcname)

    print(f"Backup created: {backup_path}")

# Run the script
create_backup()
