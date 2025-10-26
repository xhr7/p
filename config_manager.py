"""
A Python module that uses environment-driven or configuration-driven values.
This file demonstrates proper usage of configuration instead of hardcoding.
"""
import os
import json
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ConfigManager:
    def __init__(self, config_file=None):
        # Get data directory from environment variable or use default
        self.data_directory = os.environ.get('APP_DATA_DIR', './data')
        
        # Get backup directory from environment variable or use default
        self.backup_directory = os.environ.get('APP_BACKUP_DIR', './backups')
        
        # Get API endpoint from environment variable
        self.api_endpoint = os.environ.get('API_ENDPOINT', 'https://api.example.com')
        
        # Get database connection string from environment variable
        self.db_connection = os.environ.get('DB_CONNECTION_STRING', 'sqlite:///./app.db')
        
        # Load additional configuration from file if provided
        self.config = {}
        if config_file:
            self._load_config_file(config_file)
    
    def _load_config_file(self, config_file):
        """Load configuration from a JSON file."""
        try:
            with open(config_file, 'r') as f:
                self.config = json.load(f)
            logging.info(f"Configuration loaded from {config_file}")
        except Exception as e:
            logging.error(f"Error loading configuration: {e}")
    
    def get_data_path(self, filename=None):
        """Get the path to the data directory or a specific file within it."""
        path = Path(self.data_directory)
        path.mkdir(exist_ok=True, parents=True)
        
        if filename:
            return path / filename
        return path
    
    def get_backup_path(self):
        """Get the path to the backup directory."""
        path = Path(self.backup_directory)
        path.mkdir(exist_ok=True, parents=True)
        return path
    
    def get_api_url(self, endpoint=None):
        """Get the full API URL for a specific endpoint."""
        if endpoint:
            return f"{self.api_endpoint.rstrip('/')}/{endpoint.lstrip('/')}"
        return self.api_endpoint
    
    def get_config_value(self, key, default=None):
        """Get a configuration value from the loaded config or environment."""
        # First check in loaded config
        if key in self.config:
            return self.config[key]
        
        # Then check in environment variables
        env_key = f"APP_{key.upper()}"
        if env_key in os.environ:
            return os.environ[env_key]
        
        # Return default if not found
        return default

# Example usage
if __name__ == "__main__":
    config = ConfigManager()
    data_path = config.get_data_path("users.json")
    api_url = config.get_api_url("users/list")
    
    logging.info(f"Data path: {data_path}")
    logging.info(f"API URL: {api_url}")
    logging.info(f"Database connection: {config.db_connection}")

# Made with Bob
