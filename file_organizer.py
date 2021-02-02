import os
from pathlib import Path

directories = {
    "python":['.py'],
    "text_files":['.txt'],
    "videos":['.avi','.flv','.wmv',".mov", ".mp4", ".webm", ".vob", ".mng",
   ".qt", ".mpg", ".mpeg", ".3gp"],
    "documents":[".doc",'.pages','.fdf', '.xlsx'],
    "audio":[".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
   ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"],
   "photos":[".jpg",".jpeg",],
   "pdfs":[".pdf"]
}
file_formats = {file_format: directory
    for directory, file_formats in directories.items()
    for file_format in file_formats
}
def create_folders(dir):
    dir = Path(dir)
    status_message = "Running..."
    print(status_message)
    if os.path.isdir(dir):
        for object in os.scandir(dir):
            if object.is_dir():
                continue
            file_name = Path(object)
            file_type = file_name.suffix.lower() 
            if file_type in file_formats:  
                direc_path = Path(os.path.join(dir,file_formats[file_type]))
            elif file_type not in file_formats:
                misc = "msc"
                direc_path = Path(os.path.join(dir,misc))
            direc_path.mkdir(exist_ok=True)
            file_name.rename(os.path.join(direc_path,os.path.basename(file_name)))
        status_message = "Sort Successful."
    else:
        status_message = "Failed. Please enter a valid path."
    print(status_message)


create_folders() #Pass your dir in as str param