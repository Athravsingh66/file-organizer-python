# File Organizer

A simple Python automation project that organizes files into separate folders based on their file extensions.

## Features

* Select a folder to organize
* Automatically detects file extensions
* Organizes files into categories:

  * Images
  * Videos
  * Audio
  * Documents
  * Code
  * Archives
* Ignores unsupported files
* Does not move existing folders
* Uses Python's built-in `os` and `shutil` modules

## Supported Extensions

| Category  | Extensions                      |
| --------- | ------------------------------- |
| Images    | `.jpg`, `.png`, `.jpeg`, `.gif` |
| Videos    | `.mp4`, `.mkv`, `.avi`          |
| Audio     | `.mp3`, `.wav`                  |
| Documents | `.pdf`, `.docx`, `.txt`         |
| Code      | `.py`, `.c`, `.cpp`, `.java`    |
| Archives  | `.zip`, `.rar`, `.7z`           |

## How It Works

1. Run the program.
2. Select **Organize Files**.
3. Enter the path of the folder you want to organize.
4. The program checks each file's extension.
5. It creates the required category folders.
6. Files are moved into their corresponding folders.

### Example

Before:

```text
Downloads/
├── photo.jpg
├── movie.mp4
├── notes.pdf
├── program.py
└── song.mp3
```

After:

```text
Downloads/
├── Images/
│   └── photo.jpg
├── Videos/
│   └── movie.mp4
├── Documents/
│   └── notes.pdf
├── Code/
│   └── program.py
└── Audio/
    └── song.mp3
```

## Requirements

* Python 3.x
* No external packages required

## Modules Used

```python
import os
import shutil
```

* `os` is used for working with files, folders, paths, and extensions.
* `shutil` is used to move files.

## Future Improvements

* Add an `Others` folder for unsupported files
* Handle duplicate filenames
* Show the number of files moved
* Add an undo option
* Organize files by date

## Author

Athrav Singh

B.Tech CSE Student
