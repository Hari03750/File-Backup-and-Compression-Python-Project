# 🗂️ File Backup & Compression (Python Project)

## 📌 Overview
This project is a simple **file backup and compression tool** written in Python.  
It automatically compresses a source folder into a `.zip` archive and saves it in a backup directory with a **timestamp**.  

Useful for:  
- Automating backups  
- Archiving important files  
- Practicing Python file handling & automation  

---

## ⚡ Features
- ✅ Selects files from a **source folder (`testdata`)**  
- ✅ Creates a **backup folder** if it does not exist  
- ✅ Archives files into a **timestamped `.zip` file**  
- ✅ Works on **Windows** and can be adapted for Linux  

---

## 📂 Project Structure
backup_windows.py/
│── backup-script.py # Python script
│── backup/ # Backup .zip files will be stored here
│── testdata/ # Source folder with sample files
│ ├── file1.txt
│ ├── file2.txt
│── README.md # Project description

---

## 🚀 How to Run
1. Create a folder `testdata` and put some files inside (e.g., `file1.txt`, `file2.txt`).  
2. Open `backup-script.py` in **IDLE** (or any Python IDE).  
3. Run the script (`F5` in IDLE).  

Expected Output:
✅ Backup successful: backup\backup_YYYYMMDD_HHMMSS.zip

---

## 🛠️ Tech Used
- Python 3  
- `os`, `shutil`, `time`, `pathlib` libraries  

---

## 📸 Example Output

---

## 🛠️ Tech Used
- Python 3  
- `os`, `shutil`, `time`, `pathlib` libraries  

---

## 📸 Example Output
✅ Backup successful: backup\backup_20250903_222914.zip

---

## ✨ Future Improvements
- Add email notification after backup  
- Allow user to select source folder dynamically  
- Automate backups with a scheduler (Windows Task Scheduler / Cron)  

---

✅ With this project, I practiced **Python scripting, file handling, and automation** — skills relevant for **System Engineer roles**.  
