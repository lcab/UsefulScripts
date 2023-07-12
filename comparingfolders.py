# Author: Lorena Cabrera
# Date: 7/12/2023
# Purpose: Compare two folders, one containing video files with names of people(example: Lorena_Cabrera.mp4), and the 
#           other containing PDF files with names of people followed by tracking numbers.(example: Lorena Cabrera_12341234.pdf).
#           The goal is to identify any person in the second folder who is not present in the first folder and move them to a backup folder called 'backup'.

# Problem: The second folder has 2,400 files while the first folder has only 840 files.

# Solution: Cross compare the names of both folders and identify any person in folder two who is not in folder one.
#           print the similarities and diferences



import os

def compare_folders(folder1, folder2):
    folder1_files = set()
    folder2_files = set()

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

# Example usage
folder1_path = 'C:\\Users\\actualvid'
folder2_path = 'C:\\Users\\documentfolder'

compare_folders(folder1_path, folder2_path)
