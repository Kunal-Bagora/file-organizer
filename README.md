# 📂 File Organizer

A simple Python-based file organization tool that automatically sorts files into categorized folders based on their file extensions.

This project was built to practice Python fundamentals, object-oriented programming, file handling, and working with the `pathlib` module.

---

## ✨ Features

- 📁 Organizes files automatically based on file type
- 🖼️ Supports multiple image formats
- 🎬 Supports multiple video formats
- 📄 Supports text and document files
- 🎵 Supports multiple audio formats
- 📦 Places unsupported file types into an `Others` folder
- 🔄 Handles duplicate filenames automatically
- 🚫 Skips hidden files and existing directories
- 📊 Displays a summary of organized files
- ⚠️ Handles file-moving errors without stopping the program
- 🪟 Works with Windows file paths

---

## 🗂️ File Categories

The organizer currently supports the following categories:

| Category | Examples |
|----------|----------|
| Images | `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.webp`, `.svg`, `.tiff`, `.ico`, `.heic`, `.raw`, `.jfif`, `.avif` |
| Videos | `.mp4`, `.mkv`, `.avi`, `.mov`, `.wmv`, `.flv`, `.webm`, `.mpeg`, `.mpg`, `.3gp`, `.m4v`, `.ts` |
| Texts | `.txt`, `.log`, `.md`, `.rtf`, `.ini`, `.cfg`, `.conf` |
| Documents | `.pdf`, `.doc`, `.docx`, `.ppt`, `.pptx`, `.xls`, `.xlsx`, `.csv`, `.odt`, `.ods`, `.odp` |
| Music | `.mp3`, `.wav`, `.aac`, `.flac`, `.ogg`, `.m4a`, `.wma`, `.aiff` |
| Others | Any unsupported file extension |

---

## ⚙️ How It Works

1. The user provides a directory path.
2. The program validates the directory.
3. It scans the files inside the selected directory.
4. Each file's extension is checked.
5. The file is assigned to the appropriate category.
6. Category folders are created automatically.
7. Files are moved into their respective folders.
8. Duplicate filenames are renamed automatically.
9. A final summary shows the number of files organized.

### Example

Before:

```text
MyFolder/
├── photo.jpg
├── presentation.pptx
├── song.mp3
├── notes.txt
├── movie.mp4
└── data.zip
```

After:

```text
MyFolder/
├── Images/
│   └── photo.jpg
├── Documents/
│   └── presentation.pptx
├── Music/
│   └── song.mp3
├── Texts/
│   └── notes.txt
├── Videos/
│   └── movie.mp4
└── Others/
    └── data.zip
```

---

## 🛠️ Technologies Used

- **Python**
- **pathlib**
- **Object-Oriented Programming (OOP)**
- **File Handling**
- **Exception Handling**

No external Python libraries are required.

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Kunal-Bagora/file-organizer.git
```

### 2. Navigate to the project directory

```bash
cd file-organizer
```

### 3. Run the program

```bash
python File_Organizer.py
```

### 4. Enter the directory path

When prompted:

```text
Enter directory path or press Enter to use current directory
Path:
```

Enter the path of the folder you want to organize.

For example:

```text
C:\Users\YourName\Desktop\MessyFolder
```

You can also press `Enter` to organize files in the current working directory.

---

## 📊 Example Output

```text
Enter directory path or press Enter to use current directory
Path: C:\Users\YourName\Desktop\MessyFolder

Folder Found

Summary:

Total: 6
Images: 1
Videos: 1
Texts: 1
Documents: 1
Music: 1
Others: 1
```

---

## 🔄 Duplicate File Handling

If a file with the same name already exists in the destination folder, the program automatically creates a new name instead of overwriting the existing file.

Example:

```text
photo.jpg
photo(1).jpg
photo(2).jpg
```

This helps prevent accidental file replacement.

---

## 🎯 Learning Objectives

This project helped me practice:

- Working with files and directories using `pathlib`
- Object-oriented programming in Python
- Iterating through directory contents
- Working with file extensions
- Creating directories programmatically
- Moving and renaming files
- Handling duplicate filenames
- Exception handling
- Building a practical automation tool using Python

---

## 💡 Project Purpose

The main goal of this project was to build a practical automation tool while strengthening Python fundamentals.

Instead of manually sorting files into different folders, the program automates the process based on file type.

---

## 🤖 AI Assistance

AI was used as a learning and development assistant during the project for guidance, debugging, and reviewing implementation ideas.

The core project logic and implementation were developed while practicing Python fundamentals.

---

## 📌 Future Improvements

Some possible improvements for future versions:

- Add more file categories
- Allow users to customize categories and extensions
- Add a preview mode before moving files
- Add logging for moved files
- Add an undo feature
- Add a graphical user interface

---

## 👨‍💻 Author

**Kunal Bagora**

Built as part of my Python learning and portfolio projects.

---

⭐ If you find this project useful, feel free to star the repository!
