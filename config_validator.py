#!/usr/bin/env python3
"""
A Python script with a proper shebang line.
This script demonstrates correct interpreter declaration.
"""
import os
import sys
import yaml
import argparse
from pathlib import Path

def validate_config(config_file):
    """Validate the configuration file structure and values."""
    try:
        with open(config_file, 'r') as f:
            config = yaml.safe_load(f)
        
        # Check required sections
        required_sections = ['app', 'database', 'logging']
        missing_sections = [s for s in required_sections if s not in config]
        
        if missing_sections:
            return False, f"Missing required sections: {', '.join(missing_sections)}"
        
        # Validate database connection
        if 'connection_string' not in config['database']:
            return False, "Missing database connection string"
        
        return True, "Configuration is valid"
    except Exception as e:
        return False, f"Error validating config: {e}"

def main():
    parser = argparse.ArgumentParser(description='Validate configuration file')
    parser.add_argument('config_file', help='Path to the configuration file')
    args = parser.parse_args()
    
    if not os.path.exists(args.config_file):
        print(f"Error: Config file not found: {args.config_file}")
        sys.exit(1)
    
    valid, message = validate_config(args.config_file)
    print(message)
    
    if not valid:
        sys.exit(1)
    
    print("Configuration validation successful")

if __name__ == "__main__":
    main()

# Made with Bob
