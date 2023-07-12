'''Lorena Cabrera
7/12/2023
Purpose:
Go into excel file which has the name of a person in one row and their corresponding video link (oogle docs) in another row
if link works we will download the video into a folder and set the persons name as the videos name
if video link does not have access/does not work the video link file will pop up in the separate text file'''


import re
import os
import openpyxl
import gdown

#reading excel file and going to scpecific sheet
wb = openpyxl.load_workbook('names and videos.xlsx')
ws = wb['Sheet1']

#store folder paths to variables
download_folder = 'D:\\this is a path to a folder'
new_file = "D:\\This is a path\\notworking.txt"

# Iterate through excel and display data
for row in ws.iter_rows(min_row=1, max_row=840, values_only=True):
    name = row[0]  # Column 1, row index 0
    link = row[9]  # Column 10, row index 9

    # Print the name and link regardless of the condition
    print(name, end=" ")
    print(link, end=" ")
    print()

    #open text file to write the links that did not work
    with open(new_file, 'a') as not_working_file:
        if link.startswith('https://') :
            video_url = link.strip()

            # Extract the file ID from the URL
            match = re.search(r'/file/d/([^/]+)', video_url)
            if match:
                file_id = match.group(1)

                # Create the direct download link
                modified_url = f'https://drive.google.com/uc?export=download&id={file_id}'

                # Download the video using gdown
                output_path = os.path.join(download_folder, f'{file_id}.mp4')
                link_does_not_work = gdown.download(modified_url, output=output_path)

                if link_does_not_work is None:
                    not_working_file.write(link)
                else:
                    print("The link works!")
                    # New file name
                    new_name = "_".join(name.split()) + '.mp4'

                    # New file path
                    new_video_file = os.path.join(os.path.dirname(output_path), new_name)

                    # Rename the file
                    os.rename(output_path, new_video_file)

            else:
                print("No file ID found in the URL.")
        else:
            print("This is a space.")
