```markdown
# Windows Temp Files Cleaner

This is a simple Python script that cleans up temporary files in Windows. No more typing `%temp%` or other stuff in the Run box! It clears out files in three folders: `%TEMP%`, `C:\Windows\Prefetch`, and `C:\Windows\Temp` to free up disk space.

## What You Need
- Windows (like Windows 10 or 11).
- Python 3.6 or higher (if you want to run the script directly). Download it from [python.org](https://www.python.org/downloads/) and make sure to check "Add Python to PATH" during installation.
- Admin access to delete system files in `C:\Windows\Temp` and `C:\Windows\Prefetch`.
- PyInstaller (if you want to turn it into an `.exe` file, explained below).

## How to Run the Script
If you have Python installed, you can run the script directly:

1. Download the `clean_temp_files.py` file from this repository.
2. Open Command Prompt or PowerShell **as admin**:
   - Search for `cmd` or `PowerShell` in the Start menu.
   - Right-click and select "Run as administrator".
3. Go to the folder where you saved `clean_temp_files.py`:
   ```
   cd path_to_file
   ```
   Example: `cd C:\Users\YourUsername\Desktop`
4. Run the script:
   ```
   python clean_temp_files.py
   ```
5. When it asks "Are you sure you want to continue? (y/n):", type `y` to start cleaning.
6. You’ll see the deleted files or any errors. Press Enter at the end to close.

## How to Make an EXE File
If you don’t want to install Python, you can turn the script into an `.exe` file:

1. Install PyInstaller. Open Command Prompt or PowerShell (as admin) and run:
   ```
   pip install pyinstaller
   ```
2. Go to the folder with `clean_temp_files.py`:
   ```
   cd path_to_file
   ```
   Example: `cd C:\Users\YourUsername\Desktop`
3. Create the `.exe` file:
   ```
   pyinstaller --onefile clean_temp_files.py
   ```
4. Find the `clean_temp_files.exe` file in the `dist` folder.
5. **Run it as admin**:
   - Right-click the file and choose "Run as administrator".
6. When it asks "Are you sure you want to continue? (y/n):", type `y` to start cleaning.
7. You’ll see the output in the Command Prompt. Press Enter to close.

## Important Notes
- **Be careful**: This script permanently deletes files! Make sure there’s nothing important in `%TEMP%`, `C:\Windows\Prefetch`, or `C:\Windows\Temp`.
- If you see "Permission denied" errors, it means Windows is using some files. That’s normal, and the script will keep cleaning the rest.
- Back up any important files before running.
- Some antivirus programs might flag the `.exe` as suspicious. You can add it as an exception.

## What the Code Does
- `clean_temp()`: Clears the `%TEMP%` folder (user temp files).
- `clean_prefetch()`: Clears the `C:\Windows\Prefetch` folder (program speedup data).
- `clean_windows_temp()`: Clears the `C:\Windows\Temp` folder (system temp files).

## Got Ideas?
If you think I can add something cool (like a graphical interface or showing how much space was freed), let me know in the Issues section or send a Pull Request!

## License
This project is released under the [MIT License](LICENSE).

Made by [Mohammad Mehdi Eskandari]
```