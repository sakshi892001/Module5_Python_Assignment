## Module 5: Files, Exceptions, and Errors in Python Assignment

## Overview

This repository contains two Python scripts for the Module 5 assignment of the Tutedude Python course, focusing on file handling and exception management:

1. **read_file.py**: Opens and reads a text file named sample.txt, printing its content line by line, with error handling for non-existent files.

2. **write_file.py**: Takes user input, writes it to output.txt using r+ mode, appends additional data, and displays the final content.

## Prerequisites

- Python 3.x installed (verify with `python --version`).
- Git installed (verify with `git --version`).
- Visual Studio Code (VS Code) with Git extension enabled.

## Repository Setup

1. **Clone the Repository**:

- Clone this repository to your local machine:

     ```bash
     git clone https://github.com/sakshi892001/Module5_Python_Assignment.git

2. **Navigate to the Repository Folder:**

     ```bash
     cd Module5_Python_Assignment

3. **Run the scripts**:

      ```bash
     python read_file.py
     python write_file.py

## Task 1: Read a File and Handle Errors

- File: read_file.py
- Functionality: Opens and reads sample.txt, prints its content line by line, and handles errors if the file does not exist using exception handling.

## Task 2: Write and Append Data to a File

- File: write_append_file.py
- Functionality: Takes user input, writes it to output.txt using r+ mode, appends additional data by moving the file pointer to the end, and reads/displays the final content. Handles errors for file operations.

## Error Handling

- Task 1:
  - Catches FileNotFoundError for non-existent files.
  - Catches IOError for other file-related errors (e.g., permission issues).

- Task 2:
  - Catches FileNotFoundError for issues opening output.txt.
  - Catches IOError for file operation failures.
  - Catches general exceptions for unexpected errors.

## Notes

- Ensure Python is installed and added to your system's PATH.

- Test the scripts with various scenarios (e.g., missing file, invalid permissions) to verify robustness.
