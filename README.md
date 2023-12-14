# In-Memory File System

This Python project implements an in-memory file system with basic file and directory operations. The system provides functionalities similar to traditional file systems, allowing users to create directories, manipulate files, and navigate through the file system.

## Implementation Details

### Data Structures

The primary data structure used in this implementation is a Python dictionary (`file_system`), which represents the hierarchical structure of directories and files. Each key in the dictionary is a path to a directory or file, and the corresponding value is either a nested dictionary (for directories) or a string (for files).

### Design Decisions

- **Path Handling:** The project uses `os.path.join` to ensure cross-platform compatibility for file paths.
  
- **Command Line Interface:** The system provides a simple command-line interface for users to interact with the in-memory file system.

- **State Saving/Loading:** The project supports saving and loading the file system state to/from a JSON file. This allows users to persist the state across different sessions.

- **Dynamic Command Execution:** The `getattr` function is used to dynamically execute commands based on user input, allowing for extensibility.

## Setup

### Prerequisites

- Python 3.x installed on your machine.

### Setup Script

1. Clone the repository:

   ```bash
   git clone https://github.com/[Your GitHub Username]/in-memory-file-system.git
