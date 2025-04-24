import os
from collections import defaultdict
from pathlib import Path

FILE_CATEGORIES = {
    "Images": ['.jpg', '.jpeg', '.png', '.svg', '.gif', '.bmp', '.tiff', ".HEIC"],
    "Documents": ['.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx'],
    "Software": ['.exe', '.msi', '.apk', '.dmg', '.deb'],
    "Videos": ['.mp4','.MOV','.mkv', '.mov', '.avi', '.flv'],
    "Audio": ['.mp3', '.wav', '.aac', '.flac', '.m4a'],
    "Archives": ['.zip', '.rar', '.7z', '.tar', '.gz'],
}

def get_category(extension):
    for category, extensions in FILE_CATEGORIES.items():
        if extension.lower() in extensions:
            return category
    return "Others"

def categorize_files(base_folder):
    categorized = defaultdict(list)

    for root, dirs, files in os.walk(base_folder):
        # Exclude the 'Organized' folder from processing
        dirs[:] = [d for d in dirs if d != "Organized"]
        for file in files:
            ext = Path(file).suffix
            category = get_category(ext)
            full_path = os.path.join(root, file)
            categorized[category].append(full_path)

    return categorized

def print_categorized_tree(categorized):
    for category, files in categorized.items():
        print(f"📁 {category}")
        seen = set()
        for f in files:
            filename = os.path.basename(f)
            if filename in seen:
                duplicate_name = f"(duplicate)-{filename}"
                print(f"    └── {duplicate_name}")
            else:
                print(f"    └── {filename}")
                seen.add(filename)

if __name__ == "__main__":
    folder_path = input("Enter folder path to categorize: ").strip()

    if not os.path.isdir(folder_path):
        print("❌ Invalid folder path.")
    else:
        categorized = categorize_files(folder_path)
        print("\nCategorized File Tree:\n")
        print_categorized_tree(categorized)

        copy_files = input("\nDo you want to copy the files to an organized folder? (yes/no): ").strip().lower()
        if copy_files in ['yes', 'y']:
            organized_folder = os.path.join(folder_path, "Organized")
            os.makedirs(organized_folder, exist_ok=True)

            for category, files in categorized.items():
                category_folder = os.path.join(organized_folder, category)
                os.makedirs(category_folder, exist_ok=True)

                for file_path in files:
                    try:
                        file_name = os.path.basename(file_path)
                        parent_folders = os.path.dirname(file_path).split(os.path.sep)[-2:]
                        parent_folder_name = parent_folders[-1] if len(parent_folders) > 1 else parent_folders[0]
                        specific_folder = os.path.join(category_folder, parent_folder_name)
                        os.makedirs(specific_folder, exist_ok=True)

                        destination = os.path.join(specific_folder, file_name)
                        if not any(file_name.endswith(ext) for ext in FILE_CATEGORIES.get("Others", [])):
                            from shutil import copy2
                            copy2(file_path, destination)

                            # Delete the file if it matches any extension in FILE_CATEGORIES
                            for extensions in FILE_CATEGORIES.values():
                                if any(file_name.endswith(ext) for ext in extensions):
                                    os.remove(file_path)
                                    break
                    except Exception as e:
                        print(f"❌ Error copying or deleting file {file_path}: {e}")

            print("\n✅ Files have been copied to the 'Organized' folder.")
        else:
            print("\nNo files were copied.")