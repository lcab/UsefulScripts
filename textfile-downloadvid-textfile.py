'''Lorena Cabrera
7/12/2023
Purpose:
Go into text file to get multiple downloadable video links from google drive
if videos are accesible then download videos and import into separate folder
if videos not accesible then input video links into the not working text file'''

import gdown
import re
import os
import openpyxl #import excel reader

wb = openpyxl.load_workbook('names and videos.xlsx') #opening excel file
ws = wb['Sheet1'] #going to the sheet one of the excel file

# Set the path to the text file containing the video URLs
video_links_file = 'C:\\text file with all the downloadable video links\\a.txt'

# Set the path to the folder where you want to download the videos
download_folder = 'D:\Videos- code'

# Store any links not working here
new_file = "D:\Videos- code\\notworking.txt"

#opening not working text file
with open(new_file, 'w') as not_working_file:
    
    #open text file with all the downloadable video links
    with open(video_links_file) as infile:
        for line in infile:
            if line.startswith('https://'):
                video_url = line.strip()

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
                        not_working_file.write(line)
                    else:
                        print("The link works!")
                else:
                    print("No file ID found in the URL.")
            else:
                print("This is a space.")
