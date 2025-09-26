import os
import shutil

def organize_files():
    source_folder = os.path.expanduser("~/documents")

    destination_folders = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Documents": [".pdf", ".docx", ".txt", ".pptx"],
        "Videos": [".mp4", ".mkv", ".mov"],
        "Music": [".mp3", ".wav"],
        "Compressed": [".zip", ".rar"],
        "Programs": [".exe", ".msi"],
        "Python": [".py"]
    }

    for file_name in os.listdir(source_folder):
        file_path = os.path.join(source_folder, file_name)

        if os.path.isfile(file_path):
            moved = False
            for folder, extensions in destination_folders.items():
                if any(file_name.lower().endswith(ext) for ext in extensions):
                    folder_path = os.path.join(source_folder, folder)
                    os.makedirs(folder_path, exist_ok=True)
                    shutil.move(file_path, os.path.join(folder_path, file_name))
                    print(f"Moved: {file_name} → {folder}/")
                    moved = True
                    break

            if not moved:
                other_path = os.path.join(source_folder, "Others")
                os.makedirs(other_path, exist_ok=True)
                shutil.move(file_path, os.path.join(other_path, file_name))
                print(f"Moved: {file_name} → Others/")

if __name__ == "__main__":
    organize_files()
