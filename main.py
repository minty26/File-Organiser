import os
import shutil

def organize_files(folder_path):
    files = os.listdir(folder_path)
    for file in files:
        if os.path.isfile(os.path.join(folder_path, file)):
            file_extension = file.split('.')[-1]
            extension_folder_path = os.path.join(folder_path, file_extension)
            if not os.path.exists(extension_folder_path):
                os.makedirs(extension_folder_path)
            try:
                shutil.move(os.path.join(folder_path, file), os.path.join(extension_folder_path, file))
            except shutil.Error as e:
                print(f"Error organizing file: {e}")

# Specify the folder path to organize
folder_path = 'path_to_your_folder'
organize_files(folder_path)
