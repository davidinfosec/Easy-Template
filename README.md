# Easy-Template Generator

## Overview

The Easy Template Generator, named `etgen.py`, is a Python script designed to automate the creation of folder structures for template-based sessions. It sets up folders, subfolders, and template files for various use-cases, allowing customization of the setup process.

## Usage

1. **Run the Script:**
    - Ensure that you have Python installed on your system.
    - Execute the script in a terminal or command prompt.

    ```bash
    python etgen.py
    ```

2. **Follow the Prompts:**
    - Enter the month and year for the session.
    - Choose the day of the week for your sessions (e.g., Monday, Tuesday, etc.) or customize your own day.
    - Specify the number of subfolders you want (no limit, but a warning will be displayed if more than 100 is specified).
    - The script will create the necessary folder structure, subfolders, and template files.

3. **Session Setup:**
    - Open your preferred application and load the generated template files for your session.

## Folder Structure

The script generates a folder structure for each session:

- **Root Folder:** `ET MM-DD-YYYY <day_name>`
  - `1/`, `2/`, ..., `n/`: Subfolders for individual sessions (n is the specified number of subfolders).
    - `1.xxx`, `2.xxx`, ..., `n.xxx`: Template files for each session.
  - `README.md`: Information about the generated folder.

## Template Handling

- The script dynamically populates the day name in the folder based on the specified day in the script.
- If you choose to use template files, it assumes that a template file named `template.xxx` is present in the same folder as the script.
- Template files are copied into both the root folder and individual subfolders as needed.

## Notes

- Please do not manually edit any generated files to ensure the proper functioning of the sessions.
- ⚠️ **Warning:** If you specify more than 100 subfolders, consider the impact on your system's performance and file management.


### Changelog November 26th, 2023

- Introduced 'Template' folder structure with 'parent' and 'sub' subfolders.
- Enhanced template handling: 
  - Copies one template file from 'parent' to the root folder.
  - Copies individual template files from 'sub' to respective subfolders.
- Improved user prompts and warnings.
- Addressed issue with multiple template files in the parent folder.
- Preserved original file names in subfolders.
- Code readability and comment updates.

