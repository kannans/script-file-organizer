# File Organizer Script

This Python script categorizes and organizes files in a directory based on their extensions. It creates an organized folder structure, copies files into categorized subfolders, and optionally deletes the original files after copying.

## Features

- Categorizes files into predefined categories such as Images, Documents, Videos, etc.
- Creates an "Organized" folder with subfolders for each category.
- Handles duplicate file names by appending a `(duplicate)` prefix.
- Optionally deletes the original files after copying.

## File Categories

The script uses the following categories and file extensions:

- **Images**: `.jpg`, `.jpeg`, `.png`, `.svg`, `.gif`, `.bmp`, `.tiff`, `.HEIC`
- **Documents**: `.pdf`, `.doc`, `.docx`, `.txt`, `.xls`, `.xlsx`, `.ppt`, `.pptx`
- **Software**: `.exe`, `.msi`, `.apk`, `.dmg`, `.deb`
- **Videos**: `.mp4`, `.MOV`, `.mkv`, `.mov`, `.avi`, `.flv`
- **Audio**: `.mp3`, `.wav`, `.aac`, `.flac`, `.m4a`
- **Archives**: `.zip`, `.rar`, `.7z`, `.tar`, `.gz`
- **Others**: Files that do not match any of the above categories.

## How to Run

1. Ensure you have Python installed on your system.
2. Save the script as `file_organizer.py`.
3. Open a terminal and navigate to the directory containing the script.
4. Run the script using the following command:

   ```bash
   python file_organizer.pyReadme
   ```

5. Enter the path to the folder you want to organize when prompted.
6. The script will display a categorized file tree and ask if you want to copy the files to an organized folder.
7. If you choose "yes," the files will be copied to an "Organized" folder within the specified directory.

##### Example Output

Input

Suppose the folder contains the following files:

/example-folder
file1.jpg
file2.pdf
file3.mp4
file4.docx
file5.jpg

##### Script Execution

Enter folder path to categorize: /example-folder

Categorized File Tree:

📁 Images
└── file1.jpg
└── file5.jpg
📁 Documents
└── file2.pdf
└── file4.docx
📁 Videos
└── file3.mp4

Do you want to copy the files to an organized folder? (yes/no): yes

✅ Files have been copied to the 'Organized' folder.

##### Output Folder Structure

/example-folder/Organized
/Images
/example-folder
file1.jpg
file5.jpg
/Documents
/example-folder
file2.pdf
file4.docx
/Videos
/example-folder
file3.mp4

#### Notes

- Ensure you have write permissions for the directory you are organizing.
- The script will skip files in the "Organized" folder to avoid infinite loops.
- If a file cannot be copied or deleted, an error message will be displayed.

Enjoy organizing your files! ```
