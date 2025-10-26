"""
A Python script that processes data but intentionally lacks a shebang line.
This script demonstrates a runnable script without proper interpreter declaration.
"""
import os
import sys
import json
from datetime import datetime

def process_data(input_file):
    """Process data from the input file and return results."""
    try:
        with open(input_file, 'r') as f:
            data = json.load(f)
        
        # Simple processing - count items and add timestamp
        result = {
            "item_count": len(data),
            "processed_at": datetime.now().isoformat(),
            "status": "success"
        }
        
        return result
    except Exception as e:
        print(f"Error processing data: {e}")
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: data_processor.py <input_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    result = process_data(input_file)
    print(json.dumps(result, indent=2))

# Made with Bob
