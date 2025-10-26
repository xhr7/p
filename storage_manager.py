"""
A Python module that uses a hardcoded absolute file path.
This file demonstrates hardcoded path usage.
"""
import os
import shutil
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class StorageManager:
    def __init__(self):
        # Hardcoded path to a specific user directory for storing application data
        self.data_directory = "/Users/john.smith/Documents/app_data"
        
        # Hardcoded backup location
        self.backup_directory = "/Users/john.smith/Documents/app_backups"
    
    def ensure_directories(self):
        """Ensure that the data and backup directories exist."""
        os.makedirs(self.data_directory, exist_ok=True)
        os.makedirs(self.backup_directory, exist_ok=True)
        logging.info(f"Directories initialized: {self.data_directory}, {self.backup_directory}")
    
    def store_file(self, filename, content):
        """Store a file in the hardcoded data directory."""
        filepath = os.path.join(self.data_directory, filename)
        with open(filepath, 'w') as f:
            f.write(content)
        logging.info(f"File stored at {filepath}")
        return filepath
    
    def backup_data(self):
        """Backup all data to the hardcoded backup directory."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = os.path.join(self.backup_directory, f"backup_{timestamp}")
        
        shutil.copytree(self.data_directory, backup_path)
        logging.info(f"Backup created at {backup_path}")
        return backup_path

# Example usage
if __name__ == "__main__":
    manager = StorageManager()
    manager.ensure_directories()
    manager.store_file("test.txt", "This is a test file")
    manager.backup_data()

# Made with Bob
