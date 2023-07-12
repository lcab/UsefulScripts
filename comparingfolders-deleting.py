# Author: Lorena Cabrera
# Date: 7/12/2023
# Purpose: Compare two folders, one containing video files with names of people(example: Lorena_Cabrera.mp4), and the 
#           other containing PDF files with names of people followed by tracking numbers.(example: Lorena Cabrera_12341234.pdf).
#           The goal is to identify any person in the second folder who is not present in the first folder and move them to a backup folder called 'backup'.

# Problem: The second folder has 2,400 files while the first folder has only 840 files.

# Solution: Cross compare the names of both folders and identify any person in folder two who is not in folder one.
#           If a person is found in folder two but not in folder one, the file is moved to the 'backup' folder.
#           Note: The code can be modified to delete the person from folder one as well, if desired.


import os
import shutil


def compare_folders(folder1, folder2):
    folder1_files = set()
    folder2_files = set()
    unique_files_in_folder1 = set()
    unique_files_in_folder2 = set()

    # Get the names of files in folder1
    for file_name in os.listdir(folder1):
        
        if os.path.isfile(os.path.join(folder1, file_name)):
            cleaned_file_name = os.path.splitext(file_name)[0].lower().replace(" ", "").replace("_", "")
            folder1_files.add(cleaned_file_name)  # Store cleaned file name without spaces and underscores

    # Get the names of files in folder2
    for file_name in os.listdir(folder2):
        if os.path.isfile(os.path.join(folder2, file_name)):
            cleaned_file_name = os.path.splitext(file_name)[0].lower().split("_")[0].replace(" ", "").replace("_", "")
            folder2_files.add(cleaned_file_name)  # Store the first part of the file name before the underscore

    # Compare the file names
    common_files = folder1_files.intersection(folder2_files)
    unique_files_in_folder1 = folder1_files - folder2_files
    unique_files_in_folder2 = folder2_files - folder1_files

    print(f"Common files: {common_files}")
    print(f"Unique files in folder1: {unique_files_in_folder1}")
    print(f"Unique files in folder2: {unique_files_in_folder2}")

    # Create backup folder if it doesn't exist
    backup_folder = 'D:\\backup_folder'  # Change this to your desired backup folder path
    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)
        print(f"Created backup folder: {backup_folder}")

    # Save original names and paths of unique files in folder1
    for file_name in unique_files_in_folder1:
        original_file_name = None
        original_file_path = None
        for original_file in os.listdir(folder1):
            if os.path.isfile(os.path.join(folder1, original_file)):
                cleaned_original_file_name = os.path.splitext(original_file)[0].lower().replace(" ", "").replace("_", "")
                if cleaned_original_file_name == file_name:
                    original_file_name = original_file
                    original_file_path = os.path.join(folder1, original_file)
                    break

    # Save original names and paths of unique files in folder2
    for file_name in unique_files_in_folder2:
        
        original_file_name = None
        original_file_path = None
        for original_file in os.listdir(folder2):
            if os.path.isfile(os.path.join(folder2, original_file)):
                cleaned_original_file_name =  os.path.splitext(original_file)[0].lower().split("_")[0].replace(" ", "").replace("_", "")
                if cleaned_original_file_name == file_name:
                    original_file_name = original_file
                    original_file_path = os.path.join(folder2, original_file)
                    break

        if original_file_name and original_file_path:
            # Check if the cleaned original file name matches any unique file name in folder1
            cleaned_file_name_in_folder1 = file_name
            if cleaned_file_name_in_folder1 not in common_files:
                    # Copy the file to the backup folder or perform any necessary operations
                backup_file_path = os.path.join(backup_folder, original_file_name)
                shutil.copy2(original_file_path, backup_file_path)
                    # Optionally, delete the file from folder2
                os.remove(original_file_path)
                print(f"Moved file {original_file_name} from folder2 to {backup_folder} and deleted from folder2.")
            else:
                    print(f"File {original_file_name} in folder2 matches a unique file name in folder1. Skipping.")
        else:
            print(f"Could not find original file for {file_name} in folder2.")

folder1_path = 'D:\\videos'
folder2_path = 'D:\\equivalent-pdf'

compare_folders(folder1_path, folder2_path)
