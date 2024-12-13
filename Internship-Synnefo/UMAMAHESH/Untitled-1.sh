#!/bin/bash

# Set the directory to clean up
CLEANUP_DIR="/path/to/directory"

# Set the file extensions to delete
DELETE_EXTENSIONS=( ".tmp" ".log" ".bak" ".old" )

# Set the maximum age of files to delete (in days)
MAX_AGE=30

# Set the minimum size of files to delete (in MB)
MIN_SIZE=100

# Delete files by extension
for EXT in "${DELETE_EXTENSIONS[@]}"; do
  find "$CLEANUP_DIR" -type f -name "*$EXT" -delete
done

# Delete files by age
find "$CLEANUP_DIR" -type f -mtime +$MAX_AGE -delete

# Delete files by size
find "$CLEANUP_DIR" -type f -size +${MIN_SIZE}M -delete

# Delete empty directories
find "$CLEANUP_DIR" -type d -empty -delete