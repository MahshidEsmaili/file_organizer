import os 
import shutil
def organize_files(folder_path):
    if not os.path.exists(folder_path):
        print("Folder not found")
        return 
    
    files=os.listdir(folder_path)
    for file in files:
        files_path=os.path.join(folder_path,file)
        if os.path.isdir(files_path):
            continue
        if "." in file:
            ext=file.split(".")[-1]
        else:
            ext="no extension"
        target_folder=os.path.join(folder_path,ext)
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)
        shutil.move(files_path,target_folder)
    print("Files organized successfully")
    folder=input("Enter the folder path to organize:")
    organize_files(folder)
