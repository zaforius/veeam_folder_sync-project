# Folder Synchronization Tool

This project consists of a Python script designed to synchronize the contents of a source folder with a replica folder. It was developed to showcase my abilities in Python programming, Git version control, and project design as part of my application for a Python developer position at Veeam.

## Features

- **One-way synchronization**: Ensures the replica folder mirrors the source folder.
- **Logging**: Tracks and logs all file operations to both the console and a log file.
- **Configurable**: Users can specify paths and synchronization intervals via command-line arguments.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.6 or higher
- Git (for cloning the repository)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/folder-sync-project.git
   cd folder-sync-project
2. **Set up a virtual environment (Optional but recommended):**
   ```bash
   python -m venv veaam_env 
   source veaam_env/Scripts/activate # Use this command on Windows with Git Bash
3. **Install required packages:**
   ```bash
   pip install -r requirements.txt
### Usage
  To run the synchronization script, use the following command:
  ```bash
   python sync_folders.py <source_path> <replica_path> --log <log_file_path> --interval <sync_interval>
  ```

- <source_path>: The path to the source directory.
- <replica_path>: The path to the replica directory.
- <log_file_path>: Path where the log file will be stored.
- <sync_interval>: Time in seconds between each sync operation.

**Example:**

```bash

python sync_folders.py C:\Users\zafor\Desktop\py\synctest\source C:\Users\zafor\Desktop\py\synctest\replica --log C:\Users\zafor\Desktop\py\synctest\logs\sync.log --interval 2

```

## Thanks
I would like to thank the Veeam recruiting team for giving me the opportunity to participate in this selection process. 
I am excited about the possibility of contributing to and growing with such a renowned team.


