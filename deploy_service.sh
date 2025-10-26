"""
A shell script for deployment that intentionally lacks a shebang line.
This script demonstrates a shell script without proper interpreter declaration.
"""

# Setup variables
SERVICE_NAME="app-service"
DEPLOY_DIR="/opt/services"
LOG_FILE="deployment.log"

# Create log entry
echo "Starting deployment at $(date)" > $LOG_FILE

# Check if service directory exists
if [ ! -d "$DEPLOY_DIR" ]; then
    echo "Creating service directory..." >> $LOG_FILE
    mkdir -p $DEPLOY_DIR
fi

# Copy files
echo "Copying service files..." >> $LOG_FILE
cp -r ./dist/* $DEPLOY_DIR/$SERVICE_NAME/

# Set permissions
echo "Setting permissions..." >> $LOG_FILE
chmod +x $DEPLOY_DIR/$SERVICE_NAME/bin/*

# Restart service
echo "Restarting service..." >> $LOG_FILE
systemctl restart $SERVICE_NAME

echo "Deployment completed at $(date)" >> $LOG_FILE

# Made with Bob
