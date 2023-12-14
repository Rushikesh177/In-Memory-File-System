# In-Memory File System

This Python project implements an in-memory file system with basic file and directory operations. The system provides functionalities similar to traditional file systems, allowing users to create directories, manipulate files, and navigate through the file system.

## Features

- **mkdir:** Create a new directory.
- **cd:** Change the current directory.
- **ls:** List the contents of the current or specified directory.
- **touch:** Create a new empty file.
- **cat:** Display the contents of a file.
- **echo:** Write text to a file.
- **mv:** Move a file or directory to a new location.
- **cp:** Copy a file or directory to a new location.
- **rm:** Remove a file or directory.
- **save_state:** Save the current file system state to a file.
- **load_state:** Load a previously saved file system state.

## Implementation Details

### Data Structures

The primary data structure used in this implementation is a Python dictionary (`file_system`), which represents the hierarchical structure of directories and files. Each key in the dictionary is a path to a directory or file, and the corresponding value is either a nested dictionary (for directories) or a string (for files).

### Design Decisions

- **Path Handling:** The project uses `os.path.join` to ensure cross-platform compatibility for file paths.
  
- **Command Line Interface:** The system provides a simple command-line interface for users to interact with the in-memory file system.

- **State Saving/Loading:** The project supports saving and loading the file system state to/from a JSON file. This allows users to persist the state across different sessions.


## Setup

### Prerequisites

- Python 3.x installed on your machine.

### Setup Script

1. Clone the repository:

   ```bash
   git clone https://github.com/Rushikesh177/In-Memory-File-System.git
    ```
2. Change into the project directory:
   ```bash
   cd in-memory-file-system
    ```
3. Run the script:
    ```bash
   python InMemoryFileSystem.py
    ```
4. Alternatively, you can use Docker to run the project. A Dockerfile is provided for this purpose. (you need to install Docker first from their official website.
     ```bash
   docker build -t any-name-of-yours-for-image .

    ```

      ```bash
   winpty docker run -it same-name-of-yours-for-image
    ```
5. Enter commands at the prompt. For example:
   
      ```bash
   Enter command (type 'exit' to end): mkdir folder1
    ```
   
     ```bash
     mkdir folder2
     cd folder2
     touch file.txt
     echo "hello this is working?" file.txt
     cat file.txt


    ```
6. move command :
     ```bash
       mv folder2/file.txt folder1/
    ```  

7. remove command
    ```bash
      rm file.txt
    ```

8. Save state and Load state : (//state saved to json file and stored in the project repository)
    ```bash
      save_state 'any_state_name.json'
      load_state 'that_state_name.json'
  ```

9. exit command : exit

   
   

