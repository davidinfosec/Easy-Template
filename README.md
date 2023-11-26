# Easy-Template Generator

## Overview

The Easy Template Generator, named `etgen.py`, is a Python script designed to automate the creation of folder structures for template-based sessions on specific days of the week. (every Monday, Tuesday, etc.,) It sets up folders, subfolders, and template files for various use-cases, allowing customization of the setup process.

## Usage

1. **Run the Script:**
    - Ensure that you have Python installed on your system.
    - Execute the script in a terminal or command prompt.

    ```bash
    python etgen.py
    ```

2. **Follow the Prompts:**
    - Enter the month and year for the session.
    - Specify the day of the week for your sessions.
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
- **Parent Template Folder:** The 'parent' template folder contains files that are common to all sessions in a given month. These files are copied to the root folder for the first occurrence of the specified day in the month.
- **Subfolder Template Folder:** The 'sub' template folder contains files that are specific to each subfolder (session). Each subfolder gets its set of template files copied from this folder.

## Handling Concurrent Days

- The script intelligently handles sessions on concurrent days of the week. For example, if you have sessions every Monday and Wednesday, the script will create separate folder structures for each day.
- It calculates the occurrences of the specified day in the month and generates the corresponding folder structure for each occurrence.
- The session folders are uniquely named to distinguish between different occurrences on the same day.

## Notes

- ⚠️ **Warning:** If you specify more than 100 subfolders, consider the impact on your system's performance and file management.

## Changelog November 26th, 2023

- Introduced 'Template' folder structure with 'parent' and 'sub' subfolders.
- Enhanced template handling: 
  - Copies one template file from 'parent' to the root folder.
  - Copies individual template files from 'sub' to respective subfolders.
- Improved user prompts and warnings.
- Addressed issue with multiple template files in the parent folder.
- Preserved original file names in subfolders.
- Code readability and comment updates.


### Support and Contributions

If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request. Your contributions are highly appreciated.

Feel like this has been useful? Donate toward my latest projects. https://www.poof.io/tip/@davidinfosec
