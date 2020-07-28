import os
from pathlib import Path

directories = {
    "PYTHON":['.py'],
    "PLAINTEXT":['.txt'],
    "VIDEOS":['.avi','.flv','.wmv',".mov", ".mp4", ".webm", ".vob", ".mng",
   ".qt", ".mpg", ".mpeg", ".3gp"],
    "DOCUMENTS":[".doc",'.pages','.fdf'],
    "AUDIO":[".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
   ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"],
   "PHOTOS":[".jpg",".jpeg",],
   "PDF":[".pdf"]
}
file_formats = {file_format: directory
    for directory, file_formats in directories.items()
    for file_format in file_formats
}
print(file_formats)
def create_folders():
    for object in os.scandir():
        if object.is_dir():
            continue
        file_name = Path(object)
        #lower case and gets file type
        file_type = file_name.suffix.lower() 
        if file_type in file_formats:  
            direc_path =  Path(file_formats[file_type])
            direc_path.mkdir(exist_ok=True)
            file_name.rename((direc_path.joinpath(file_name)))
        elif file_type not in file_formats:
            misc = "MISC"
            direc_path =  Path(misc)
            direc_path.mkdir(exist_ok=True)
            file_name.rename((direc_path.joinpath(file_name)))


create_folders()