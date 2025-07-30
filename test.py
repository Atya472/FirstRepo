import os
import shutil

def organize_file(directory):
    file_types={
        "Images":[".jpg",".png"],
        "Documents":[".pdf",".docx"],
        "Videos":[".mp4",".mov"]
    }

    for folder in file_types.keys():
        folder_path=os.path.join(directory,folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    for file_name in os.listdir(directory):
        file_path=os.path.join(directory,file_name)
        if os.path.isfile(file_path):
            for folder,extensions in file_types.items():
                if any(file_name.lower().endswith(ext) for ext in extensions):
                    shutil.move(file_path,os.path.join(directory,folder,file_name))

organize_file(input('please enter the path of the folder that you want to organize',))